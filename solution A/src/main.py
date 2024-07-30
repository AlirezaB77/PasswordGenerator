import random
import string
from abc import ABC, abstractmethod

import nltk


def PinPasswordGenerator(lenght = 8 , ):
    pin = ''.join([random.choice(string.digits) for i in range(lenght)])
    return pin

def RandomPasswordGenerator(lenght = 8, number = False , symbol = False):
    character =  string.ascii_letters
    if number:
        character += string.digits
    if symbol:
        character += string.punctuation
    pin = ''.join([random.choice(character) for i in range(lenght)])
    return pin

def MemorablePasswordGenerator(number_word = 8, separator = '-' , capital = False):
    vocab =  nltk.corpus.words.words()
    pin = ([random.choice(vocab) for i in range(number_word)])
    if capital:
        pin = (word.upper() if random.choice([True,False]) else word.lower() for word in pin)
    pin = separator.join(pin)
    return pin
