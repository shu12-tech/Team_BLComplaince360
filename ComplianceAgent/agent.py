import json
from pathlib import Path

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage

# ==========================================
# MISTRAL API KEY
# ==========================================

API_KEY = "lpsv2HFf38ngXYX0MGqC4sy9R5cr0RuX"

# ==========================================
# LOAD PROMPT
# ==========================================

BASE_DIR = Path(__file__).resolve().parent
PROMPT_PATH = BASE_DIR / "prompt.txt"

if not PROMPT_PATH.exists():
    raise FileNotFoundError(f"Prompt file not found: {PROMPT_PATH}")

PROMPT_TEMPLATE = PROMPT_PATH.read_text(encoding="utf-8")

# ==========================================
# INITIALIZE MISTRAL
# ==========================================

llm = ChatMistralAI(
    model="mistral-large-latest",
    api_key=API_KEY,
    temperature=0
)

# ==========================================
# MAIN FUNCTION
# ==========================================

def analyze_compliance(response_json):

    try:

        print("========== INPUT ==========")
        print(response_json)

        payload = json.loads(response_json)

        prompt = PROMPT_TEMPLATE.replace(
            "{evidence}",
            json.dumps(payload, indent=2)
        )

        print("Calling Mistral...")

        response = llm.invoke(
            [HumanMessage(content=prompt)]
        )

        result = response.content.strip()

        result = (
            result.replace("```json", "")
                  .replace("```", "")
                  .strip()
        )

        parsed = json.loads(result)

        print("========== OUTPUT ==========")
        print(json.dumps(parsed, indent=2))

        return json.dumps(parsed)

    except Exception as e:

        return json.dumps({
            "status": "ERROR",
            "message": str(e)
        })


# ==========================================
# LOCAL TEST
# ==========================================

if __name__ == "__main__":

    sample_json = """
    {
        "source":"uiautomation",
        "data":{
            "expected":[
                {
                    "Username":"john.doe",
                    "Status":"Disabled"
                }
            ],
            "actual":[
                {
                    "Username":"john.doe",
                    "Status":"Active"
                }
            ]
        }
    }
    """

    output = analyze_compliance(sample_json)

    print(output)