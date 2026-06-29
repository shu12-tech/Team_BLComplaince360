from fastapi import FastAPI, Body
import json

from agent import analyze_compliance

app = FastAPI(
    title="Compliance Agent API",
    version="1.0"
)

@app.post("/analyze")
def analyze(request: dict = Body(...)):

    # Convert incoming JSON to string
    input_json = json.dumps(request)

    # Run your compliance agent
    result = analyze_compliance(input_json)

    # Return JSON
    return json.loads(result)