import os
import re
import argparse
from datetime import datetime
from pathlib import Path
from tqdm import tqdm

def get_act_number(act_name):
    """Extract numeric value from act name (e.g., 'act1' -> 1)"""
    return int(act_name.replace('act', ''))

def get_chapter_number(chapter_name):
    """Extract numeric value from chapter name (e.g., 'chapter1' -> 1)"""
    try:
        # Only process directories that start with 'chapter'
        if not chapter_name.startswith('chapter'):
            return float('inf')  # Put non-chapter directories at the end
        return int(chapter_name.replace('chapter', ''))
    except ValueError:
        return float('inf')  # Handle invalid formats

def get_scene_number(scene_name):
    """Extract numeric value from scene name (e.g., 'scene1.md' -> 1)"""
    try:
        # Only process files that start with 'scene'
        if not scene_name.startswith('scene'):
            return float('inf')  # Put non-scene files at the end
        return int(scene_name.replace('scene', '').replace('.md', ''))
    except ValueError:
        return float('inf')  # Handle invalid formats

def validate_directory_structure(root_dir: Path) -> bool:
    """Validate that the directory structure matches expected format"""
    if not root_dir.exists():
        print(f"Error: Directory {root_dir} does not exist")
        return False
    
    acts = [d for d in root_dir.iterdir() if d.is_dir()]
    if not acts:
        print(f"Error: No acts found in {root_dir}")
        return False
    
    return True

def generate_metadata_header():
    """Generate a metadata header for the manuscript"""
    return f"""---
generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
source_directory: final_text
---

"""

def clean_content(content: str) -> str:
    """Clean up content by removing extra whitespace and standardizing line breaks"""
    # Remove multiple blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)
    # Remove trailing whitespace
    content = re.sub(r'[ \t]+$', '', content, flags=re.MULTILINE)
    return content

def concatenate_final_text(input_dir='final_text', output_file='complete_manuscript.md', clean=False):
    """
    Concatenate all markdown files from final_text directory into a single file,
    maintaining the proper order of acts, chapters, and scenes.
    """
    # Get the root directory
    root_dir = Path(input_dir)
    output_path = Path(output_file)
    
    if not validate_directory_structure(root_dir):
        return
    
    # Dictionary to store all content
    full_content = []
    
    # Get all acts and sort them (only process directories starting with 'act')
    acts = sorted(
        [d for d in root_dir.iterdir() if d.is_dir() and d.name.startswith('act')],
        key=lambda x: get_act_number(x.name)
    )
    
    # Process each act
    for act_dir in tqdm(acts, desc="Processing acts"):
        full_content.append(f"\n\n# {act_dir.name.upper()}\n\n")
        
        # Get and sort chapters (only process directories starting with 'chapter')
        chapters = sorted(
            [d for d in act_dir.iterdir() if d.is_dir() and d.name.startswith('chapter')],
            key=lambda x: get_chapter_number(x.name)
        )
        
        # Process each chapter
        for chapter_dir in tqdm(chapters, desc=f"Processing chapters in {act_dir.name}", leave=False):
            full_content.append(f"\n## {chapter_dir.name.upper()}\n\n")
            
            # Get and sort scenes (only process scene*.md files)
            scenes = sorted(
                [f for f in chapter_dir.iterdir() if f.suffix == '.md' and f.stem.startswith('scene')],
                key=lambda x: get_scene_number(x.name)
            )
            
            # Process each scene
            for scene_file in tqdm(scenes, desc=f"Processing scenes in {chapter_dir.name}", leave=False):
                try:
                    with open(scene_file, 'r', encoding='utf-8') as f:
                        scene_content = f.read().strip()
                        if scene_content:  # Only add non-empty scenes
                            full_content.append(f"\n### {scene_file.stem.upper()}\n\n")
                            full_content.append(scene_content + "\n\n")
                except Exception as e:
                    print(f"Error reading {scene_file}: {e}")
    
    # Prepare final content
    final_content = ''.join(full_content)
    if clean:
        final_content = clean_content(final_content)

    # Write everything to the output file
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(generate_metadata_header())
            f.write(final_content)
        print(f"Successfully created {output_path}")
    except Exception as e:
        print(f"Error writing output file: {e}")

def parse_args():
    parser = argparse.ArgumentParser(description='Concatenate final text files into a single manuscript.')
    parser.add_argument('--input-dir', default='final_text', help='Input directory containing the text files')
    parser.add_argument('--output-file', default='complete_manuscript.md', help='Output file path')
    parser.add_argument('--clean', action='store_true', help='Clean up extra whitespace and line breaks')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    concatenate_final_text(args.input_dir, args.output_file, args.clean)
