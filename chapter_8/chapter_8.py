#!/usr/bin/env python
import pyinputplus as pyip
from typing import Tuple
import random

def sandwich_input() -> Tuple[str, str, str, str, str, str, str, int]:
    bread: str = pyip.inputMenu(['White', 'wheat', 'Sourdough'], prompt="Select you Bread:\n")
    protein: str = pyip.inputMenu(['Chicken', "Turkey", 'Ham', 'Tofu'], prompt="Select your Protein:\n")
    cheese: str = pyip.inputYesNo(prompt="Do you want cheese?:  ")
    mayo: str = pyip.inputYesNo(prompt="Do you want mayo?: ")
    mustard: str = pyip.inputYesNo(prompt="Do you want mustard?:  ")
    lettuce: str = pyip.inputYesNo(prompt="Do you want lettuce?:  ")
    tomato: str = pyip.inputYesNo(prompt="Do you want tomato?:  ")
    count: int = pyip.inputInt(prompt="How many sandwiches do you want?: ", max=10,min=1)
    return (bread, protein, cheese, mayo, mustard, lettuce, tomato, count)

def multiplication_quiz() -> None:
    for i in range(10):
        a = random.randint(0,100)
        b = random.randint(0,100)
        answer = a * b
        correct = False
        question = f"Question {1}) What is {a} * {b}?: "
        try:
            for q in range(3): # three tries
                user_ans = pyip.inputInt(prompt = question, min=0, timeout=8)
                if user_ans != answer:
                    print("Incorrect")
                else:
                    print("Correct")
                    correct = True
                    break
            if not correct:
                print("Ran out of tries")
        except pyip.TimeoutException:
            print("Time ran out!!")
try: # skip sandwich input
  print(sandwich_input())
except KeyboardInterrupt:
  print("\n---Skipping  Sandwich Input---")
multiplication_quiz()
