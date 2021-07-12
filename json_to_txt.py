# This tool will convert .json files in same folder to .txt
# Made specifically for novelai research tool
# Advised that you create folder to place json outputs: likely will not work in main test folder

import json
import os

# Prepare list of files in directory to convert
directory_list = os.listdir()
print(directory_list)

# Loop running through each file in directory
for files in directory_list:
    file_name = files
    # For in-text deliniation of iteration
    iteration_count = 1
    # Load JSON-specific files to python dictionary
    if files.endswith(".json"):
        with open(files) as file:
            data = json.load(file)
        # Variable for prompt to be pasted once in txt file
        prompt = data[0]['prompt']
        # Create txt file, "w" to rewrite any txt files of same name
        txt_file = open(f"{file_name}.txt","w")
        txt_file.write(
        f"Export of {file_name}\n\n"
        f"Prompt:\n{prompt}\n\n"
        )
        # Append each JSON object from file into txt format
        # Comment out any undesired categories
        for jsonitem in data:
            # count will count number of characters written
            count = txt_file.write(
            f"\n==========\n\n"
            f"Iteration {iteration_count}\n\n"
            # f"Prompt: {prompt}\n\n"
            # f"Model: {jsonitem['settings']['model'] | }
            f"Prefix: {jsonitem['settings']['prefix']} | "
            f"Temperature: {jsonitem['settings']['temperature']}"
            f"\nTop-K: {jsonitem['settings']['top_k']} | "
            f"Top-P: {jsonitem['settings']['top_p']} | "
            f"TFS: {jsonitem['settings']['tail_free_sampling']}"
            f"\nRep Pen: {jsonitem['settings']['repetition_penalty']} | "
            f"Rep Range: {jsonitem['settings']['repetition_penalty_range']} | "
            f"Rep Slope: {jsonitem['settings']['repetition_penalty_slope']}\n\n"
            f"Results:\n\n"
            f"{jsonitem['result']}\n"
            )
            iteration_count = iteration_count + 1
        txt_file.close()
        # Script should write more than 0 characters onto txt file
        if count > 0:
            print(f"File successfully written: {file_name}.txt.")
        else:
            print("Error writing file.")

# Rename files to remove '.json'
path = os.getcwd()
for file in os.listdir():
    if file.endswith('.txt'):
        os.rename(os.path.join(path, file), os.path.join(path, file.replace(".json","")))

# If on UNIX system, use `cat *.txt > name.txt` to combine files together.
