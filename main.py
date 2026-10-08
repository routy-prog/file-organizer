import os, shutil

categories = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".mp3": "Music",
    ".wav": "Music",
    ".mp4": "Music",
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".py": "Python"
}

files = os.listdir("test_files")

for category in categories.values():
    os.makedirs(f"test_files/{category}", exist_ok=True)

for file in files:
    name, extension = os.path.splitext(file)
    if extension in categories:
        shutil.move(f"test_files/{file}", f"test_files/{categories[extension]}/{file}")
    else:
        print("Неизвестный тип")