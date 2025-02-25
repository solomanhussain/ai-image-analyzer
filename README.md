# Folder Organizer

A simple Streamlit application that organizes files in a folder by creating date-based subfolders and moving files into them based on their modification dates.

## Features

- Simple and intuitive web interface
- Real-time progress updates
- Handles file name conflicts automatically
- Works with any folder path

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/folder-organizer.git
cd folder-organizer
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
.\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Enter the folder path you want to organize (default is your Downloads folder)
3. Click "Organize Files" to start the organization process
4. Watch the real-time progress as files are organized

## How it Works

- Creates subfolders named with the format "YYYY-MM-DD" based on file modification dates
- Moves each file to its corresponding date folder
- Handles naming conflicts by appending numbers to filenames
- Shows real-time progress and results in the web interface