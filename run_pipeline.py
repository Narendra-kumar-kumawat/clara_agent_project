import os
import json

from scripts.extract_demo import extract_demo_data
from scripts.generate_agent import generate_agent
from scripts.update_onboarding import update_account

demo_folder="dataset/demo_calls"
onboard_folder="dataset/onboarding_calls"
output_folder="outputs/accounts"

os.makedirs(output_folder,exist_ok=True)

for demo_file in os.listdir(demo_folder):

    demo_path=os.path.join(demo_folder,demo_file)

    memo=extract_demo_data(demo_path)

    account_id=memo["account_id"]

    account_folder=os.path.join(output_folder,account_id)

    v1_folder=os.path.join(account_folder,"v1")
    v2_folder=os.path.join(account_folder,"v2")

    os.makedirs(v1_folder,exist_ok=True)
    os.makedirs(v2_folder,exist_ok=True)

    # ----- v1 -----

    agent_v1=generate_agent(memo,"v1")

    with open(os.path.join(v1_folder,"memo.json"),"w") as f:
        json.dump(memo,f,indent=4)

    with open(os.path.join(v1_folder,"agent.json"),"w") as f:
        json.dump(agent_v1,f,indent=4)

    # ----- onboarding -----

    demo_num=demo_file.split("_")[1].split(".")[0]
    onboard_file=f"onboard_{demo_num}.txt"

    onboard_path=os.path.join(onboard_folder,onboard_file)

    if os.path.exists(onboard_path):

        updated_data,changes=update_account(memo,onboard_path)

        agent_v2=generate_agent(updated_data,"v2")

        with open(os.path.join(v2_folder,"memo.json"),"w") as f:
            json.dump(updated_data,f,indent=4)

        with open(os.path.join(v2_folder,"agent.json"),"w") as f:
            json.dump(agent_v2,f,indent=4)

        changelog_path=os.path.join(account_folder,"changelog.txt")

        with open(changelog_path,"w") as f:
            for c in changes:
                f.write(c+"\n")

print("Assignment pipeline completed successfully.")