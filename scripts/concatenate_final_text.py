import os
from pathlib import Path

def get_act_number(act_name):
    """Extract numeric value from act name (e.g., 'act1' -> 1)"""
    return int(act_name.replace('act', ''))

def get_chapter_number(chapter_name):
    """Extract numeric value from chapter name (e.g., 'chapter1' -> 1)"""
    return int(chapter_name.replace('chapter', ''))

def get_scene_number(scene_name):
    """Extract numeric value from scene name (e.g., 'scene1.md' -> 1)"""
    return int(scene_name.replace('scene', '').replace('.md', ''))

def concatenate_final_text(input_dir='final_text', output_file='complete_manuscript.md'):
    """
    Concatenate all markdown files from final_text directory into a single file,
    maintaining the proper order of acts, chapters, and scenes.
    """
    # Get the root directory
    root_dir = Path(input_dir)
    output_path = Path(output_file)
    
    # Dictionary to store all content
    full_content = []
    
    # Get all acts and sort them
    acts = sorted(
        [d for d in root_dir.iterdir() if d.is_dir()],
        key=lambda x: get_act_number(x.name)
    )
    
    # Process each act
    for act_dir in acts:
        full_content.append(f"\n\n# {act_dir.name.upper()}\n\n")
        
        # Get and sort chapters
        chapters = sorted(
            [d for d in act_dir.iterdir() if d.is_dir()],
            key=lambda x: get_chapter_number(x.name)
        )
        
        # Process each chapter
        for chapter_dir in chapters:
            full_content.append(f"\n## {chapter_dir.name.upper()}\n\n")
            
            # Get and sort scenes
            scenes = sorted(
                [f for f in chapter_dir.iterdir() if f.suffix == '.md'],
                key=lambda x: get_scene_number(x.name)
            )
            
            # Process each scene
            for scene_file in scenes:
                try:
                    with open(scene_file, 'r', encoding='utf-8') as f:
                        scene_content = f.read().strip()
                        if scene_content:  # Only add non-empty scenes
                            full_content.append(f"\n### {scene_file.stem.upper()}\n\n")
                            full_content.append(scene_content + "\n\n")
                except Exception as e:
                    print(f"Error reading {scene_file}: {e}")
    
    # Write everything to the output file
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(''.join(full_content))
        print(f"Successfully created {output_path}")
    except Exception as e:
        print(f"Error writing output file: {e}")

if __name__ == '__main__':
    concatenate_final_text()
