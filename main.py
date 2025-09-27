import os
from pathlib import Path
from dotenv import load_dotenv


def get_organize_folder_path():
    return os.getenv('ORGANIZE_FOLDER_PATH')

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

organize_folder_path = get_organize_folder_path()
print(organize_folder_path)
for file in Path(organize_folder_path).iterdir():
    if file.is_file():
        file_extension = file.suffix.lower()[1:]
        if file_extension in MAPPING_EXTENSION_FOR_FOLDER:
            folder_name = MAPPING_EXTENSION_FOR_FOLDER[file_extension]
            folder_path = Path(organize_folder_path) / folder_name
            if not folder_path.exists():
                folder_path.mkdir()
            file.rename(folder_path / file.name)