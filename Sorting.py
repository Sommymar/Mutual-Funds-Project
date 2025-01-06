import os
from prettytable import PrettyTable

def find_files(base_path, mode):
    found_files = []
    
    if mode == 'A':
        folder_names = ['485', '497']
    elif mode == 'B':
        folder_names = ['N-CRS', 'N-CSRS']
    else:
        print("Invalid mode! Choose 'A' or 'B'.")
        return []

    try:
        for root, dirs, files in os.walk(base_path):
            for dir_name in dirs:
                if dir_name in folder_names:
                    folder_path = os.path.join(root, dir_name)
                    try:
                        for file in os.listdir(folder_path):
                            if file.endswith('.txt'):
                                found_files.append(os.path.join(folder_path, file))
                    except Exception as e:
                        print(f"Error accessing files in folder {folder_path}: {e}")
    except Exception as e:
        print(f"Error walking through directory {base_path}: {e}")

    return found_files

def display_files_in_table(mode, files):
    # Create a PrettyTable object
    table = PrettyTable()
    # Define the column names
    table.field_names = ["Mode", "File Path"]
    # Add rows for each file found
    for file in files:
        table.add_row([mode, file])
    # Print the table
    print(table)

if __name__ == "__main__":
    base_path = r"C:\Users\chiso\OneDrive\Documents\McMaster Research Coop Summer 2024\Extraction\html"  # Replace with the actual path to the "HTML" folder
    
    # Mode A Results
    files_a = find_files(base_path, 'A')
    print("Mode A Results:")
    display_files_in_table('A', files_a)
    
    # Add a separator for clarity
    print("\n" + "-"*40 + "\n")
    
    # Mode B Results
    files_b = find_files(base_path, 'B')
    print("Mode B Results:")
    display_files_in_table('B', files_b)