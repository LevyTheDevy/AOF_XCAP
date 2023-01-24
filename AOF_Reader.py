import json
import os
import pandas as pd
import os
# Import the `defaultdict` function from the `collections` module
from collections import defaultdict

# Open the input file for reading
with open('AOF/VOICE.aof', 'r') as f:
    # Read the entire file into a string
    text = f.read()

# Find the start and end indices of the description
start_index = text.index('<Content Start>') + len('<Content Start>')
end_index = text.index('<Content End>')

# Extract the description from the text
description = text[start_index:end_index]

# Open the output file for writing
with open('Data.txt', 'w') as f:
    # Write the description to the file
    f.write(description)

# Open the input file for reading
with open('AOF/VOICE.aof', 'r') as f:
    # Read the entire file into a string
    text = f.read()

# Find the start and end indices of the description
start_index = text.index('<Description Start>') + len('<Description Start>')
end_index = text.index('<Description End>')

# Extract the description from the text
description = text[start_index:end_index]

# Open the output file for writing
with open('Description.txt', 'w') as f:
    # Write the description to the file
    f.write(description)

import re

# The array of strings to search for
remove_array = [] #['Str', 'Int', 'Dbl', 'hexstr', 'tim']

# Open the input file for reading
with open("Description.txt", "r") as input_file:
    # Open the output file for writing
    with open("Structure.txt", "w") as output_file:
        # Iterate through the lines
        for line in input_file:
            line = line.strip()
            # Initialize a flag to indicate if the line should be removed
            remove_line = False
            # Iterate through the strings to remove
            for remove_string in remove_array:
                # Use the re module to check for exact string matches
                if re.search(r"\b" + re.escape(remove_string) + r"\b", line):
                    remove_line = True
                    break
            if not remove_line:
                output_file.write(line + "\n")



os.remove("Description.txt")
# Close the output file
output_file.close()

# Open the Structure.txt file and read its contents into a variable
with open('Structure.txt', 'r') as structure_file:
    structure = structure_file.readlines()

# Open the Data.txt file and read its contents into a variable
with open('Data.txt', 'r') as data_file:
    data = data_file.readlines()

# Create a default dictionary to store the merged data
merged_data = defaultdict(list)

# Create a set to store the first strings from the Data.txt file
data_keys = set()

# Iterate over the lines in the Data.txt file
for line in data:
    # Split the line by the pipe character
    parts = line.strip().split('|')
    # Add the first string to the set
    data_keys.add(parts[0])

# Create a default dictionary to store the merged data
merged_data = defaultdict(list)

# Iterate over the lines in the Structure.txt file
for line in structure:
    # Split the line by the pipe character
    parts = line.strip().split('|')
    # Check if the first string exists in the Data.txt file
    if parts[0] in data_keys:
        # Add the line to the dictionary using the first string as the key
        merged_data[parts[0]].append(line)

# Iterate over the lines in the Data.txt file
for line in data:
    # Split the line by the pipe character
    parts = line.strip().split('|')
    # Add the line to the dictionary using the first string as the key
    merged_data[parts[0]].append(line)

# Open a new file to write the merged data
with open('MergedData.txt', 'w') as merged_file:
    # Iterate over the items in the dictionary
    for key, value in merged_data.items():
        # Write each item to the file
        for item in value:
            merged_file.write(item)

# Open the original .txt file for reading
with open('MergedData.txt', 'r') as original_file:
    # Read the lines from the file
    lines = original_file.readlines()

# Open a new file for writing
with open('MergedData_Cleaned.txt', 'w') as cleaned_file:
    # Iterate over the lines in the original file
    for line in lines:
        # Check if the line is not empty
        if line.strip():
            # Write the non-empty line to the new file
            cleaned_file.write(line)

os.remove("MergedData.txt")

DF_Array = []
for key, value in merged_data.items():
    # split the first line
    first_line = value[0].strip().split("|")
    columns = None
    # check if the number of elements in the first line is equal to the number of elements in the other lines
    for line in value[1:]:
        if len(first_line) == len(line.strip().split("|")):
            # Use the first line as the column names
            columns = first_line
            break
    if not columns:
        columns = [f"col{i}" for i in range(len(line.strip().split("|")))]
    # Create a DataFrame for each unique line
    df = pd.DataFrame([line.strip().split("|") for line in value], columns=columns)
    df = df.iloc[2:]
    DF_Array.append(df)
    if key != '':
        df.to_csv("DATA/" +str(key)+".csv")
        print(df.head())
    else:
        print("Missing DATA")

