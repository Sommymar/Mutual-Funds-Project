import os
import re

# Function to extract text block for shareholders, starting with 'Dear' and ending with "Sincerely" or a date if "Sincerely" isn't found
def extract_shareholders_letter(content):
    # Step 1: Create a pattern that starts with variations of "Dear" and ends with "Sincerely" or a date
    sincerely_pattern = re.compile(
        r'(Dear\s+Fellow\s+Shareholders|dear\s+fellow\s+shareholders|Dear\s+Shareholders|dear\s+shareholders|Dear\s+Fellow\s+shareholders|dear\s+Fellow\s+shareholders).*?'
        r'(Sincerely|sincerely)', 
        re.DOTALL | re.IGNORECASE
    )

    date_pattern = re.compile(
        r'(Dear\s+Fellow\s+Shareholders|dear\s+fellow\s+shareholders|Dear\s+Shareholders|dear\s+shareholders|Dear\s+Fellow\s+shareholders|dear\s+Fellow\s+shareholders).*?'
        r'([A-Z][a-z]+\s+\d{1,2},\s+\d{4})', 
        re.DOTALL | re.IGNORECASE
    )

    # Step 2: Try to match with the sincerely pattern first
    match = sincerely_pattern.search(content)

    # Step 3: If no sincerely match is found, fall back to the date pattern
    if not match:
        match = date_pattern.search(content)

    # Step 4: If a match is found, return the block of text
    if match:
        extracted_text = match.group(0)  # Get the entire matching block
        return extracted_text
    else:
        return None

# Function to recursively process all files in the input folder
def process_folder(input_folder, output_folder):
    for root, dirs, files in os.walk(input_folder):
        # Create corresponding directories in the output folder if they don't exist
        output_root = root.replace(input_folder, output_folder)
        if not os.path.exists(output_root):
            os.makedirs(output_root)

        for file in files:
            if file.endswith('.txt'):
                input_file_path = os.path.join(root, file)
                output_file_path = os.path.join(output_root, file.replace('.txt', '_shareholders_extracted.txt'))

                # Read the content of the input file
                with open(input_file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Extract shareholders letter
                extracted_text = extract_shareholders_letter(content)

                if extracted_text:
                    # Save the extracted text to the output file
                    with open(output_file_path, 'w', encoding='utf-8') as output_file:
                        output_file.write(extracted_text)
                    print(f"Extracted letter saved as '{output_file_path}'")
                else:
                    print(f"No shareholder letter found in '{input_file_path}'")

# Main function to prompt for mode (A for shareholders, B for prospectus)
def main():
    # Ask the user for the mode
    mode = input("Press 'A' for shareholders or 'B' for prospectus: ")

    # Get the folder path input from user
    input_folder = input("Please enter the full path to the folder containing text files: ")
    
    # Define the output folder (it will replicate the input folder structure)
    output_folder = input_folder + "_extracted"

    if mode.upper() == 'A':
        # Process all files in the input folder
        process_folder(input_folder, output_folder)
    elif mode.upper() == 'B':
        print("Prospectus extraction has not been implemented yet.")
    else:
        print("Invalid input. Please press 'A' for shareholders or 'B' for prospectus.")

if __name__ == "__main__":
    main()