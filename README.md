Downloads Organizer

A simple Python script to automatically organize your Downloads folder into subfolders based on file types.

Features

- Sorts files into categories like:
  - Images
  - Videos
  - Documents
  - Music
  - Archives
  - Installers
  - Code files
  - Others
- Uses `pathlib` and `shutil` from the standard Python library
- Skips folders and processes only files

How It Works

The script scans your `Downloads` folder and moves each file into a subfolder based on its extension. If the file extension is not recognized, it will go to the `Others` folder.

Requirements

- Python 3.6 or higher (no external libraries needed)

Setup and Usage

1. Clone or download this repository.
2. Open the script in your code editor.
3. Run it using:


Customization
You can edit the tipos_arquivos dictionary inside the script to define new file types and folder names.
'Designs': ['.psd', '.ai', '.xd']

Warning
•	Files will be moved, not copied.
•	Be careful when testing—don't run it if you have important unsorted files you might lose track of.
•	The folder names are in Portuguese


