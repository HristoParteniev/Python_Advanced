"""
You have the following string data = 'This is An exAmPlE StRinG'
which is returned by the function get_data().
Write the following decorators and apply all of them on the get_data() function:
1. Split decorator that splits the string into words with a space separator
2. Uppercase decorator that makes all words uppercase
3. Filter decorator that removes all words with < 4 characters length
What is the order of execution of the decorators?
Is it from top to bottom or from bottom to the top?
"""

def split_words_decorator(func):
    """Splitting data into words decorator"""
    def wrapper():
        data = func()
        print("executing first wrapper")
        return data.split()
    return wrapper

def uppercase_decorator(func):
    """Making words uppercase decorator"""
    def wrapper():
        data = func()
        print("executing second wrapper")
        return [x.upper() for x in data]
    return wrapper

def filter_decorator(func):
    """Removing words with less than 4 letters decorator"""
    def wrapper():
        data = func()
        print("executing third wrapper")
        return list(filter(lambda x: len(x) >= 4, data))
    return wrapper

@filter_decorator      # applying third decorator
@uppercase_decorator   # applying second decorator
@split_words_decorator # applying first decorator
def get_data():
    """Main function returning source data string"""
    return 'This is An exAmPlE StRinG'

if __name__ == "__main__":
    try:
        result = get_data()
        print(result)
    except MemoryError as e:
        print(f"System ran out of memory {MemoryError}.")
