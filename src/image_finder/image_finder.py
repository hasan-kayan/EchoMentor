import os
import shutil

# Define the folder to clone the photos and videos into
destination_folder = "Cloned_Media"

# Define the common image and video file extensions
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
video_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.webm']

# Combine image and video extensions
media_extensions = image_extensions + video_extensions

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Function to find and clone media files
def clone_media_files(root_folder):
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.lower().endswith(tuple(media_extensions)):
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_folder, file)
                
                # Ensure unique file names in the destination folder
                if os.path.exists(destination_path):
                    base, extension = os.path.splitext(file)
                    counter = 1
                    while os.path.exists(destination_path):
                        destination_path = os.path.join(destination_folder, f"{base}_{counter}{extension}")
                        counter += 1
                
                # Copy the file to the destination folder
                shutil.copy2(source_path, destination_path)
                print(f"Copied: {source_path} to {destination_path}")

# Get the root directory for searching media files
root_directory = os.path.expanduser("~")  # Starts from the user's home directory

# Run the function to clone media files
clone_media_files(root_directory)

print(f"Cloning completed. All media files are copied to {destination_folder}.")
