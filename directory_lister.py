"""
Asks the user for a directory path and lists all files and directories.
Handles errors if the directory doesn't exist or is inaccessible.
"""

import os # required for directory operations

# Ask user for a directory path
directory_path = input("Enter a directory path: ")

try:
    # list all files and directories
    items = os.listdir(directory_path)

    # print the items in a nicely formatted way
    print(f"\nContents of '{directory_path}':")
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item}")

except FileNotFoundError:
 print(f"Error: The directory '{directory_path}' does not exist.")

except PermissionError:
 print(f"Error: Permission denied to access '{directory_path}'.")

except Exception as e:
# Catch-all for any other exceptions
 print(f"An unexpected error occured: {e}")

