# This tool will convert .json files in same folder to .txt
# Made specifically for novelai research tool
# Advised that you create folder to place json outputs: likely will not work in main test folder

import json
import os
import shutil

debug_mode = False
# if a file cannot be read in debug_mode = True will give out the error message and end the script

# Prepare list of files in directory to convert
directory_list = os.listdir()
print("Directory List:\n{}".format(directory_list))

if not os.path.exists("txt files"):
    os.mkdir("txt files")

# Loop running through each file in directory
for files in directory_list:
    file_name = files
    # For in-text deliniation of iteration
    iteration_count = 1
    # Load JSON-specific files to python dictionary
    if files.endswith(".json"):
        with open(files) as file:
            # incomplete or corrupted JSONs will give you an error and crash the whole script
            # checking if loading file works otherwise skipping file
            file_read = False
            try:
                data = json.load(file)
            except Exception as error:
                if debug_mode == True:
                    print("\nERROR WHILE READING IN FILE! The error message is given below.\n"
                          "To just skip corrupted files set debug_mode in the script to False.\n"
                          "Error occured while reading in file: {}\n".format(files))
                    print(repr(error))
                    quit()
                else:
                    print("\nERROR READING FILE - skipping: {}\n".format(files))
                    file_read = False
            else:
                file_read = True

        if file_read == True:  # skip processing if file was corrupt
            # Variable for prompt to be pasted once in txt file
            prompt = data[0]['prompt']
            # Create txt file, "w" to rewrite any txt files of same name
            txt_file_name = file_name.replace(".json", ".txt")
            print(f"Processing: {file_name}")
            txt_file = open(f"txt files/{txt_file_name}", "w")
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
                print(f"File successfully written: {txt_file_name}")
            else:
                print("Error writing file.")

print("\nAll files processed and saved as txt files in /txt files.\n")

while True:
    try:
        user_input = input(
            "Do you want to combine all these files into one single txt file? (y/n): ")
        if user_input.lower() == "y" or user_input.lower() == "yes":
            combine = True
            print("Okay - now combining all output files into a single txt-file.")
            break
        elif user_input.lower() == "n" or user_input.lower() == "no":
            combine = False
            print("Okay - exiting script.")
            quit()
        else:
            raise ValueError  # this will send it to the print message and back to the input option
        break
    except ValueError:
        print("Please enter 'y' or 'n'!")

if combine:
    combined_file = "txt files/ALL.txt"
    with open(combined_file, 'wb') as outfile:
        for infile in os.listdir("txt files"):
            infile_path = os.path.join("txt files", infile)
            if (infile_path != combined_file) and (infile_path.endswith(".txt")):
                # don't want to copy the output into the output also only want txt files
                with open(infile_path, 'rb') as readfile:
                    shutil.copyfileobj(readfile, outfile)
    print("DONE! Find the combined file under /txt files/ALL.txt")
