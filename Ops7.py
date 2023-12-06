#!/usr/bin/env python3

# Import libraries
import os

# Declaration of functions
def generate_directories_and_files(user_path):
    """
    Generate all directories, sub-directories, and files for a given directory path.

    Parameters:
    user_path (str): The user-provided directory path.
    """
    for (root, dirs, files) in os.walk(user_path):
        # Add a print command here to print ==root==
        print(f"Root Directory: {root}")

        # Add a print command here to print ==dirs==
        print(f"Sub-Directories: {dirs}")

        # Add a print command here to print ==files==
        print(f"Files: {files}")

# Main
if __name__ == "__main__":
    # Declaration of variables
    user_input_path = input("Enter the directory path: ")

    # Pass the variable into the function here
    generate_directories_and_files(user_input_path)

# End

resource - chatgpt
