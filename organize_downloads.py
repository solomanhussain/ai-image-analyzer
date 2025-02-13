#!/usr/bin/env python3
import os
import shutil
from datetime import datetime

def organize_downloads(downloads_folder):
    # Iterate over all items in the Downloads folder
    for item in os.listdir(downloads_folder):
        item_path = os.path.join(downloads_folder, item)
        
        # Process only files (skip directories)
        if os.path.isfile(item_path):
            # Get the file's modification time (you can also use creation time if desired)
            mod_time = os.path.getmtime(item_path)
            # Format the modification time as YYYY-MM-DD
            date_folder = datetime.fromtimestamp(mod_time).strftime("%Y-%m-%d")
            
            # Create the target folder path
            target_folder = os.path.join(downloads_folder, date_folder)
            # Create the folder if it doesn't already exist
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)
            
            # Construct the destination path and move the file
            destination = os.path.join(target_folder, item)
            print(f"Moving '{item}' to folder '{date_folder}'")
            shutil.move(item_path, destination)

if __name__ == "__main__":
    # Define the Downloads folder (default location on a Mac)
    downloads_dir = os.path.expanduser("~/Downloads")
    organize_downloads(downloads_dir)