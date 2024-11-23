#!/usr/bin/env python3
import os
import re

def clean_file(filepath):
    """
    Clean up excessive line breaks and trailing whitespace in a text file.
    
    Args:
        filepath (str): Path to the file to be cleaned
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Replace multiple consecutive line breaks with a maximum of 2
        cleaned_content = re.sub(r'\n{3,}', '\n\n', content)
        
        # Remove trailing whitespace
        cleaned_content = re.sub(r'\s+$', '', cleaned_content, flags=re.MULTILINE)
        
        # Write back to the file
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(cleaned_content)
        
        return True
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def process_directory(directory):
    """
    Process all text files in a directory and its subdirectories.
    
    Args:
        directory (str): Root directory to start processing
    """
    cleaned_files = 0
    failed_files = 0
    
    # File extensions to process
    text_extensions = ['.md', '.txt', '.json', '.yaml', '.yml']
    
    for root, _, files in os.walk(directory):
        for file in files:
            # Check if file has a text extension
            if any(file.lower().endswith(ext) for ext in text_extensions):
                filepath = os.path.join(root, file)
                print(f"Processing: {filepath}")
                
                if clean_file(filepath):
                    cleaned_files += 1
                else:
                    failed_files += 1
    
    return cleaned_files, failed_files

if __name__ == "__main__":
    project_root = "."
    
    print("Starting cleanup of excessive line breaks...")
    cleaned, failed = process_directory(project_root)
    
    print("\nCleanup completed!")
    print(f"Successfully cleaned: {cleaned} files")
    print(f"Failed to clean: {failed} files")
