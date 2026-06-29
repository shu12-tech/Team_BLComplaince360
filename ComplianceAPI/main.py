from fastapi import FastAPI
import requests

from data.access_review import router as access_router
from data.infrastructure_security import router as infrastructure_router
from data.security_operations import router as security_router

app = FastAPI(
    title="Continuous Compliance Engine",
    version="1.0"
)

app.include_router(access_router)
app.include_router(infrastructure_router)
app.include_router(security_router)

BASE_URL = "https://masses-uncured-rockband.ngrok-free.dev"

ACCESS_API = f"{BASE_URL}/api/access-review"
INFRA_API = f"{BASE_URL}/api/infrastructure-security"
SECURITY_API = f"{BASE_URL}/api/security-operations"


@app.get("/")
def root():
    return {
        "status": "Running"
    }


@app.get("/api/compliance-analysis")
def compliance_analysis():

    access = requests.get(ACCESS_API).json()
    infra = requests.get(INFRA_API).json()
    security = requests.get(SECURITY_API).json()

    return {
        "access_review": access,
        "infrastructure_security": infra,
        "security_operations": security
    }