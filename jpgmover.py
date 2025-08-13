import os
import shutil

source_folder = "C:\\Users\\Aayushmaan\\Desktop\\New folder (2)\\1"
destination_folder = "C:\\Users\\Aayushmaan\\Desktop\\New folder (2)\\2"

# Create destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Loop through files in the source folder
for filename in os.listdir(source_folder):
    if filename.lower().endswith(".jpg"):
        src_path = os.path.join(source_folder, filename)
        dst_path = os.path.join(destination_folder, filename)
        shutil.move(src_path, dst_path)
        print(f"Moved: {filename}")

print("All .jpg files have been moved.")
