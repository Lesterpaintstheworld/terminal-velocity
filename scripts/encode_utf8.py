import os
import chardet
from pathlib import Path

def convert_to_utf8(file_path):
    try:
        # Détecter l'encodage actuel
        with open(file_path, 'rb') as file:
            raw_data = file.read()
            result = chardet.detect(raw_data)
            current_encoding = result['encoding']

        # Si ce n'est pas déjà en UTF-8, convertir
        if current_encoding and current_encoding.lower() != 'utf-8':
            # Lire avec l'encodage détecté
            with open(file_path, 'r', encoding=current_encoding) as file:
                content = file.read()
            
            # Réécrire en UTF-8
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"Converti: {file_path} de {current_encoding} vers UTF-8")
        
    except Exception as e:
        print(f"Erreur avec {file_path}: {str(e)}")

def main():
    # Extensions de fichiers texte à traiter
    text_extensions = {'.md', '.txt', '.py', '.json', '.yml', '.yaml'}
    
    # Partir du répertoire racine du projet
    root_dir = Path(__file__).parent.parent
    
    # Parcourir récursivement
    for path in root_dir.rglob('*'):
        if path.is_file() and path.suffix in text_extensions:
            convert_to_utf8(str(path))

if __name__ == '__main__':
    main()
