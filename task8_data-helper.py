import datetime
import random

def get_random_date():
    min_date = datetime.datetime(1970, 1, 1)
    max_date = datetime.datetime(2024, 12, 31)
    rand_interval = random.randrange((max_date - min_date).days)
    rand_date = min_date + datetime.timedelta(days=rand_interval)
    return str(rand_date)[:10]

def get_random_string():
    result = ''
    for _ in range(8):
        result += chr(random.randint(97,122))
    return result.capitalize()

def get_random_integer():
    number = random.randint(1, 1000)
    return number

def get_random_double():
    number = random.randint(1, 1000)
    divisor = random.randint(1, 1000)
    result = number / divisor
    return round(result, 2)
