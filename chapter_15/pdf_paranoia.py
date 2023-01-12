#!/usr/bin/env python
from pathlib import Path
import sys, os
from PyPDF2 import PdfReader, PdfWriter

options = ("e", "d")

if len(sys.argv) != 2:
    print("Please enter 'e' (encrypt) or 'd' (decrypt) as a command line arg")
    exit(1)

if sys.argv[1] not in options:
    print(f"Invalid option please choose {options}")
    exit(1)

password = input("Enter the pdf password: ")

for folderName, subFolders, fileNames in os.walk("."):
    if "/." in folderName:
        continue # Skip hidden folders
    if r"\." in folderName:
        continue # Skip hidden folders (windows)
    if "venv" in folderName:
        continue # Skip venv folders
 
    for file in fileNames:
        if sys.argv[1] == "e":
            if file.endswith(".pdf") and not file.endswith("_encrypted.pdf"):
                fileLocation = str(Path(folderName,file))
                reader = PdfReader(fileLocation)
                writer = PdfWriter()
                for page in reader.pages:
                    writer.add_page(page)
                writer.encrypt(password)
                no_suffix = fileLocation.removesuffix(".pdf")
                with open(f"{no_suffix}_encrypted.pdf", "wb") as f:
                        writer.write(f)
                testReader = PdfReader(f"{no_suffix}_encrypted.pdf")
                if not testReader.is_encrypted:
                    raise NotImplementedError(f"file {fileLocation}_encrypted.pdf did not encrypt properly.")
                os.remove(fileLocation)
            
        if sys.argv[1] == "d":
            if file.endswith("_encrypted.pdf"):
                encryptedFileLocation = str(Path(folderName,file))
                reader = PdfReader(encryptedFileLocation)
                writer = PdfWriter()

                if reader.is_encrypted:
                    results = reader.decrypt(password)
                else:
                    print(f"Skipping {encryptedFileLocation} it is not encrypted")
                    continue
                try:
                    for page in reader.pages:
                        writer.add_page(page)
                        stripped = encryptedFileLocation.removesuffix("_encrypted.pdf")
                        with open(f"{stripped}.pdf", "wb") as f:
                            writer.write(f)
                except Exception:
                    print(f"Skipping {encryptedFileLocation} Incorrect password")

