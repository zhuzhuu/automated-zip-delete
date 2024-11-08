import os
import time

# Define the path to your Downloads folder
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

# Get the current time
current_time = time.time()

# Define the time threshold (7 days in seconds)
time_threshold = 7 * 24 * 60 * 60  # 7 days

# Iterate through the files in the Downloads folder
for filename in os.listdir(downloads_folder):
    if filename.endswith('.zip'):
        file_path = os.path.join(downloads_folder, filename)
        # Get the last modified time of the file
        file_mod_time = os.path.getmtime(file_path)
        # Check if the file was modified in the last 7 days
        if current_time - file_mod_time < time_threshold:
            print(f"Deleting: {file_path}")  # Print the file being deleted
            os.remove(file_path)  # Delete the file

print("Deletion of .zip files completed.")
