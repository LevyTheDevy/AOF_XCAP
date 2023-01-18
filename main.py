import json

# Open the input file for reading
with open('dump.txt', 'r') as f:
    # Read the entire file into a string
    text = f.read()

# Find the start and end indices of the description
start_index = text.index('<Content Start>') + len('<Content Start>')
end_index = text.index('<Content End>')

# Extract the description from the text
description = text[start_index:end_index]

# Open the output file for writing
with open('Content.txt', 'w') as f:
    # Write the description to the file
    f.write(description)

# Open the input file for reading
with open('dump.txt', 'r') as f:
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

# The array of strings to search for
strings_to_remove = ['Str', 'Int', 'Dbl', 'hexstr', 'tim']

# Open the input file for reading
with open("Description.txt", "r") as input_file:
    # Open the output file for writing
    with open("Description_Filtered.txt", "w") as output_file:
        # Read the lines of the input file
        lines = input_file.readlines()

        # Iterate through the lines
        for line in lines:
            # Check if the line contains any of the strings in the array
            if not any(s in line for s in strings_to_remove):
                # If not, write the line to the output file
                output_file.write(line)

# Close the output file
output_file.close()

# Read first file to create structure
with open("Description_Filtered.txt", "r") as structure_file:
    structure_lines = structure_file.readlines()

data = {}
for line in structure_lines:
    line_list = line.strip().split("|")
    parent = line_list[0]
    child = {}
    if len(line_list) > 1:
        for i in range(1, len(line_list)):
            child[line_list[i]] = []
    data[parent] = child

with open("Content.txt", "r") as data_file:
    data_lines = data_file.readlines()

for line in data_lines:
    line_list = line.strip().split("|")
    parent = line_list[0]
    if parent in data and len(line_list) > 1:
        for i in range(1, len(line_list)):
            if line_list[i] in data[parent]:
                data[parent][line_list[i]].append(line_list[i])
            else:
                print(f"{line_list[i]} is not a valid key in the {parent} structure.")

json_data = json.dumps(data, indent=4) # indent=4 adds white space for readability
print(json_data)




