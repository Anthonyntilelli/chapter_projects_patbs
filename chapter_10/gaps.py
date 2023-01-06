#!/usr/bin/env python

import os, shutil
from pathlib  import Path

gapLoc = Path("chapter_10", "gaps")
if not gapLoc.is_dir():
    print("Gap location is missing or not a directory.")
    exit(1)
