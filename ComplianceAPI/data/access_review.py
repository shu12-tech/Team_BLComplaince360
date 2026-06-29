from fastapi import APIRouter

router = APIRouter()

@router.get("/api/access-review")
def access_review():

    return {
        "users": [
            {
                "username": "admin01",
                "role": "Administrator",
                "mfaEnabled": False,
                "lastLoginDays": 120,
                "status": "Active"
            },
            {
                "username": "finance.user",
                "role": "Finance",
                "mfaEnabled": True,
                "lastLoginDays": 2,
                "status": "Active"
            },
            {
                "username": "contractor01",
                "role": "Contractor",
                "mfaEnabled": False,
                "lastLoginDays": 90,
                "status": "Active"
            }
        ],
        "policies": [
            {
                "policyName": "AdminFullAccess",
                "effect": "Allow",
                "action": "*",
                "resource": "*"
            },
            {
                "policyName": "FinanceReadOnly",
                "effect": "Allow",
                "action": ["read"],
                "resource": "FinanceDB"
            }
        ]
    }