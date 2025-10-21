import os

def rename_files_in_folder(folder_path, prefix="file"):
    """
    Renames all files in the specified folder using a pattern like:
    file_1.txt, file_2.txt, etc.

    :param folder_path: Path to the folder containing files
    :param prefix: Prefix for renamed files (default is 'file')
    """

    # Change current working directory to the target folder
    os.chdir(folder_path)

    # Get all file names in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Sort files to rename them in order
    files.sort()

    # Loop through each file and rename it
    for index, filename in enumerate(files, start=1):
        # Extract file extension
        ext = os.path.splitext(filename)[1]
        # Create new file name
        new_name = f"{prefix}_{index}{ext}"
        # Rename the file
        os.rename(filename, new_name)
        print(f"Renamed: {filename} ➜ {new_name}")

    print("\n✅ All files renamed successfully!")


# Example usage
if __name__ == "__main__":
    folder_path = input("Enter the folder path: ").strip()
    rename_files_in_folder(folder_path)
