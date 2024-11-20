import os

def create_scene_template(act, chapter, scene):
    content = f"""# Scene {act}.{chapter}.{scene}

## Setting
[Describe the physical or virtual location and atmosphere]

## Characters Present
- [List main characters present]
- [Supporting characters if any]

## Scene Summary
[1-2 paragraphs describing the key events and purpose of the scene]

## Key Moments
1. **First Major Beat**
   - [Detail point]
   - [Detail point]
   - [Detail point]

2. **Second Major Beat**
   - [Detail point]
   - [Detail point]
   - [Detail point]

3. **Third Major Beat**
   - [Detail point]
   - [Detail point]
   - [Detail point]

## Emotional Beats
- [Character]: [Emotional journey]
- [Character]: [Emotional journey]
- [Overall tone progression]

## Technical Elements
- [Relevant technology]
- [Systems involved]
- [Technical considerations]

## Dialogue Highlights
**[Character]**: "[Key dialogue line]"

**[Character]**: "[Key dialogue line]"

**[Character]**: "[Key dialogue line]"

## Scene Impact
- [Major consequence]
- [Character development]
- [Plot progression]

## Notes
- [Important consideration]
- [Writing guidance]
- [Future implications]
"""
    
    # Create directory structure
    dir_path = f"story/act{act}/chapter{chapter}/scene{scene}"
    os.makedirs(dir_path, exist_ok=True)
    
    # Create file
    filename = f"{dir_path}/{act}_{chapter}_{scene}_scene.md"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created: {filename}")

def main():
    # Generate scenes for Acts 2-4
    for act in range(2, 5):  # Acts 2-4
        for chapter in range(1, 6):  # 5 chapters per act
            for scene in range(1, 4):  # 3 scenes per chapter
                create_scene_template(act, chapter, scene)

if __name__ == "__main__":
    main()
