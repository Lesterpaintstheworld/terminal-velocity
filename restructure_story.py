import os
import shutil
import re

def create_directory(path):
    """Create directory if it doesn't exist"""
    if not os.path.exists(path):
        os.makedirs(path)

def parse_filename(filename):
    """Parse filename to extract act, chapter and scene numbers"""
    # Common patterns in filenames
    act_patterns = [
        r'act(\d+)',
        r'ch(\d+)', 
        r'chapter(\d+)',
    ]
    
    scene_pattern = r'(\d+)_(\d+)_(\d+)'  # For format like 02_003_scene
    simple_scene_pattern = r'(\d+)_(\d+)_'  # For format like 1_1_ubc
    
    # First try to find the act number
    act_num = None
    for pattern in act_patterns:
        match = re.search(pattern, filename.lower())
        if match:
            act_num = match.group(1)
            break
    
    # Try to extract chapter and scene numbers
    chapter_num = None
    scene_num = None
    
    # Try complex scene pattern first
    match = re.search(scene_pattern, filename)
    if match:
        chapter_num = match.group(2)
        scene_num = match.group(3)
    else:
        # Try simple scene pattern
        match = re.search(simple_scene_pattern, filename)
        if match:
            chapter_num = match.group(1)
            scene_num = match.group(2)
    
    return act_num, chapter_num, scene_num

def restructure_files(source_dir, target_dir):
    """Restructure files into act/chapter/scene hierarchy"""
    create_directory(target_dir)
    
    # Process each file in the source directory
    for root, dirs, files in os.walk(source_dir):
        for filename in files:
            if filename.endswith('.md'):
                source_path = os.path.join(root, filename)
                
                # Parse the filename
                act_num, chapter_num, scene_num = parse_filename(filename)
                
                # Determine target directory
                if act_num:
                    act_dir = os.path.join(target_dir, f'act{act_num}')
                    create_directory(act_dir)
                    
                    if chapter_num:
                        chapter_dir = os.path.join(act_dir, f'chapter{chapter_num}')
                        create_directory(chapter_dir)
                        
                        if scene_num:
                            scene_dir = os.path.join(chapter_dir, f'scene{scene_num}')
                            create_directory(scene_dir)
                            target_path = os.path.join(scene_dir, filename)
                        else:
                            target_path = os.path.join(chapter_dir, filename)
                    else:
                        target_path = os.path.join(act_dir, filename)
                else:
                    # Files without act numbers go in the root of target directory
                    target_path = os.path.join(target_dir, filename)
                
                # Copy the file
                shutil.copy2(source_path, target_path)
                print(f'Copied: {filename} -> {target_path}')

def main():
    source_dir = 'story'
    target_dir = 'story_restructured'
    
    print("Starting file restructuring...")
    restructure_files(source_dir, target_dir)
    print("\nFile restructuring complete!")
    print(f"Files have been organized in: {target_dir}")

if __name__ == "__main__":
    main()
