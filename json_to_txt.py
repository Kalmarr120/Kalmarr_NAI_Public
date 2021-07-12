# This tool will convert .json files in same folder to .txt
# Made specifically for novelai research tool
# Advised that you create folder to place json outputs: likely will not work in main test folder

import json
import os

dl = os.listdir()
print(dl)

for f in dl:
    name = f
    a = 1
    if f.endswith(".json"):
    # if f.path.endswith(".json"):
        with open(f) as file:
            data = json.load(file)
        prompt = data[0]['prompt']
        txt_file = open(f"{name}.txt","w")
        txt_file.write(
        f"Export of {name}\n\n"
        f"Prompt:\n{prompt}\n\n"
        )
        for i in data:
            n = txt_file.write(
            f"\n==========\n\n"
            f"Iteration {a}\n\n"
            # f"Prompt: {prompt}\n\n"
            # f"Model: {i['settings']['model'] | }
            f"Prefix: {i['settings']['prefix']} | "
            f"Temperature: {i['settings']['temperature']}"
            f"\nTop-K: {i['settings']['top_k']} | "
            f"Top-P: {i['settings']['top_p']} | "
            f"TFS: {i['settings']['tail_free_sampling']}"
            f"\nRep Pen: {i['settings']['repetition_penalty']} | "
            f"Rep Range: {i['settings']['repetition_penalty_range']} | "
            f"Rep Slope: {i['settings']['repetition_penalty_slope']}\n\n"
            f"Results:\n\n"
            f"{i['result']}\n"
            )
            a = a + 1
        txt_file.close()
        if n > 0:
            print(f"File successfully written: {name}.txt.")
        else:
            print("Error writing file.")

path = os.getcwd()
for file in os.listdir():
    if file.endswith('.txt'):
        os.rename(os.path.join(path, file), os.path.join(path, file.replace(".json","")))
