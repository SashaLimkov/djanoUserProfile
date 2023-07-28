from random import choices
from string import ascii_letters, digits


def generate_password(length: int) -> str:
    characters = ascii_letters + digits
    return ''.join(choices(characters, k=length)).strip()

import string, random
 
def generate_password_with_special_characters(length): 
    letters_and_symbols = list(string.ascii_letters + string.digits + "!@#$%&*")
    random.shuffle(letters_and_symbols)
    password_chars = []
    while len(password_chars) < length:
        password_chars.append(random.choice(letters_and_symbols))
    return "".join(password_chars)


print(generate_password_with_special_characters(8))