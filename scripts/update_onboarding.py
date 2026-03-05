def update_account(existing_data,onboarding_file):

    changes=[]

    with open(onboarding_file,"r") as f:
        lines=f.readlines()

    for line in lines:

        line=line.strip()

        if "phone tree" in line.lower():

            old=existing_data["emergency_routing_rules"]

            existing_data["emergency_routing_rules"]="transfer to phone tree"

            changes.append(f"Emergency routing updated: {old} -> phone tree")

        elif "dispatch manager" in line.lower():

            old=existing_data["emergency_routing_rules"]

            existing_data["emergency_routing_rules"]="transfer to dispatch manager"

            changes.append(f"Emergency routing updated: {old} -> dispatch manager")

    return existing_data,changes