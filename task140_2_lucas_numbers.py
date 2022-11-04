"""imports"""
import datetime
import time

start_time = None
end_time = None
elapsed_time = None

def log(original_function):
    """function being called from create_lucas_list function"""
    def new_function(*args):
        with open("log.txt", "a") as logfile:
            logfile.write(f"{datetime.datetime.now()}, Function: {original_function.__name__}\
            called with positional arguments {args}\
            , with output, elapsed time in ms: {original_function(args[0])} \n")
        return original_function(*args)
    return new_function


@log
def create_lucas_list(n):
    """func creating lucas list"""
    if n < 2:
        return n
    sequence = [2, 1]

    global start_time, end_time, elapsed_time
    start_time = time.time()
    for i in range(2, n + 1):

        sequence.append(sequence[i - 1] + sequence[i - 2])

    end_time = time.time()
    elapsed_time = (end_time - start_time) / 1000
    return sequence[n], elapsed_time
    #return [n for n in sequence]

test = create_lucas_list(10000)
print(test)
