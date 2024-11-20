import os
import shutil
from pathlib import Path

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
                 "characters/human_characters/isabella_torres/character_pro
 les",
                 "characters/human_characters/isabella_torres/duplicated_ch
 acter_profiles",
                 "characters/human_characters/isabella_torres/profile"
             ],
             "target_dir":
 "characters/human_characters/isabella_torres/profile"
         },
         "marcus_reynolds": {
             "source_dirs": [
                 "characters/human_characters/marcus_reynolds/profile",
                 "characters/marcus_reynolds_profile.md"
             ],
             "target_dir":
 "characters/human_characters/marcus_reynolds/profile"
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
         # Create target directory
         Path(paths["target_dir"]).mkdir(parents=True, exist_ok=True)

         # Move and merge files
         for source_dir in paths["source_dirs"]:
             if os.path.exists(source_dir):
                 if os.path.isfile(source_dir):
                     # Handle single files
                     shutil.move(source_dir,
                               os.path.join(paths["target_dir"],
 os.path.basename(source_dir)))
                 else:
                     # Handle directories
                     for file in os.listdir(source_dir):
                         src_path = os.path.join(source_dir, file)
                         dst_path = os.path.join(paths["target_dir"], file)
                         if not os.path.exists(dst_path):
                             shutil.move(src_path, dst_path)

                     # Remove empty source directory
                     try:
                         os.rmdir(source_dir)
                     except OSError:
                         pass

 def consolidate_interaction_scripts():
     """Consolidate interaction scripts into a standard location"""
     interaction_dirs = {
         "isabella": {
             "source_dirs": [
                 "characters/human_characters/isabella_torres/interaction_s
 ipts",
                 "characters/human_characters/isabella_torres/isabella-ciph
 -interaction-script.md",
                 "characters/human_characters/isabella_torres/isabella-marc
 -interaction-script.md"
             ],
             "target_dir":
 "characters/human_characters/isabella_torres/interactions"
         }
     }

     for char, paths in interaction_dirs.items():
         Path(paths["target_dir"]).mkdir(parents=True, exist_ok=True)

         for source in paths["source_dirs"]:
             if os.path.exists(source):
                 if os.path.isfile(source):
                     shutil.move(source,
                               os.path.join(paths["target_dir"],
 os.path.basename(source)))
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

     # Merge content if multiple files exist
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

     # Merge content if both files exist
     content = []
     for file in pulse_files:
         if os.path.exists(file) and file != target_file:
             with open(file, 'r', encoding='utf-8') as f:
                 content.append(f.read())
             os.remove(file)

     if content:
         with open(target_file, 'a', encoding='utf-8') as f:
             f.write("\n\n".join(content))

 def main():
     print("Starting repository restructuring...")

     # Create base directory structure
     create_directory_structure()

     # Consolidate character profiles
     print("Consolidating character profiles...")
     consolidate_character_profiles()

     # Consolidate interaction scripts
     print("Consolidating interaction scripts...")
     consolidate_interaction_scripts()

     # Consolidate relationship maps
     print("Consolidating relationship maps...")
     consolidate_relationship_maps()

     # Clean up Pulse files
     print("Cleaning up Pulse files...")
     clean_pulse_files()

     print("Repository restructuring complete!")

 if __name__ == "__main__":
     main()