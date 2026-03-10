"""
Asks the user for a filename, reads all lines from the file,
removes any leading or trailing whitespace from each line, and
prints the resulting list. If the file does not exist, an error message
is displayed
"""

filename = input("Enter the filename: ")

try:
    with open(filename, "r") as file:
        lines = file.readlines()

 # strip whitespace from each line
        stripped_lines = [line.strip() for line in lines]

        print("Resulting list: ")
        print(stripped_lines)

except FileNotFoundError:
    print("Error: The file does not exist")

