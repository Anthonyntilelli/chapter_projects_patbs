#!/usr/bin/env python

import os, re, shutil
from pathlib  import Path

gapLoc = Path("chapter_10", "gaps")
if not gapLoc.is_dir():
    print("Gap location is missing or not a directory.")
    exit(1)

files = list(os.listdir(gapLoc))
files.sort()
count = 1 # files start at 1
pattern = re.compile(r"(.+)(\d\d)\.(\w+)")
for file in files:
    match = pattern.search(file)
    if match != None:
        head = match.group(1)
        num = match.group(2)
        end = match.group(3)
        if int(num) != count:
            if count <= 10:
              num = "0" + str(count)
            else:
              num = str(count)
            shutil.move(str(gapLoc/file), str(gapLoc / (head + num + end)))
        count += 1