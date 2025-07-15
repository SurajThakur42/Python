import os

# Specify the directory path
path = '/python'

try:
    # Get the list of entries in the specified directory
    entries = os.listdir(path)

    # Print each entry
    for entry in entries:
        print(entry)

except FileNotFoundError:
    print(f"Error: The directory '{path}' does not exist.")
except PermissionError:
    print(f"Error: Permission denied to access the directory '{path}'.")
except OSError as e:
    print(f"Error: {e}")
