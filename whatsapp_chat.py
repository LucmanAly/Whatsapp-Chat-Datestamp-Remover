file_path = 'C:/Users/….....'

# Open the original file for reading
with open(file_path, 'r', encoding='utf-8') as f:
    # Read the file line by line
    lines = f.readlines()

# Open the new file for writing
file = 'C:/Users/...…….'
with open(file, 'w', encoding='utf-8') as f:
    # Loop through the lines
    for line in lines:
        # Check if the line starts with the date and time stamp
        if line.startswith('['):
            # Split the line at the first occurrence of '] '
            line = line.split('] ')[1]
        # Write the modified line to the new file
        f.write(line)