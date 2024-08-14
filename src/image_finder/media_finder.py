# media_finder.py

import os
import shutil

# Define the common image and video file extensions
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
video_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.webm']

# Combine image and video extensions
media_extensions = image_extensions + video_extensions

def search_media_files(root_folder):
    """Search for media files and return their paths."""
    media_files = []
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.lower().endswith(tuple(media_extensions)):
                file_path = os.path.join(root, file)
                media_files.append(file_path)
    return media_files

def clone_media_files(media_files, destination_folder="Cloned_Media"):
    """Clone the media files to the destination folder."""
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

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
        print(f"Copied: {file_path} to {destination_path}")

    print(f"Cloning completed. All media files are copied to {destination_folder}.")
