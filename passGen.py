# Import required libraries
from string import ascii_letters, digits, punctuation
from random import choice


class PassGen(object):

    def __init__(self, is_special: bool):
        self._characters = ascii_letters + digits + punctuation if is_special else ascii_letters + digits
        self._password: list[str] = []

    # Generation of passwords
    def generate(self, length: int) -> list[str]:
        for x in range(10):
            self._password.append('')
            for i in range(length):
                self._password[x] += choice(self._characters)
        return self._password
