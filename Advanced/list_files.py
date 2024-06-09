import os

folders = input("Enter the list of folders with spaces in between: ").split()

for folder in folders:

    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Looks like the program does not exist")
        continue
    except PermissionError:
        print("No access to this folder: " + folder)

    print("=== listing files for the folder :- " + folder)

    for file in files:
        print(file)