# Import the os and shutil modules
import os
import shutil

# Define a dictionary with the folder names and file extensions
listOfDirectories = {
    "Picture_Folder": [".jpeg", ".jpg", ".gif", ".png"],
    "Video_Folder": [".wmv", ".mov", ".mp4",".mpg", ".mpeg", ".mkv"],
    "Zip_Folder": [".iso", ".tar", ".gz", ".rz", ".7z",".dmg", ".rar", ".zip"],
    "Music_Folder": [".mp3", ".msv",".wav", ".wma"],
    "PDF_Folder": [".pdf"],
}

# Loop through the dictionary keys
for key in listOfDirectories:
    # Create a folder for each key
    if not os.path.exists(key):
        os.makedirs(key)

# Loop through the files in the current directory
for file in os.listdir():
    # Get the file extension
    src = file
    ext = src.split(".")[-1]

    # Loop through the dictionary items
    for folder, extensions in listOfDirectories.items():
        # If the file extension matches the dictionary value, move the file to the corresponding folder
        if "." + ext in extensions:
            dest = os.path.join(folder, src)
            shutil.move(src, dest)
            break
        