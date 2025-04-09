def read_and_modify_file():
    # Ask the user for the filename
    filename = input("Enter the filename to read: ")

    try:
        # Try to open and read the file
        with open(filename, 'r') as file:
            content = file.read()

        # Modify the content (e.g., convert it to uppercase)
        modified_content = content.upper()

        # Create a new filename
        new_filename = f"modified_{filename}"

        # Write the modified content to the new file
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Modified content written to '{new_filename}'")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{filename}' could not be read or written.")

# Run the program
print(read_and_modify_file())
