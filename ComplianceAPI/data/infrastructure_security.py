from fastapi import APIRouter

router = APIRouter()

@router.get("/api/infrastructure-security")
def infrastructure_security():

    return {
        "devices": [
            {
                "hostname": "FIN-LAPTOP-01",
                "antivirus": True,
                "encryption": True,
                "status": "Compliant"
            },
            {
                "hostname": "HR-LAPTOP-02",
                "antivirus": False,
                "encryption": False,
                "status": "Non-Compliant"
            }
        ],
        "systems": [
            {
                "system": "CustomerDB",
                "lastBackup": "2026-06-01",
                "status": "Success"
            },
            {
                "system": "FinanceDB",
                "lastBackup": "2026-05-01",
                "status": "Failed"
            }
        ],
        "findings": [
            {
                "asset": "WEB-SERVER-01",
                "severity": "Critical",
                "cvss": 9.8,
                "daysOpen": 45
            },
            {
                "asset": "APP-SERVER-02",
                "severity": "Medium",
                "cvss": 5.1,
                "daysOpen": 3
            }
        ]
    }