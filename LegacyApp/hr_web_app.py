import json
import os
import sys
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from json import JSONDecodeError
from urllib.parse import urlparse


APP_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(APP_DIR, "database.json")
HOST = "127.0.0.1"
DEFAULT_PORT = 8765
REQUIRED_USER_FIELDS = ("username", "fullname", "email", "role", "status")
ALLOWED_STATUSES = ("Active", "Disabled")


HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Internal HR Database v2.1 (Build 2004)</title>
  <style>
    :root {
      color-scheme: dark;
      --bg: #0f172a;
      --panel: #1e293b;
      --panel-2: #111827;
      --line: #334155;
      --line-soft: #1e293b;
      --text: #f8fafc;
      --muted: #94a3b8;
      --accent: #4f46e5;
      --accent-hover: #6366f1;
      --teal: #0f766e;
      --danger: #be123c;
    }

    * {
      box-sizing: border-box;
    }

    body {
      margin: 0;
      background: var(--bg);
      color: var(--text);
      font-family: "Segoe UI", Arial, sans-serif;
      font-size: 13px;
    }

    #hr_app_main_window {
      width: min(1100px, calc(100vw - 32px));
      margin: 24px auto;
      border: 1px solid var(--line-soft);
      background: var(--bg);
    }

    nav {
      height: 38px;
      border-bottom: 1px solid var(--line-soft);
      display: flex;
      align-items: center;
      gap: 24px;
      padding: 0 18px;
      color: #cbd5e1;
    }

    main {
      display: grid;
      grid-template-columns: minmax(0, 1fr) 320px;
      gap: 12px;
      padding: 12px;
    }

    fieldset {
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--panel);
      min-width: 0;
    }

    legend {
      color: #38bdf8;
      font-weight: 700;
      padding: 0 8px;
    }

    .table-wrap {
      overflow: auto;
      min-height: 382px;
      background: var(--panel-2);
      border: 1px solid var(--line-soft);
    }

    table {
      width: 100%;
      border-collapse: collapse;
      table-layout: fixed;
    }

    th,
    td {
      text-align: left;
      border-bottom: 1px solid var(--line-soft);
      border-right: 1px solid var(--line-soft);
      padding: 9px 10px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    th {
      color: var(--muted);
      background: var(--panel);
      font-weight: 700;
    }

    tr[data-selected="true"] {
      background: var(--accent);
    }

    label {
      display: block;
      color: var(--muted);
      font-weight: 600;
      margin: 12px 0 6px;
    }

    input,
    select {
      width: 100%;
      height: 34px;
      border: 1px solid var(--line);
      border-radius: 6px;
      background: #0b1220;
      color: var(--text);
      padding: 6px 10px;
    }

    input:focus,
    select:focus {
      border-color: var(--accent-hover);
      outline: none;
    }

    .actions {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin-top: 18px;
    }

    button {
      border: 0;
      border-radius: 6px;
      color: white;
      font-weight: 700;
      padding: 9px 12px;
      background: var(--accent);
      cursor: pointer;
    }

    button:hover {
      background: var(--accent-hover);
    }

    #refresh_button {
      background: #334155;
    }

    #copy_table_button {
      grid-column: 1 / -1;
      background: var(--teal);
    }

    #automation_status_label {
      border-top: 1px solid var(--line-soft);
      padding: 8px 14px;
      color: var(--muted);
      text-align: right;
      font-size: 12px;
    }

    .error {
      color: #fecdd3;
    }
  </style>
