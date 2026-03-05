import json

def extract_demo_data(file_path):

    memo = {
        "account_id": "",
        "company_name": "",
        "business_hours": "",
        "office_address": "",
        "services_supported": [],
        "emergency_definition": [],
        "emergency_routing_rules": "",
        "non_emergency_routing_rules": "collect details and schedule follow-up",
        "call_transfer_rules": {
            "timeout": "60 seconds",
            "retry": "1",
            "fallback": "notify dispatch"
        },
        "integration_constraints": "",
        "after_hours_flow_summary": "",
        "office_hours_flow_summary": "",
        "questions_or_unknowns": [],
        "notes": ""
    }

    with open(file_path,"r") as f:
        lines=f.readlines()

    for line in lines:

        line=line.strip()

        if line.startswith("Company:"):
            memo["company_name"]=line.split(":")[1].strip()
            memo["account_id"]=memo["company_name"].replace(" ","_")

        elif line.startswith("Address:"):
            memo["office_address"]=line.split(":")[1].strip()

        elif line.startswith("Business Hours:"):
            memo["business_hours"]=line.split(":")[1].strip()

        elif line.startswith("Services:"):
            services=line.split(":")[1]
            memo["services_supported"]=[s.strip() for s in services.split(",")]

        elif "-" in line:
            memo["emergency_definition"].append(line.replace("-","").strip())

        elif "transfer" in line.lower():
            memo["emergency_routing_rules"]=line

        elif line.startswith("Notes"):
            memo["notes"]=line

    memo["office_hours_flow_summary"] = "greet caller, ask purpose, collect name and phone number, route call, fallback if transfer fails"

    memo["after_hours_flow_summary"] = "greet caller, confirm emergency, collect name phone address, attempt transfer, fallback and assure follow-up"

    return memo