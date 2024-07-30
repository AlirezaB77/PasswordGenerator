import random
import string
from abc import ABC, abstractmethod

import nltk

nltk.download('words')


class PasswordGenerator(ABC):
    @classmethod
    @abstractmethod
    def generate(self) -> None:
        pass

class PinPasswordGenerator(PasswordGenerator):
    def __init__(self,lenght = 8) -> None:
        self.lenght = lenght

    def generate(self) -> None:
        pin = ''.join([random.choice(string.digits) for i in range(self.lenght)])
        return pin

class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self,lenght = 8, number = False , symbol = False) -> None:
        self.lenght = lenght
        self.number = number
        self.symbol = symbol
        self.character =  string.ascii_letters
        if number:
            self.character += string.digits
        if symbol:
            self.character += string.punctuation

    def generate(self) -> None:
        pin = ''.join([random.choice(self.character) for i in range(self.lenght)])
        return pin

class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(self,number_word = 8, separator = '-' , capital = False) -> None:
        self.number_word = number_word
        self.separator = separator
        self.capital = capital
        self.vocab =  nltk.corpus.words.words()

    def generate(self) -> None:
        pin = ([random.choice(self.vocab) for i in range(self.number_word)])
        if self.capital:
            pin = (word.upper() if random.choice([True,False]) else word.lower() for word in pin)
        pin = self.separator.join(pin)
        return pin
