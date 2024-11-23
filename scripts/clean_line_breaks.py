import os

def clean_line_breaks(file_path):
    try:
        # Read the file content
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Replace multiple line breaks (3 or more) with double line break
        while '\n\n\n' in content:
            content = content.replace('\n\n\n', '\n\n')
        
        # Write the cleaned content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
            
        return True
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return False

def process_directory(directory):
    cleaned_files = 0
    failed_files = 0
    
    # Walk through all directories and files
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Process only text/markdown files
            if file.endswith(('.md', '.txt')):
                file_path = os.path.join(root, file)
                print(f"Processing: {file_path}")
                
                if clean_line_breaks(file_path):
                    cleaned_files += 1
                else:
                    failed_files += 1
    
    return cleaned_files, failed_files

if __name__ == "__main__":
    # Start from the project root directory
    project_root = "."
    
    print("Starting cleanup of excessive line breaks...")
    cleaned, failed = process_directory(project_root)
    
    print("\nCleanup completed!")
    print(f"Successfully cleaned: {cleaned} files")
    print(f"Failed to clean: {failed} files")
