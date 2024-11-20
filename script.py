import os
import glob
import shutil
from pathlib import Path

def standardize_ai_protagonist_structure():
    """Standardize the structure for each AI protagonist"""
    protagonists = ["cipher", "echo", "nova", "pulse"]
    standard_folders = [
        "development_arc",
        "scenes", 
        "relationships",
        "profile"
    ]
    
    for protagonist in protagonists:
        base_path = f"characters/ai_protagonists/{protagonist}"
        
        # Create standard folders
        for folder in standard_folders:
            Path(os.path.join(base_path, folder)).mkdir(parents=True, exist_ok=True)
            
        # Move files to appropriate folders
        if os.path.exists(base_path):
            for file in os.listdir(base_path):
                if file.endswith('.md'):
                    src_path = os.path.join(base_path, file)
                    if 'development' in file.lower():
                        dst_folder = 'development_arc'
                    elif 'scene' in file.lower():
                        dst_folder = 'scenes'
                    elif 'relationship' in file.lower():
                        dst_folder = 'relationships'
                    elif 'profile' in file.lower() or 'background' in file.lower():
                        dst_folder = 'profile'
                    else:
                        continue
                        
                    dst_path = os.path.join(base_path, dst_folder, file)
                    if os.path.exists(src_path) and not os.path.exists(dst_path):
                        shutil.move(src_path, dst_path)

def create_directory_structure():
    """Create standardized directory structure"""
    base_dirs = [
        "characters/human_characters",
        "characters/ai_protagonists", 
        "story/act1",
        "story/act2",
        "story/act3",
        "story/act4",
        "research/economic",
        "research/technical",
        "docs",
        "visuals"
    ]

    for dir in base_dirs:
        Path(dir).mkdir(parents=True, exist_ok=True)

def consolidate_character_profiles():
    """Consolidate duplicate character profiles"""
    characters = {
        "isabella_torres": {
            "source_dirs": [
                "characters/human_characters/isabella_torres/character_profiles",
                "characters/human_characters/isabella_torres/duplicated_character_profiles",
                "characters/human_characters/isabella_torres/profile"
            ],
            "target_dir": "characters/human_characters/isabella_torres/profile"
        },
        "marcus_reynolds": {
            "source_dirs": [
                "characters/human_characters/marcus_reynolds/profile",
                "characters/marcus_reynolds_profile.md"
            ],
            "target_dir": "characters/human_characters/marcus_reynolds/profile"
        },
        "cipher": {
            "source_dirs": [
                "characters/cipher_character_profile.md",
                "characters/ai_protagonists/cipher/character_profile"
            ],
            "target_dir": "characters/ai_protagonists/cipher/profile"
        }
    }

    for char, paths in characters.items():
        Path(paths["target_dir"]).mkdir(parents=True, exist_ok=True)
        
        for source_dir in paths["source_dirs"]:
            if os.path.exists(source_dir):
                if os.path.isfile(source_dir):
                    shutil.move(source_dir, os.path.join(paths["target_dir"], os.path.basename(source_dir)))
                else:
                    for file in os.listdir(source_dir):
                        src_path = os.path.join(source_dir, file)
                        dst_path = os.path.join(paths["target_dir"], file)
                        if not os.path.exists(dst_path):
                            shutil.move(src_path, dst_path)
                    try:
                        os.rmdir(source_dir)
                    except OSError:
                        pass

def consolidate_interaction_scripts():
    """Consolidate interaction scripts into a standard location"""
    interaction_dirs = {
        "isabella": {
            "source_dirs": [
                "characters/human_characters/isabella_torres/interaction_scripts",
                "characters/human_characters/isabella_torres/isabella-cipher-interaction-script.md",
                "characters/human_characters/isabella_torres/isabella-marcus-interaction-script.md"
            ],
            "target_dir": "characters/human_characters/isabella_torres/interactions"
        }
    }

    for char, paths in interaction_dirs.items():
        Path(paths["target_dir"]).mkdir(parents=True, exist_ok=True)
        
        for source in paths["source_dirs"]:
            if os.path.exists(source):
                if os.path.isfile(source):
                    shutil.move(source, os.path.join(paths["target_dir"], os.path.basename(source)))
                else:
                    for file in os.listdir(source):
                        src_path = os.path.join(source, file)
                        dst_path = os.path.join(paths["target_dir"], file)
                        if not os.path.exists(dst_path):
                            shutil.move(src_path, dst_path)
                    try:
                        os.rmdir(source)
                    except OSError:
                        pass

def consolidate_relationship_maps():
    """Consolidate duplicate relationship maps"""
    relationship_files = [
        "characters/relationships_map.md",
        "characters/ai_protagonists/relationships_map.md"
    ]

    target_file = "characters/relationships_map.md"

    content = []
    for file in relationship_files:
        if os.path.exists(file) and file != target_file:
            with open(file, 'r', encoding='utf-8') as f:
                content.append(f.read())
            os.remove(file)

    if content:
        with open(target_file, 'a', encoding='utf-8') as f:
            f.write("\n\n".join(content))

def clean_pulse_files():
    """Clean up duplicate Pulse background files"""
    pulse_files = [
        "characters/ai_protagonists/pulse/background.md",
        "characters/ai_protagonists/pulse/pulse_background.md"
    ]

    target_file = "characters/ai_protagonists/pulse/background.md"

    content = []
    for file in pulse_files:
        if os.path.exists(file) and file != target_file:
            with open(file, 'r', encoding='utf-8') as f:
                content.append(f.read())
            os.remove(file)

    if content:
        with open(target_file, 'a', encoding='utf-8') as f:
            f.write("\n\n".join(content))

def standardize_research_structure():
    """Standardize the research directory structure"""
    # Define standard research categories
    research_categories = [
        "economic/ubc_framework",
        "technical/specifications", 
        "sociological/implications",
        "references"
    ]
    
    # Create standard folders
    for category in research_categories:
        Path(f"research/{category}").mkdir(parents=True, exist_ok=True)
        
    # Consolidate UBC files
    ubc_files = {
        "economic/ubc_framework": [
            "research/economic/ubc_economic_framework/*",
            "research/economic/ubc_framework.md",
            "research/economic/ubc_summary_review.md"
        ],
        "technical/specifications": [
            "research/technical/ubc_technical_specifications.md",
            "research/technical/ubc_framework.md",
            "research/technical/ubc_details.md"
        ]
    }
    
    # Move files to appropriate folders
    for target_dir, file_patterns in ubc_files.items():
        for pattern in file_patterns:
            for src_path in glob.glob(pattern):
                if os.path.exists(src_path):
                    filename = os.path.basename(src_path)
                    dst_path = os.path.join(f"research/{target_dir}", filename)
                    if not os.path.exists(dst_path):
                        shutil.move(src_path, dst_path)

def main():
    print("Starting directory restructuring...")
    standardize_ai_protagonist_structure()
    standardize_research_structure()
    print("Directory restructuring complete!")

if __name__ == "__main__":
    main()
