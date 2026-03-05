def generate_agent(account_data, version):

    prompt=f"""
You are Clara, an AI receptionist for {account_data['company_name']}.

BUSINESS HOURS: {account_data['business_hours']}

OFFICE ADDRESS: {account_data['office_address']}

SERVICES:
{", ".join(account_data['services_supported'])}

OFFICE HOURS FLOW:
1 greet caller
2 ask purpose of call
3 collect caller name and phone number
4 transfer call based on routing rules
5 if transfer fails apologize and notify dispatch
6 ask if they need anything else
7 close call

AFTER HOURS FLOW:
1 greet caller
2 ask purpose
3 confirm if emergency
4 if emergency collect name phone and address immediately
5 attempt transfer
6 if transfer fails apologize and assure follow-up
7 if non emergency collect details for next business day
8 ask if they need anything else
9 close call
"""

    agent = {

        "agent_name": account_data["account_id"]+"_agent",

        "version": version,

        "voice_style": "professional",

        "variables":{

            "timezone":"America/Chicago",
            "business_hours":account_data["business_hours"],
            "office_address":account_data["office_address"]

        },

        "call_transfer_protocol":account_data["emergency_routing_rules"],

        "fallback_protocol":"If transfer fails apologize and notify dispatch",

        "system_prompt":prompt
    }

    return agent