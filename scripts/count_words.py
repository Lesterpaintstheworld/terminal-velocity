import os
import re

def count_words(text):
    text = re.sub(r'#.*?\n', '', text)
    text = re.sub(r'\*\*.*?\*\*', '', text)
    text = re.sub(r'\*.*?\*', '', text)
    words = re.findall(r'\w+', text)
    return len(words)

def analyze_final_text(root_dir='final_text', target_total=150000):
    target_per_act = target_total / 3  # 50,000 words
    target_per_chapter = target_per_act / 5  # 10,000 words
    target_per_scene = target_per_chapter / 3  # ~3,333 words
    
    word_counts = {}
    
    for act_name in os.listdir(root_dir):
        act_path = os.path.join(root_dir, act_name)
        if not os.path.isdir(act_path):
            continue
            
        word_counts[act_name] = {'total': 0, 'chapters': {}}
        
        for chapter_name in os.listdir(act_path):
            chapter_path = os.path.join(act_path, chapter_name)
            if not os.path.isdir(chapter_path):
                continue
                
            word_counts[act_name]['chapters'][chapter_name] = {'total': 0, 'scenes': {}}
            
            for scene_name in os.listdir(chapter_path):
                if not scene_name.endswith('.md'):
                    continue
                    
                scene_path = os.path.join(act_path, chapter_name, scene_name)
                with open(scene_path, 'r', encoding='utf-8') as f:
                    text = f.read()
                    word_count = count_words(text)
                    word_counts[act_name]['chapters'][chapter_name]['scenes'][scene_name] = word_count
                    word_counts[act_name]['chapters'][chapter_name]['total'] += word_count
                    word_counts[act_name]['total'] += word_count

    print("Word Count Analysis\n")
    print(f"Target total: {target_total:,} words")
    print(f"Target per act: {target_per_act:,.0f} words")
    print(f"Target per chapter: {target_per_chapter:,.0f} words")
    print(f"Target per scene: {target_per_scene:,.0f} words\n")
    
    total_words = 0
    for act_name, act_data in word_counts.items():
        act_total = act_data['total']
        total_words += act_total
        act_percentage = (act_total / target_per_act) * 100
        print(f"\n{act_name}: {act_total:,} words ({act_percentage:.1f}% of target)")
        
        for chapter_name, chapter_data in act_data['chapters'].items():
            chapter_total = chapter_data['total']
            chapter_percentage = (chapter_total / target_per_chapter) * 100
            print(f"  {chapter_name}: {chapter_total:,} words ({chapter_percentage:.1f}% of target)")
            
            for scene_name, scene_count in chapter_data['scenes'].items():
                scene_percentage = (scene_count / target_per_scene) * 100
                print(f"    {scene_name}: {scene_count:,} words ({scene_percentage:.1f}% of target)")

    overall_percentage = (total_words / target_total) * 100
    print(f"\nTotal words: {total_words:,} ({overall_percentage:.1f}% of target)")

if __name__ == '__main__':
    analyze_final_text()
