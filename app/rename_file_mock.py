import string
import random

letters = string.ascii_lowercase

def get_random_string():
    return (''.join(random.choice(letters) for i in range(5)))