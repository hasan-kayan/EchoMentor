# file_search.py

import os

def search_files(root_folder, extension, output_file="found_files.txt"):
    if not extension.startswith('.'):
        raise ValueError("Invalid extension. Please include the dot (.) at the beginning.")

    with open(output_file, 'w') as file_out:
        for root, dirs, files in os.walk(root_folder):
            for file in files:
                if file.lower().endswith(extension):
                    file_path = os.path.join(root, file)
                    file_out.write(file_path + '\n')
                    print(f"Found: {file_path}")

    print(f"Search completed. Paths of all found files are saved in {output_file}.")
