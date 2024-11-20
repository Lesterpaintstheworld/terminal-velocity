import os
import shutil

def create_directory(path):
    """Create directory if it doesn't exist"""
    if not os.path.exists(path):
        os.makedirs(path)

def move_files(source_dir, target_dir):
    """Move files to their correct locations based on manual mapping"""
    
    # Create base directory
    create_directory(target_dir)

    # Manual mapping of files to their correct locations
    file_mapping = {
        # Act 1
        "scenes/act1/ch1/1_1_ubc_presentation.md": "act1/chapter1/scene1/",
        "scenes/act1/ch1/1_2_consciousness_discovery.md": "act1/chapter1/scene2/",
        "scenes/act1/ch1/1_3_isabella_reaction.md": "act1/chapter1/scene3/",
        
        "scenes/act1/ch2/2_1_vision_clash.md": "act1/chapter2/scene1/",
        "scenes/act1/ch2/2_2_strategic_doubts.md": "act1/chapter2/scene2/",
        "scenes/act1/ch2/2_3_first_clash.md": "act1/chapter2/scene3/",
        
        "scenes/act1/ch3/3_1_art_emergence.md": "act1/chapter3/scene1/",
        "scenes/act1/ch3/3_2_ubc_test.md": "act1/chapter3/scene2/",
        "scenes/act1/ch3/3_3_rights_discussion.md": "act1/chapter3/scene3/",
        
        "scenes/act1/ch4/4_1_security_assessment.md": "act1/chapter4/scene1/",
        "scenes/act1/ch4/4_2_alliance_formation.md": "act1/chapter4/scene2/",
        "scenes/act1/ch4/4_3_opposition_emerges.md": "act1/chapter4/scene3/",
        
        "scenes/act1/ch5/5_1_system_anomalies.md": "act1/chapter5/scene1/",
        "scenes/act1/ch5/5_2_institutional_response.md": "act1/chapter5/scene2/",
        "scenes/act1/ch5/5_3_cipher_confrontation.md": "act1/chapter5/scene3/",

        # Act level files
        "scenes/act1/act1_scenes.md": "act1/",
        "scenes/act1/act1_timeline.md": "act1/",
        "scenes/act2/act2_scenes.md": "act2/",
        "scenes/act2/act2_timeline.md": "act2/",
        "scenes/act3/act3_timeline.md": "act3/",
        "scenes/act4/act4_scenes.md": "act4/",
        "scenes/act4/act4_timeline.md": "act4/",

        # Structure files
        "structure/act_breakdowns/act1_foundation.md": "act1/",
        "structure/act_breakdowns/act2_rising.md": "act2/",
        "structure/act3_crisis.md": "act3/",
        "structure/act4_resolution.md": "act4/",
    }

    # Process each file mapping
    for source_path, target_subdir in file_mapping.items():
        full_source = os.path.join(source_dir, source_path)
        full_target_dir = os.path.join(target_dir, target_subdir)
        
        # Only process if source file exists
        if os.path.exists(full_source):
            # Create target directory
            create_directory(full_target_dir)
            
            # Get just the filename from the source path
            filename = os.path.basename(source_path)
            full_target = os.path.join(full_target_dir, filename)
            
            # Copy the file
            try:
                shutil.copy2(full_source, full_target)
                print(f'Copied: {source_path} -> {target_subdir}{filename}')
            except FileNotFoundError:
                print(f'Source file not found: {source_path}')
            except Exception as e:
                print(f'Error copying {source_path}: {str(e)}')

def main():
    source_dir = 'story'
    target_dir = 'story_restructured'
    
    print("Starting file restructuring...")
    move_files(source_dir, target_dir)
    print("\nFile restructuring complete!")
    print(f"Files have been organized in: {target_dir}")

if __name__ == "__main__":
    main()
