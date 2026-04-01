import os
import shutil

def organize_files(folder_path):
    """
    Organizes files in the given folder into subfolders based on file extensions.
    """
    if not os.path.exists(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        return

    # Dictionary mapping file extensions to folder names
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
        "Audio": [".mp3", ".wav", ".aac"],
        "Videos": [".mp4", ".mov", ".avi", ".mkv"],
        "Archives": [".zip", ".rar", ".tar", ".gz"],
        "Scripts": [".py", ".js", ".sh", ".bat"]
    }

    # Create folders if they don't exist
    for folder in file_types.keys():
        os.makedirs(os.path.join(folder_path, folder), exist_ok=True)

    # Move files into respective folders
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        moved = False
        for folder, extensions in file_types.items():
            if ext in extensions:
                shutil.move(file_path, os.path.join(folder_path, folder, filename))
                moved = True
                break

        # If file type is unknown, move to "Others"
        if not moved:
            os.makedirs(os.path.join(folder_path, "Others"), exist_ok=True)
            shutil.move(file_path, os.path.join(folder_path, "Others", filename))

    print("✅ Files organized successfully!")

if __name__ == "__main__":
    # Example: Change this path to the folder you want to organize
    folder_to_organize = input("Enter the folder path to organize: ").strip()
    organize_files(folder_to_organize)
