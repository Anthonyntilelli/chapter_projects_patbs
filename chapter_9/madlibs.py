#!/usr/bin/env python
from pathlib import Path

KEYWORDS = ("ADJECTIVE", "NOUN", "ADVERB", "VERB")
source_file = open(Path(Path.cwd(),"chapter_9","madlibs_source.txt"))
lines = source_file.readlines()
source_file.close()

result_file = open(Path(Path.cwd(),"chapter_9","madlibs_results.txt"), "a")

for line in lines:
    if line == "\n": ## Skip empty lines
        continue
    word_list = [] 
    words = line.strip().split() # remove end \n
    for word in words:
        has_period = False
        if word.endswith("."):
            word = word[:-1]
            has_period = True
        if word in KEYWORDS:
            print(f"Enter a {word}:")
            word = input()
        
        if has_period:
            word = word + "."
            word_list.append(word)
        else:
            word_list.append(word)
    new_sentence = " ".join(word_list)
    print(new_sentence)
    result_file.write(new_sentence + "\n")

result_file.close()



    





# Save new sentances.