import os

 # Structure from chapter_scene_overview.md
 structure = {
     "act1": {
         "chapter1": ["scene1", "scene2", "scene3"],  # The Awakening
         "chapter2": ["scene1", "scene2", "scene3"],  # Architects of Chang
         "chapter3": ["scene1", "scene2", "scene3"],  # Echoes of the Futur
         "chapter4": ["scene1", "scene2", "scene3"],  # Front Lines
         "chapter5": ["scene1", "scene2", "scene3"]   # Breaking Points
     },
     "act2": {
         "chapter6": ["scene1", "scene2", "scene3"],  # New Rules
         "chapter7": ["scene1", "scene2", "scene3"],  # The Price of Progre
         "chapter8": ["scene1", "scene2", "scene3"],  # Fragile Alliances
         "chapter9": ["scene1", "scene2", "scene3"]   # Crisis Points
     },
     "act3": {
         "chapter10": ["scene1", "scene2", "scene3"], # Crisis Points
         "chapter11": ["scene1", "scene2", "scene3"], # Turning Points
         "chapter12": ["scene1", "scene2", "scene3"]  # Final Confrontation
     }
 }

 def create_directory_structure():
     base_path = ".final_text"

     # Create base directory if it doesn't exist
     if not os.path.exists(base_path):
         os.makedirs(base_path)

     # Create the structure
     for act, chapters in structure.items():
         act_path = os.path.join(base_path, act)
         if not os.path.exists(act_path):
             os.makedirs(act_path)

         for chapter, scenes in chapters.items():
             chapter_path = os.path.join(act_path, chapter)
             if not os.path.exists(chapter_path):
                 os.makedirs(chapter_path)

             for scene in scenes:
                 scene_file = os.path.join(chapter_path, f"{scene}.md")
                 if not os.path.exists(scene_file):
                     # Create empty file
                     open(scene_file, 'w').close()

 if __name__ == "__main__":
     create_directory_structure()
     print("Empty directory structure created successfully!")