</head>
<body>
  <section id="hr_app_main_window" aria-label="hr_app_main_window">
    <nav aria-label="main_menu">
      <span>File</span><span>Edit</span><span>View</span><span>Tools</span><span>Help</span>
    </nav>

    <main>
      <fieldset id="active_accounts_group" aria-label="active_accounts_group">
        <legend>Active Accounts Table</legend>
        <div class="table-wrap">
          <table id="accounts_table" aria-label="accounts_table">
            <thead>
              <tr>
                <th id="col_username" data-field="username">Username</th>
                <th id="col_fullname" data-field="fullname">Full Name</th>
                <th id="col_email" data-field="email">Email</th>
                <th id="col_role" data-field="role">Role</th>
                <th id="col_status" data-field="status">Status</th>
              </tr>
            </thead>
            <tbody id="accounts_table_body"></tbody>
          </table>
        </div>
      </fieldset>

      <fieldset id="account_properties_group" aria-label="account_properties_group">
        <legend>Account Properties</legend>

        <label id="username_label" for="username_entry">Username:</label>
        <input id="username_entry" name="username" autocomplete="off">

        <label id="fullname_label" for="fullname_entry">Full Name:</label>
        <input id="fullname_entry" name="fullname" autocomplete="off">

        <label id="email_label" for="email_entry">Email:</label>
        <input id="email_entry" name="email" autocomplete="off">

        <label id="role_label" for="role_entry">Role:</label>
        <input id="role_entry" name="role" autocomplete="off">

        <label id="status_label" for="status_dropdown">Status:</label>
        <select id="status_dropdown" name="status">
          <option value="Active">Active</option>
          <option value="Disabled">Disabled</option>
        </select>

        <div class="actions">
          <button id="refresh_button" type="button">Refresh</button>
          <button id="save_button" type="button">Save Changes</button>
          <button id="copy_table_button" type="button">Copy Table Data</button>
        </div>
      </fieldset>
    </main>

    <div id="automation_status_label" aria-live="polite">READY</div>
  </section>

  <script>
    const fields = ["username", "fullname", "email", "role", "status"];
    let users = [];
    let selectedIndex = null;

    function setStatus(code, message = "") {
      const status = document.getElementById("automation_status_label");
      status.textContent = code;
      status.dataset.code = code;
      status.dataset.message = message;
    }

    function escapeText(value) {
      return String(value ?? "");
    }

    function getFormUser() {
      return {
        username: document.getElementById("username_entry").value.trim(),
        fullname: document.getElementById("fullname_entry").value.trim(),
        email: document.getElementById("email_entry").value.trim(),
        role: document.getElementById("role_entry").value.trim(),
        status: document.getElementById("status_dropdown").value
      };
    }

    function setFormUser(user = {}) {
      document.getElementById("username_entry").value = user.username ?? "";
      document.getElementById("fullname_entry").value = user.fullname ?? "";
      document.getElementById("email_entry").value = user.email ?? "";
      document.getElementById("role_entry").value = user.role ?? "";
      document.getElementById("status_dropdown").value = user.status ?? "Active";
    }

    function renderTable() {
      const tbody = document.getElementById("accounts_table_body");
      tbody.innerHTML = "";
      users.forEach((user, index) => {
        const row = document.createElement("tr");
        row.id = `account_row_${index + 1}`;
        row.dataset.index = String(index);
        row.dataset.username = user.username;
        row.dataset.selected = index === selectedIndex ? "true" : "false";
        row.setAttribute("aria-label", `account_row_${index + 1}_${user.username}`);
        fields.forEach((field) => {
          const cell = document.createElement("td");
          cell.id = `account_row_${index + 1}_${field}`;
          cell.dataset.field = field;
          cell.textContent = escapeText(user[field]);
          row.appendChild(cell);
        });
        row.addEventListener("click", () => selectRow(index));
        tbody.appendChild(row);
      });
      document.getElementById("accounts_table").dataset.rowCount = String(users.length);
    }

    function selectRow(index) {
      selectedIndex = index;
      setFormUser(users[index]);
      renderTable();
      setStatus("ROW_SELECTED", users[index].username);
    }

    function validateUser(user) {
      for (const field of fields) {
        if (!user[field]) {
          throw new Error(`${field} is required.`);
        }
      }
      if (!["Active", "Disabled"].includes(user.status)) {
        throw new Error("status must be Active or Disabled.");
      }
      const duplicate = users.some((existing, index) =>
        index !== selectedIndex && existing.username === user.username
      );
      if (duplicate) {
        throw new Error(`username '${user.username}' already exists.`);
      }
    }

    async function loadUsers() {
      try {
        const response = await fetch("/api/users", { cache: "no-store" });
        const payload = await response.json();
        if (!response.ok) {
          throw new Error(payload.error || "Load failed.");
        }
        users = payload.users;
        selectedIndex = null;
        setFormUser();
        renderTable();
        setStatus("LOAD_SUCCESS", `${users.length} row(s) loaded`);
      } catch (error) {
        users = [];
        selectedIndex = null;
        setFormUser();
        renderTable();
        setStatus("LOAD_ERROR", error.message);
      }
    }

    async function saveSelectedUser() {
      if (selectedIndex === null) {
        setStatus("VALIDATION_ERROR", "Select a user first.");
        return;
      }
      const updatedUser = getFormUser();
      try {
        validateUser(updatedUser);
        const nextUsers = users.map((user, index) => index === selectedIndex ? updatedUser : user);
        const response = await fetch("/api/users", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ users: nextUsers })
        });
        const payload = await response.json();
        if (!response.ok) {
          throw new Error(payload.error || "Save failed.");
        }
        users = payload.users;
        renderTable();
        setStatus("SAVE_SUCCESS", updatedUser.username);
      } catch (error) {
        setStatus("VALIDATION_ERROR", error.message);
      }
    }

    async function copyTableData() {
      const header = fields.join("\\t");
      const rows = users.map((user) => fields.map((field) => escapeText(user[field])).join("\\t"));
      const tsv = [header, ...rows].join("\\n");
      await navigator.clipboard.writeText(tsv);
      setStatus("COPY_SUCCESS", `${users.length} row(s) copied`);
    }

    document.getElementById("refresh_button").addEventListener("click", loadUsers);
    document.getElementById("save_button").addEventListener("click", saveSelectedUser);
    document.getElementById("copy_table_button").addEventListener("click", copyTableData);
    document.addEventListener("keydown", (event) => {
      if (event.ctrlKey && event.shiftKey && event.key.toLowerCase() === "c") {
        event.preventDefault();
        copyTableData();
      }
    });
    loadUsers();
  </script>
