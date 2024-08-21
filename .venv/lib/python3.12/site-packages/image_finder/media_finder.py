import os
import shutil

# Define the common image and video file extensions
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
video_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.webm']

# Combine image and video extensions
media_extensions = image_extensions + video_extensions

def search_media_files(root_folder, specific_extension=None):
    """
    Search for media files in the given root folder and return their paths.

    Args:
        root_folder (str): The root folder to start the search from.
        specific_extension (str, optional): A specific file extension to search for. Must include the dot (.) at the beginning.
                                             If None, all media files will be returned.

    Returns:
        list: A list of paths to the found media files.

    """
    media_files = []
    if specific_extension and not specific_extension.startswith('.'):
        raise ValueError("Invalid extension. Please include the dot (.) at the beginning.")

    extensions_to_search = [specific_extension] if specific_extension else media_extensions

    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.lower().endswith(tuple(extensions_to_search)):
                file_path = os.path.join(root, file)
                media_files.append(file_path)

    print(f"Search completed. {len(media_files)} media files found.")
    return media_files

def collect_and_clone_media_files(root_folder, specific_extension=None, destination_folder="Collected_Media"):
    """
    Search for media files, collect them in a specific folder, and return the list of paths to the collected files.

    Args:
        root_folder (str): The root folder to start the search from.
        specific_extension (str, optional): A specific file extension to search for. Must include the dot (.) at the beginning.
                                             If None, all media files will be collected.
        destination_folder (str, optional): The destination folder where the files will be cloned.
                                            Defaults to "Collected_Media".

    Returns:
        list: A list of paths to the cloned media files.

    """
    # Search for media files based on the specific extension or all media files
    media_files = search_media_files(root_folder, specific_extension)

    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    collected_files = []
    for file_path in media_files:
        file = os.path.basename(file_path)
        destination_path = os.path.join(destination_folder, file)

        # Ensure unique file names in the destination folder
        if os.path.exists(destination_path):
            base, extension = os.path.splitext(file)
            counter = 1
            while os.path.exists(destination_path):
                destination_path = os.path.join(destination_folder, f"{base}_{counter}{extension}")
                counter += 1

        # Copy the file to the destination folder
        shutil.copy2(file_path, destination_path)
        collected_files.append(destination_path)
        print(f"Copied: {file_path} to {destination_path}")

    print(f"Cloning completed. All media files are copied to {destination_folder}.")
    return collected_files
