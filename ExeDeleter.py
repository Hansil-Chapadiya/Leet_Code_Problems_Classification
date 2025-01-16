import os

# Define the folder path where the files are located
folder_path = r"E:\LeetCode_Problems"

# Iterate through all files in the folder
for file_name in os.listdir(folder_path):
    # Check if the file ends with ".exe"
    if file_name.endswith(".exe"):
        # Construct full file path
        file_path = os.path.join(folder_path, file_name)
        try:
            # Remove the .exe file
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Failed to delete {file_path}: {e}")

print("All .exe files have been processed.")
