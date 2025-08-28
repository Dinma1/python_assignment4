#
# A program to read from one file, modify its content,
# and write the new content to a separate file,
# with robust error handling.
#

import os

def process_file_with_error_handling():
    """
    Guides the user through a file reading and writing process.
    Handles common file-related exceptions gracefully.
    """
    # 1. Ask the user for the name of the file they want to read.
    input_filename = input("Please enter the name of the file you want to read: ")

    # We will use a try-except block to handle potential errors.
    try:
        # 2. Open the input file in read mode ('r').
        # The 'with' statement ensures the file is automatically closed.
        with open(input_filename, 'r') as infile:
            original_content = infile.read()
            print(f"\nSuccessfully read the content from '{input_filename}':")
            print("---" * 10)
            print(original_content)
            print("---" * 10)

        # 3. Modify the content. For this challenge, we'll convert it to uppercase.
        modified_content = original_content.upper()
        print("\nContent has been modified (converted to uppercase).")

        # 4. Create a new filename for the output file.
        # This prevents overwriting the original.
        output_filename = f"modified_{input_filename}"

        # 5. Open the new file in write mode ('w') and write the modified content.
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        # 6. Success message.
        print(f"\nSuccess! The modified content has been saved to '{output_filename}'.")
        print("You can now find this new file in the same directory.")

    # 7. Error Handling: Catch specific exceptions.
    except FileNotFoundError:
        # This error occurs if the file specified by the user does not exist.
        print(f"\nError: The file '{input_filename}' was not found.")
        print("Please make sure the file exists and you have typed the correct name.")
    except PermissionError:
        # This error occurs if the program does not have the necessary permissions
        # to read the file.
        print(f"\nError: You do not have permission to access the file '{input_filename}'.")
        print("Please check your file permissions.")
    except Exception as e:
        # A general catch-all for any other unexpected errors that might occur.
        print(f"\nAn unexpected error occurred: {e}")

# This ensures the function runs only when the script is executed directly.
if __name__ == "__main__":
    process_file_with_error_handling()