</body>
</html>
"""


def load_users():
    if not os.path.exists(DB_PATH):
        raise ValueError("database.json not found.")
    try:
        with open(DB_PATH, "r", encoding="utf-8") as file:
            users = json.load(file)
    except JSONDecodeError as exc:
        raise ValueError("database.json contains invalid JSON.") from exc
    validate_users(users)
    return users


def validate_users(users):
    if not isinstance(users, list):
        raise ValueError("database.json must contain a list of users.")

    seen_usernames = set()
    for index, user in enumerate(users):
        if not isinstance(user, dict):
            raise ValueError(f"User record {index + 1} must be an object.")
        missing = [field for field in REQUIRED_USER_FIELDS if field not in user]
        if missing:
            raise ValueError(f"User record {index + 1} is missing: {', '.join(missing)}.")

        normalized = {}
        for field in REQUIRED_USER_FIELDS:
            value = str(user[field]).strip()
            if not value:
                raise ValueError(f"User record {index + 1} has empty {field}.")
            normalized[field] = value
        if normalized["status"] not in ALLOWED_STATUSES:
            raise ValueError(f"User '{normalized['username']}' has unsupported status.")
        if normalized["username"] in seen_usernames:
            raise ValueError(f"Duplicate username: {normalized['username']}.")
        seen_usernames.add(normalized["username"])
        user.update(normalized)


def save_users(users):
    validate_users(users)
    temp_path = f"{DB_PATH}.tmp"
    with open(temp_path, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)
        file.write("\n")
        file.flush()
        os.fsync(file.fileno())
    os.replace(temp_path, DB_PATH)


class HRRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = urlparse(self.path).path
        if path in ("/", "/index.html"):
            self.send_text(HTML, "text/html; charset=utf-8")
            return
        if path == "/api/users":
            try:
                self.send_json({"users": load_users()})
            except ValueError as exc:
                self.send_json({"error": str(exc)}, status=400)
            return
        self.send_json({"error": "Not found."}, status=404)

    def do_POST(self):
        path = urlparse(self.path).path
        if path != "/api/users":
            self.send_json({"error": "Not found."}, status=404)
            return

        try:
            length = int(self.headers.get("Content-Length", "0"))
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
            users = payload.get("users")
            save_users(users)
            self.send_json({"users": users})
        except (JSONDecodeError, UnicodeDecodeError):
            self.send_json({"error": "Invalid JSON request."}, status=400)
        except ValueError as exc:
            self.send_json({"error": str(exc)}, status=400)
        except OSError as exc:
            self.send_json({"error": f"Save failed: {exc}"}, status=500)

    def log_message(self, format, *args):
        return

    def send_json(self, payload, status=200):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def send_text(self, text, content_type, status=200):
        body = text.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def parse_port():
    if len(sys.argv) >= 2:
        return int(sys.argv[1])
    return DEFAULT_PORT


def main():
    port = parse_port()
    server = ThreadingHTTPServer((HOST, port), HRRequestHandler)
    url = f"http://{HOST}:{port}/"
    print(f"Serving Internal HR Database at {url}")
    print("Press Ctrl+C to stop.")
    try:
        webbrowser.open(url)
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
