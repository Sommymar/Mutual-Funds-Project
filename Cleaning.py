import os
import re

# Function to clean the content of a file
def clean_file_content(content):
    # Remove HTML tags using regular expressions
    cleaned_content = re.sub(r'<[^>]+>', '', content)
    # Replace &nbsp; with a space
    cleaned_content = cleaned_content.replace('&nbsp;', ' ')
    # Optionally, remove excessive whitespace
    cleaned_content = re.sub(r'\s+', ' ', cleaned_content).strip()
    return cleaned_content

# Function to replicate the directory structure and clean the files
def clean_html_folder(input_folder, output_folder):
    # Traverse the directory structure
    for root, dirs, files in os.walk(input_folder):
        # Get the corresponding output path by replacing input folder path with output folder path
        output_root = root.replace(input_folder, output_folder)
        
        # Create directories in the output folder if they don't exist
        if not os.path.exists(output_root):
            os.makedirs(output_root)

        # Process each file in the directory
        for file in files:
            if file.endswith('.txt'):
                input_file_path = os.path.join(root, file)
                output_file_path = os.path.join(output_root, file.replace('.txt', '_cleaned.txt'))

                # Read the content of the input file
                with open(input_file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Clean the content
                cleaned_content = clean_file_content(content)

                # Save the cleaned content to the output file
                with open(output_file_path, 'w', encoding='utf-8') as f:
                    f.write(cleaned_content)

                print(f"Cleaned file saved as '{output_file_path}'")

if __name__ == "__main__":
    # Define the input and output folder paths
    input_folder = r"C:\Users\chiso\OneDrive\Documents\McMaster Research Coop Summer 2024\Extraction\html"
    output_folder = r"C:\Users\chiso\OneDrive\Documents\McMaster Research Coop Summer 2024\Extraction\html_cleaned"

    # Clean all files in the folder and replicate the directory structure
    clean_html_folder(input_folder, output_folder)