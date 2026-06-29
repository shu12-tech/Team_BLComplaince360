from fastapi import APIRouter

router = APIRouter()

@router.get("/api/security-operations")
def security_operations():

    return {
        "alerts": [
            {
                "alertId": "ALT-1001",
                "severity": "Critical",
                "eventType": "Unauthorized Database Access",
                "status": "Open"
            },
            {
                "alertId": "ALT-1002",
                "severity": "High",
                "eventType": "Multiple Failed Admin Logins",
                "status": "Open"
            }
        ],
        "employees": [
            {
                "employeeId": "EMP001",
                "trainingCompleted": True
            },
            {
                "employeeId": "EMP002",
                "trainingCompleted": False
            }
        ]
    }