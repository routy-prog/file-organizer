# File Organizer

A simple Python utility that automatically organizes files into folders based on their extensions.

## Features

- Organizes images, music, documents, and Python files.
- Creates category folders automatically.
- Moves files using their extensions.
- Reports unknown file types.

## Requirements

- Python 3.10 or newer

## Usage

1. Place the files you want to organize into the `test_files` folder.
2. Run the program:

   ```bash
   python main.py
   ```

3. The program will move recognized files into category folders.

## Supported file types

| Category | Extensions |
|---|---|
| Images | `.jpg`, `.jpeg`, `.png` |
| Music | `.mp3`, `.wav`, `.mp4` |
| Documents | `.pdf`, `.doc`, `.docx` |
| Python | `.py` |

## Project structure

```text
file-organizer/
├── main.py
├── README.md
└── .gitignore
```

## Future improvements

- Add more file types.
- Add logging.
- Allow users to select a folder.

## License

This project is for educational purposes.