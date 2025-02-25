"""
Streamlit interface for organizing downloads by date.
"""
import os
import shutil
from datetime import datetime
from pathlib import Path

import streamlit as st

def organize_folder(folder_path: str, placeholder) -> None:
    """Organize files in a folder by date."""
    folder_path = Path(folder_path).expanduser()
    if not folder_path.exists():
        st.error(f"Folder does not exist: {folder_path}")
        return

    total_files = len([f for f in folder_path.iterdir() if f.is_file()])
    processed = 0

    for item in folder_path.iterdir():
        if item.is_file():
            # Get the file's modification time
            mod_time = item.stat().st_mtime
            date_folder = datetime.fromtimestamp(mod_time).strftime("%Y-%m-%d")
            
            # Create the target folder
            target_folder = folder_path / date_folder
            target_folder.mkdir(exist_ok=True)
            
            # Prepare destination path
            destination = target_folder / item.name
            
            # Handle file name conflicts
            counter = 1
            original_stem = destination.stem
            while destination.exists():
                destination = target_folder / f"{original_stem}_{counter}{destination.suffix}"
                counter += 1
            
            # Move the file
            try:
                shutil.move(str(item), str(destination))
                processed += 1
                placeholder.text(f"Processed {processed}/{total_files} files - Moved '{item.name}' to '{date_folder}'")
            except Exception as e:
                placeholder.error(f"Error moving '{item.name}': {str(e)}")

    if processed > 0:
        placeholder.success(f"✅ Successfully organized {processed} files into date folders")
    else:
        placeholder.info("No files to organize")

def main():
    st.set_page_config(
        page_title="Folder Organizer",
        page_icon="📁",
        layout="centered"
    )

    st.title("📁 Folder Organizer")
    st.markdown("""
    This tool organizes files in a folder by creating subfolders for each date
    and moving files into them based on their modification date.
    """)

    # Folder path input
    folder_path = st.text_input(
        "Folder Path",
        value=str(Path.home() / "Downloads"),
        help="Enter the path to the folder you want to organize"
    )

    # Progress placeholder
    progress_placeholder = st.empty()

    # Organize button
    if st.button("Organize Files", type="primary"):
        if folder_path:
            organize_folder(folder_path, progress_placeholder)
        else:
            st.error("Please enter a folder path")

if __name__ == "__main__":
    main()