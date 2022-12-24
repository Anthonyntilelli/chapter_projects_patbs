#!/usr/bin/env python
import re

def date_detection(date: str) -> bool:
    """Checks for format DD/MM/YYYY and returns true or false"""
    pattern = re.compile(r"^(0[1-9]|1[0-9]|2[0-9]|3[0-1])/(0[0-9]|1[0-2])/\d{4}$")
    result = pattern.search(date)
    if result is None:
        return False
    return True

def strong_password(password: str) -> bool:
    """Check is a password is 8+ characters and is a mix of lowcase, upercase and digit"""
    size = re.compile(r"[\w]{8,}")
    upper = re.compile(r"[A-Z]")
    diget = re.compile(r"\d")
    lower = re.compile(r"[a-z]")

    if size.search(password) is None:
        return False    
    if upper.search(password) is None:
        return False
    if diget.search(password) is None:
        return False
    if lower.search(password) is None:
        return False
    return True

def reg_strip(word: str) -> str:
    left = re.compile(r"^\s")
    stripped = left.sub("", word)
    right = re.compile(r"\s$")
    return right.sub("", stripped)

print("-----date_detection False-----")
print(date_detection("potato"))
print(date_detection("10/13/1990"))
print(date_detection("10/1212/1990"))
print(date_detection("5/10/1990"))
print(date_detection("32/10/1990"))
print("-----date_detection TRUE-----")
print(date_detection("01/01/1990"))
print(date_detection("01/02/1990"))
print(date_detection("01/12/1990"))
print(date_detection("10/12/1990"))
print(date_detection("31/12/1990"))

print("-----strong_password False -----")
print(strong_password("short"))
print(strong_password("loooooooooooong"))
print(strong_password("123456789"))
print(strong_password("abc123def456"))
print(strong_password("ABC123DEF456"))
print("-----strong_password True -----")
print(strong_password("abc123DEF456"))
print(strong_password("ABC123def456"))

print("-----reg_strip-----")
print(reg_strip('\nitem1\n'))
print(reg_strip("\titem2\t"))
print(reg_strip(" item3  "))
print(reg_strip("item 4"))