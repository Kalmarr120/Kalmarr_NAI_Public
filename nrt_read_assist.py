# Import JSON
import json
import textwrap

# Ask for file name and convert JSON to dict
input1 = input(f"Input the name of your JSON file (e.g. test) >>>: ")
with open(f"{input1}.json") as file:
    data = json.load(file)

# Print data for reading in Python
# Variable for prompt for convenience
prompt = data[0]['prompt']
# Variable for iteration number
a = 1
print(
    f"\n=== Python Reader for NAI Research Tool ===\n"
    f"\nPrompt:\n{prompt}"
    )
for i in data:
    print(
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
        f"Rep Slope: {i['settings']['repetition_penalty_slope']}"
        f"\n")
    print(textwrap.fill(f"Results: {i['result']}"))
    a = a + 1
print("\n")

# Export to txt file if wanted
while True:
    export_txt = input(f"Would you like to export to a .txt file? [Y/N] >>: ")
    if export_txt.lower() == "y":
        # Will be overwritten with every run, comment out to add
        txt_file = open(f"{input1}.txt","w")
        # Remove comment to add to existing file
        # txt_file = open(f"{input}.txt","a")
        txt_file.write(
            f"Export of {input1}.json\n\n"
            f"Prompt:\n{prompt}\n\n"
            )
        # txt_file.close()
        a = 1
        txt_file = open(f"{input1}.txt","a")
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
            f"Results: {i['result']}\n"
            )
            a = a + 1
        txt_file.close()
        if n > 0:
            print("File successfully written.")
        else:
            print("Error writing file.")
        exit()
    else:
        break