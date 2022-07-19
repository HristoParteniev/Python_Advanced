"""imports"""
import random
import sys

def generate_rand_num():
    """Generating random number between 20 and 25"""
    return random.randrange(20,26)


permutatation_rows = generate_rand_num()
"""Using variable to store generated number"""

COUNTER = 0
FINISHED = False

def generate_permutations(a, n):
    """Permutations generation function"""
    global FINISHED
    if FINISHED:
        return
    if n == 0:
        print(''.join(a))
        global COUNTER
        COUNTER += 1
        if COUNTER == permutatation_rows:
            print(f'Permutations displayed: {COUNTER}')
            FINISHED = True
            return
    elif n != 0:
        for i in range(n):
            generate_permutations(a, n-1)
            j = 0 if n % 2 == 0 else i
            a[j], a[n] = a[n], a[j]
            generate_permutations(a, n-1)

if len(sys.argv) != 2:
    sys.stderr.write('Exactly one argument is required\n')
    sys.exit(1)

word = sys.argv[1]

generate_permutations(list(word), len(word)-1)
