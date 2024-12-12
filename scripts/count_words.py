 import os
 import re

 def count_words(text):
     # Remove markdown formatting and count words
     text = re.sub(r'#.*?\n', '', text)  # Remove headers
     text = re.sub(r'\*\*.*?\*\*', '', text)  # Remove bold text
     text = re.sub(r'\*.*?\*', '', text)  # Remove italic text
     words = re.findall(r'\w+', text)
     return len(words)

 def analyze_final_text(root_dir='final_text'):
     word_counts = {}

     # Walk through the directory structure
     for act_name in os.listdir(root_dir):
         act_path = os.path.join(root_dir, act_name)
         if not os.path.isdir(act_path):
             continue

         word_counts[act_name] = {'total': 0, 'chapters': {}}

         # Process each chapter
         for chapter_name in os.listdir(act_path):
             chapter_path = os.path.join(act_path, chapter_name)
             if not os.path.isdir(chapter_path):
                 continue

             word_counts[act_name]['chapters'][chapter_name] = {'total': 0,
 'scenes': {}}

             # Process each scene
             for scene_name in os.listdir(chapter_path):
                 if not scene_name.endswith('.md'):
                     continue

                 scene_path = os.path.join(chapter_path, scene_name)
                 with open(scene_path, 'r', encoding='utf-8') as f:
                     text = f.read()
                     word_count = count_words(text)
                     word_counts[act_name]['chapters'][chapter_name]['scenes'][s
 ne_name] = word_count
                     word_counts[act_name]['chapters'][chapter_name]['total'] +=
 word_count
                     word_counts[act_name]['total'] += word_count

     # Print results
     print("Word Count Analysis\n")

     for act_name, act_data in word_counts.items():
         print(f"\n{act_name}: {act_data['total']} words")

         for chapter_name, chapter_data in act_data['chapters'].items():
             print(f"  {chapter_name}: {chapter_data['total']} words")

             for scene_name, scene_count in chapter_data['scenes'].items():
                 print(f"    {scene_name}: {scene_count} words")

 if __name__ == '__main__':
     analyze_final_text()