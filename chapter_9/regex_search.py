#!/usr/bin/env python
from pathlib import Path
import re

found = False
folder = Path(Path.cwd())
text_files = list(folder.glob("*.txt"))
if len(text_files) == 0:
    print("No text files found in CWD")
    exit()

string_re = input("Please provide a regex to search the files: ")
regex = re.compile(string_re)

for file_path in text_files:
    file = open(file_path, "r")
    lines = file.readlines()
    file.close()
    for line in lines:
        match = regex.search(line)
        if match != None:
            # Grep like print out
            output = str(file_path) + ":" + line.strip()  ## Remove \n
            print(output)
            found = True
        
if found: # GREP like
    exit(0) # something found 
else:
    exit(1) # nothing found
