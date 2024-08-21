import os

def search_files(root_folder, extension):
    """
    Search for files with a specific extension in a given root folder.

    Args:
        root_folder (str): The root folder to start the search from.
        extension (str): The file extension to search for. Must include the dot (.) at the beginning.

    Raises:
        ValueError: If the extension does not start with a dot (.) character.

    Returns:
        list: A list of paths to the found files.
    """
    if not extension.startswith('.'):
        raise ValueError("Invalid extension. Please include the dot (.) at the beginning.")

    found_files = []
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.lower().endswith(extension):
                file_path = os.path.join(root, file)
                found_files.append(file_path)
                print(f"Found: {file_path}")

    print(f"Search completed. {len(found_files)} files found.")
    return found_files
