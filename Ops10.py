# Create a new .txt file
file_name = 'example.txt'
with open(file_name, 'w') as file:
    # Append three lines
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")
    file.write("This is the third line.\n")

# Read and print the first line
with open(file_name, 'r') as file:
    first_line = file.readline()
    print("First line:", first_line)

# Delete the .txt file
import os
os.remove(file_name)
print(f"{file_name} has been deleted.")
