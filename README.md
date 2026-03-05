For the project Run (1 , 2)

1.  & C:/Users/Lenovo/.virtualenvs/DocuQuery-main-V_M28mqC/Scripts/Activate.ps1   <!-- create virtual environment -->
2.  python c:/Users/Lenovo/Desktop/clara_agent_project/run_pipeline.py   <!-- now run this project -->




                                 # Clara Agent Automation Pipeline #

This project simulates the Clara Answers onboarding automation system.

The system processes **demo call transcripts** and **onboarding call transcripts** to automatically generate and update an AI voice agent configuration.

The pipeline performs the following:

* Extract company information from demo call transcripts
* Generate a preliminary AI agent configuration (v1)
* Process onboarding updates
* Update the agent configuration (v2)
* Generate a changelog of modifications
* Store structured outputs

---

# Project Structure

```
clara_agent_project/

dataset/
    demo_calls/
        demo_1.txt
        demo_2.txt

    onboarding_calls/
        onboard_1.txt
        onboard_2.txt

outputs/
    accounts/

scripts/
    extract_demo.py
    generate_agent.py
    update_onboarding.py

run_pipeline.py
README.md
```

---

# Environment Setup

This project uses a Python virtual environment.

Activate the virtual environment before running the pipeline.

### Activate Virtual Environment

Run the following command in PowerShell:

```
& C:/Users/Lenovo/.virtualenvs/DocuQuery-main-V_M28mqC/Scripts/Activate.ps1
```

After activation, the environment will be ready to execute the project scripts.

---

# Run the Pipeline

Once the virtual environment is activated, run the pipeline using:

```
python c:/Users/Lenovo/Desktop/clara_agent_project/run_pipeline.py
```

The script will:

1. Read demo call transcripts
2. Extract structured data
3. Generate **Agent Version v1**
4. Process onboarding transcripts
5. Update the configuration to **Agent Version v2**
6. Create a changelog for modifications

---

# Output

After execution, the system will create structured outputs inside the `outputs` folder.

Example:

```
outputs/

accounts/

ABC_Fire_Protection/

v1/
    memo.json
    agent.json

v2/
    memo.json
    agent.json

changelog.txt
```

---

# How the Pipeline Works

### Step 1 — Demo Call Processing

The system reads demo call transcripts and extracts company information such as:

* Company name
* Address
* Business hours
* Services offered
* Emergency definitions
* Routing rules

This information is stored as an **Account Memo JSON**.

---

### Step 2 — Agent Draft Generation

Using the extracted information, the system generates a **Retell Agent Draft Specification (v1)**.

The draft includes:

* Agent name
* Voice style
* System prompt
* Business hour routing logic
* After-hours emergency handling

---

### Step 3 — Onboarding Update

When onboarding transcripts are processed, the system:

* Updates routing rules
* Applies configuration changes
* Generates **Agent Version v2**

---

### Step 4 — Change Tracking

All changes between v1 and v2 are recorded in a **changelog file**.

Example:

```
Emergency routing changed from technician to phone tree
```

---

# Requirements

* Python 3.9+
* VS Code (recommended)

No external APIs or paid services are required.

The pipeline runs entirely locally using Python.

---

# Notes

This project demonstrates:

* Automation pipeline design
* Structured data extraction
* AI agent configuration generation
* Version-controlled updates

The system is designed to be **repeatable, reproducible, and zero-cost**.
