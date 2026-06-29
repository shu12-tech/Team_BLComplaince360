# Team_BLCompliance360

> **AI-powered Continuous Compliance Engine using UiPath Maestro, AI Agents, FastAPI, LangChain, Mistral AI, UI Automation, and Intelligent Document Processing (IXP).**

---

## Overview

**Team_BLCompliance360** is an AI-powered Continuous Compliance Engine that automates enterprise compliance validation by combining intelligent automation and generative AI.

The solution continuously collects compliance evidence from enterprise systems, legacy applications, and business documents. The collected evidence is analyzed by an AI Compliance Agent, validated through a UiPath Revalidation Agent, and returned as a standardized compliance finding aligned with industry security frameworks.

This approach helps organizations reduce manual audit effort, improve compliance visibility, and accelerate security assessments while maintaining consistency and governance throughout the compliance process.

---

## Problem Statement

Enterprise compliance evidence is often distributed across multiple systems and formats, making compliance assessments complex and time-consuming.

Organizations commonly face challenges such as:

* Manual evidence collection
* Legacy applications without APIs
* Compliance reports stored as PDFs or scanned documents
* Multiple disconnected security tools
* Time-consuming audit preparation
* Inconsistent compliance reporting
* Delayed identification of security risks

Traditional compliance assessments provide only periodic visibility, making it difficult to maintain a continuous understanding of an organization's compliance posture.

---

## Solution

Team_BLCompliance360 provides an end-to-end automation solution that continuously validates enterprise compliance across multiple evidence sources.

The solution combines:

* UiPath Maestro for workflow orchestration
* FastAPI for enterprise integration
* AI Compliance Agent powered by LangChain and Mistral AI
* UiPath UI Automation for legacy systems
* UiPath Intelligent Document Processing (IXP)
* UiPath Revalidation Agent for validating AI-generated findings

By integrating these technologies, the platform delivers accurate, standardized, and auditable compliance results while minimizing manual intervention.

---

## Key Features

* Continuous compliance validation
* AI-powered compliance analysis
* Multi-source evidence collection
* Enterprise REST API integration
* Legacy application automation
* Intelligent Document Processing (IXP)
* SOC 2 control mapping
* Standardized compliance findings
* AI result revalidation
* Structured JSON output
* Modular and scalable architecture
* Open-source implementation

---

## Solution Components

### UiPath Maestro

UiPath Maestro orchestrates the complete compliance workflow by coordinating all automation activities, AI interactions, and decision-making processes.

### Evidence Collection

The platform supports three independent evidence sources:

**API Evidence**

* Access Reviews
* Infrastructure Security
* Security Operations
* Backup Validation
* Device Compliance
* Vulnerability Reports

**UI Automation**

UiPath Robots collect compliance evidence from legacy enterprise applications by comparing expected and actual application states.

Examples include:

* User status
* Role assignments
* Permissions
* Security configurations
* Access rights

**Intelligent Document Processing (IXP)**

Business documents are processed using UiPath Intelligent Document Processing.

Supported documents include:

* Audit Reports
* Compliance Reports
* Risk Assessments
* Backup Reports
* Security Policies
* Incident Reports

---

## AI Compliance Agent

The AI Compliance Agent is developed using Python, LangChain, and Mistral AI.

Based on the evidence source, the agent performs compliance validation by:

* Identifying compliance violations
* Mapping findings to SOC 2 controls
* Prioritizing the highest business risk
* Generating a standardized compliance finding
* Producing structured JSON output

---

## UiPath Revalidation Agent

Before the compliance finding is finalized, a UiPath Revalidation Agent performs an additional validation step.

The Revalidation Agent:

* Reviews the AI-generated finding
* Verifies that the finding is supported by the supplied evidence
* Confirms the selected SOC 2 control mapping
* Validates the assigned risk level
* Ensures the response follows the required JSON schema

This additional validation layer improves reliability, consistency, and trust in AI-assisted compliance assessments.

---

## Compliance Frameworks

The solution currently supports:

* SOC 2
* ISO 27001
* NIST Cybersecurity Framework (CSF)
* CIS Controls

Supported SOC 2 control mappings include:

* CC6.1 – Access Control
* CC6.2 – Identity Lifecycle
* CC7.2 – Threat Detection
* CC7.3 – Backup and Recovery
* CC7.4 – Logging and Monitoring
* CC8.1 – Risk Assessment

---

## Workflow

The compliance validation process consists of the following steps:

1. UiPath Maestro initiates the workflow.
2. Compliance evidence is collected from APIs, UI Automation, or Intelligent Document Processing.
3. Evidence is converted into a standardized JSON format.
4. The AI Compliance Agent analyzes the supplied evidence.
5. The agent identifies the highest-risk compliance issue and maps it to the appropriate SOC 2 control.
6. The generated finding is validated by the UiPath Revalidation Agent.
7. A standardized compliance result is returned to the workflow for downstream processing.

---

## Technology Stack

### Automation

* UiPath Maestro
* UiPath Studio
* UiPath Intelligent Document Processing (IXP)
* UiPath Revalidation Agent

### Artificial Intelligence

* LangChain
* Mistral AI
* Prompt Engineering

### Backend

* Python
* FastAPI
* REST APIs
* JSON

### Security Frameworks

* SOC 2
* ISO 27001
* NIST Cybersecurity Framework (CSF)
* CIS Controls

---

## Repository Structure

```
Team_BLCompliance360/
│
├── ComplianceAgent/
│   ├── agent.py
│   ├── api.py
│   ├── prompt.txt
│   └── data/
│
├── UiPath/
│   ├── Main.xaml
│   ├── project.json
│   └── Workflows/
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## Getting Started

### Prerequisites

* Python 3.10+
* UiPath Studio
* UiPath Maestro
* Mistral AI API Key
* Git

### Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/Team_BLCompliance360.git
```

Navigate to the project directory:

```bash
cd Team_BLCompliance360
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure your environment variables:

```env
MISTRAL_API_KEY=your_api_key
```

Start the FastAPI server:

```bash
uvicorn api:app --reload --port 8001
```

Open the UiPath project and execute the Main workflow.

---

## Sample Output

```json
{
  "RunId": "RUN-20260629-001",
  "ControlId": "CC6.1",
  "RiskLevel": "HIGH",
  "ConfidenceScore": 97,
  "Finding": "Administrator account observed without MFA enabled. This increases the risk of unauthorized privileged access. Enable MFA immediately."
}
```

---

## Future Enhancements

* Microsoft Defender integration
* Microsoft Sentinel integration
* AWS Security Hub integration
* Azure Security Center integration
* ServiceNow integration
* Splunk integration
* Automated remediation workflows
* Compliance dashboards
* Historical compliance analytics
* Additional compliance framework support

---

## Contributing

Contributions are welcome.

To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Submit a Pull Request.

Please ensure that all contributions include appropriate documentation and follow the existing project structure.

---

## License

This project is licensed under the **MIT License**.

See the **LICENSE** file for more information.

---

## Team

**Team_BLCompliance360**

Developed as a hackathon solution to demonstrate how **UiPath Maestro**, **AI Agents**, **FastAPI**, **LangChain**, **Mistral AI**, **UI Automation**, and **Intelligent Document Processing (IXP)** can be combined to automate enterprise compliance validation and deliver reliable, standardized, and auditable compliance assessments.

