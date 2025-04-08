def read_and_modify_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            content = infile.readlines()

        # Modify content (example: make all lines uppercase)
        modified_content = [line.upper() for line in content]

        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)

        print(f"✅ File has been read from '{input_filename}' and written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"❌ Error: You do not have permission to read '{input_filename}'.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# 🧪 Ask user for filename
user_file = input("Enter the name of the file to read: ")
read_and_modify_file(user_file, "modified_output.txt")
