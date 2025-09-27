import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

ORGANIZE_FOLDER_PATH = os.getenv('ORGANIZE_FOLDER_PATH')

MAPPING_EXTENSION_FOR_FOLDER = {
    'exe': 'Application',
    'png': 'Image',
    'jpeg': 'Image',
    'jpg': 'Image',
    'pdf': 'Documents',
    'xlsx': 'Documents',
    'csv': 'Documents',
    'json': 'Collections',
    'docx': 'Documents',
    'txt': 'Documents',
    'mp3': 'Music',
    'wav': 'Music',
    'mp4': 'Video',
    'zip': 'Compressed',
    'rar': 'Compressed',
    '7z': 'Compressed',
    'iso': 'Compressed',
    'ipynb': 'Notebooks',
}

for file in Path(ORGANIZE_FOLDER_PATH).iterdir():
    if file.is_file():
        file_extension = file.suffix.lower()[1:]
        if file_extension in MAPPING_EXTENSION_FOR_FOLDER:
            folder_name = MAPPING_EXTENSION_FOR_FOLDER[file_extension]
            folder_path = Path(ORGANIZE_FOLDER_PATH) / folder_name
            if not folder_path.exists():
                folder_path.mkdir()
            file.rename(folder_path / file.name)