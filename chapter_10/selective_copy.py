#!/usr/bin/env python
# Will copy files ending in .py
import os, shutil
from pathlib  import Path

copyLoc = Path("chapter_10", ".copyLoc")
if not copyLoc.is_dir():
    print("Copy location is missing or not a directory.")
    exit(1)

for folderName, subFolders, fileNames in os.walk("."):
    if "/." in folderName:
        continue # Skip hidden folders
    if r"\." in folderName:
        continue # Skip hidden folders (windows)
    if "venv" in folderName:
        continue # Skip venv folders

    print(folderName)
    print(subFolders)
    print(fileNames)
    print("------")
    for file in fileNames:
        if file.endswith(".py"):
            src = Path(folderName,file)
            shutil.copy(src, str(copyLoc))
