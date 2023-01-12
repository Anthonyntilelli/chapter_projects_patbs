#!/usr/bin/env python
import sys
from pathlib import Path
from PyPDF2 import PdfReader

if len(sys.argv) != 2 or not sys.argv[1].endswith(".pdf"):
    print("Please enter pdf file")
    exit(1)

words_file = Path("chapter_15", "dictionary.txt")
if not words_file.is_file():
    print("dictionary.txt is missing or not a file")
    exit(1)

pdf_file = Path(sys.argv[1])
if not pdf_file.is_file():
    print(f"{pdf_file} is missing or not a valid file")
    exit(1)


reader = PdfReader(str(pdf_file))
if not reader.is_encrypted:
    print("Not and encrypted file")
    exit(1)

print("Starting the Brute force...")
with open(words_file) as f:
    for line in f.readlines():
        attempt = line.strip()
        res = reader.decrypt(attempt.upper())
        if res != res.NOT_DECRYPTED:
            print(f"Password is {attempt.upper()}")
            break
        res = reader.decrypt(attempt.lower())
        if res != res.NOT_DECRYPTED:
            print(f"Password is {attempt.lower()}")
            break



