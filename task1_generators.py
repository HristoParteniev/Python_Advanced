"""imports"""
import os
import random
from datetime import datetime, timedelta

def consecutive_numbers_generator():
    """ Generating numbers """
    for i in range(1, 21):
        yield i

def generate_random_word(number):
    """ Generating words """
    while True:
        result = ''
        for _ in range(number):
            result += chr(random.randint(97,122))    # generate letters a-z
        yield result

def generate_random_timestamp():
    """ Generating timestamps """
    while True:
        min_date = datetime(1970, 1, 1)
        max_date = datetime(2024, 12, 31)
        rand_interval = random.randrange((max_date - min_date).days)
        rand_date = min_date + timedelta(days=rand_interval)
        yield str(rand_date)

def generate_random_bool():
    """ Generating boolean values """
    while True:
        yield random.choice([True,False])

if __name__ == '__main__':
    num_gen = consecutive_numbers_generator()
    word_gen = generate_random_word(8)
    ts_gen = generate_random_timestamp()
    bool_gen = generate_random_bool()

    desktop_path = os.path.join(os.path.expanduser("~"),
    'OneDrive - Adastra, s.r.o\\Desktop\\Task1_Generators_python_by_Hristo_Parteniev.txt')

    with open(desktop_path, 'w', encoding='utf-8') as file:
        for _ in range(20):
            file.write(f'"{next(num_gen)}",\
                "{next(word_gen)}",\
                    "{next(ts_gen)}",\
                        "{next(bool_gen)}"'+ '\n')
