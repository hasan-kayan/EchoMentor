import os

# Get file extension from the user
file_extension = input("Enter the file extension (e.g., .txt, .jpg): ").strip().lower()

# Validate the file extension input
if not file_extension.startswith('.'):
    print("Invalid extension. Please include the dot (.) at the beginning.")
    exit()

# Define the output text file
output_file = "found_files.txt"

# Function to search and collect file paths
def search_files(root_folder, extension):
    with open(output_file, 'w') as file_out:
        for root, dirs, files in os.walk(root_folder):
            for file in files:
                if file.lower().endswith(extension):
                    file_path = os.path.join(root, file)
                    file_out.write(file_path + '\n')
                    print(f"Found: {file_path}")

# Get the root directory for searching files
root_directory = os.path.expanduser("~")  # Starts from the user's home directory

# Run the function to search files and save paths
search_files(root_directory, file_extension)

print(f"Search completed. Paths of all found files are saved in {output_file}.")
