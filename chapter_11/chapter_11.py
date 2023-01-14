#!/usr/bin/env python
import random

def ask(choices: tuple[str], prompt: str) -> str:
    guess = ""
    while guess not in choices:
      guess = input(prompt)
    return guess

coin = ("head","tail")
guess = ask(coin, "Guess the coin toss! Enter head or tail: ")
toss = random.choice(coin)
if toss == guess:
    print("You got it!")
else:
    guess = ask(coin,"Nope! Guess again!: ")
    toss = random.choice(coin)
    if toss == guess:
        print("You got it!")
    else:
        print("Nope. You are really bad at this game.")