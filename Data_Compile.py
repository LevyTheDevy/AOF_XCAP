

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

import pandas as pd

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
    else:
        print("Missing DATA")





