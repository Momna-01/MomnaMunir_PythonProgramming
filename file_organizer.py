import os
import shutil

def organize_files(directory):
    # Change the current working directory to the specified path
    os.chdir(directory)
    
    # Define mapping of extensions to folder names
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
        'Videos': ['.mp4', '.mkv', '.mov'],
    }

    # Scan files in the directory
    for file in os.listdir(directory):
        # Skip if it's a directory
        if os.path.isdir(file):
            continue
            
        # Get the file extension
        filename, extension = os.path.splitext(file)
        
        # Check which category the extension belongs to
        for folder, extensions in file_types.items():
            if extension.lower() in extensions:
                # Create the folder if it doesn't exist
                if not os.path.exists(folder):
                    os.makedirs(folder)
                
                # Move the file
                shutil.move(file, os.path.join(folder, file))
                print(f"Moved: {file} -> {folder}")

# Main execution
target_path = input("Enter the full path of the folder to organize: ")
if os.path.exists(target_path):
    organize_files(target_path)
    print("Organization complete!")
else:
    print("Invalid path. Please try again.")