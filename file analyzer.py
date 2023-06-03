import os
import matplotlib.pyplot as plt

def analyze_file_system(root_directory):
    file_count = 0
    total_size = 0

    # Traverse the directory structure
    for dirpath, dirnames, filenames in os.walk(root_directory):
        print(f"Directory: {dirpath}")

        # Analyze files in the current directory
        for filename in filenames:
            file_count += 1
            file_path = os.path.join(dirpath, filename)
            file_size = os.path.getsize(file_path)
            total_size += file_size

            # Extract file information
            file_info = {
                "Name": filename,
                "Size": file_size,
                "Path": file_path,
                # Add more attributes as needed (e.g., file type, creation/modification dates)
            }
            print(f"File: {filename} | Size: {file_size} bytes")

    print(f"Total files: {file_count}")
    print(f"Total size: {total_size} bytes")

    # Create a pie chart of file types
    file_types = {}
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            _, file_extension = os.path.splitext(filename)
            file_types[file_extension] = file_types.get(file_extension, 0) + 1

    labels = list(file_types.keys())
    sizes = list(file_types.values())

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Distribution of File Types')
    plt.show()

# Usage example
root_directory = r"C:\Users\uernb\Desktop"
analyze_file_system(root_directory)
