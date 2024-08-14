# file_search.py

import os

def search_files(root_folder, extension, output_file="found_files.txt"):
    """
    Search for files with a specific extension in a given root folder and save their paths in an output file.

    Args:
        root_folder (str): The root folder to start the search from.
        extension (str): The file extension to search for. Must include the dot (.) at the beginning.
        output_file (str, optional): The name of the output file to save the paths of found files. Defaults to "found_files.txt".

    Raises:
        ValueError: If the extension does not start with a dot (.) character.

    Returns:
        None
    """
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
