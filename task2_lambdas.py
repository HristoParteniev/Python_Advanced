"""

1. You have the following sentence as string:
    sentence = 'This is a lAmBdA FuNction task'
 - Split the sentence into a list
 - Write a lambda function that accepts the list of words returns multiple lists
   each list containing the actual word, the word uppercase, the word lowercase
   , the length of the word
   return the results as a 2d list
Expected result:
[
    ['This', 'THIS', 'this', 4],
    ['is', 'IS', 'is', 2],
    ['a', 'A', 'a', 1],
    ['lAmBdA', 'LAMBDA', 'lambda', 6],
    ['FuNction', 'FUNCTION', 'function', 8],
    ['task', 'TASK', 'task', 4]
]

"""
if __name__ == '__main__':
    SENTENCE = 'This is a lAmBdA FuNction task'
    list_sentence = SENTENCE.split()

    final_list = []

    for word in range(len(list_sentence)):
        process_word = lambda a: [a[word], a[word].upper(), a[word].lower(), len(a[word])]
        final_list.append(process_word(list_sentence))

    print(final_list)

"""
2. You have the following sentence as string:
    sentence = 'This is a lAmBdA FuNction task'
 - Split the sentence into a list
 - write a series of functions that return a 
 string uppercase, lowercase and the length of a string
 - create a list of those functions 
 and use map to apply all functions to the sentence list
 return the results as a 2d list
 Expected result:
 [
 ['THIS', 'this', 4],
 ['IS', 'is', 2], ['A', 'a', 1],
 ['LAMBDA', 'lambda', 6],
 ['FUNCTION', 'function', 8],
 ['TASK', 'task', 4]
]
"""
if __name__ == '__main__':

    def to_upper(word):
        """ getting word to uppercase"""
        return word.upper()

    def to_lower(word):
        """ getting word to lowercase"""
        return word.lower()

    def get_len(word):
        """ getting word's length'"""
        return len(word)

    def process_word_func(word):
        return [to_upper(word), to_lower(word), get_len(word)]

final_result2 = list(map(process_word_func, list_sentence))
print(final_result2)

"""
3. You have the following lists
 a = [1, 11, 23, 44, 16]
 b = [2, 3, 5, 6, 7, 8, 44, 16]
 Using a lambda function return a list with values that are common between the 2 lists
 Expected results: [44, 16]
"""
if __name__ == '__main__':
    a = [1, 11, 23, 44, 16]
    b = [2, 3, 5, 6, 7, 8, 44, 16]

    common_elements = lambda list1, list2: [element for element in list1 if element in list2]
    final_result3 = common_elements(a,b)
    print(final_result3)
    
"""4. You have the following sentence as string:
    sentence = 'This is a lAmBdA FuNction task'
 - Split the sentence into a list
 Using a lambda function sort the list by the last
  character of each word alphabetically
 Expected result: ['a', 'lAmBdA', 'task', 'FuNction', 'This', 'is']"""

if __name__ == '__main__':
    SENTENCE2 = 'This is a lAmBdA FuNction task'
    task4_list = SENTENCE2.split()
    task4_lambda = lambda x: sorted(x, key=lambda word: word[-1])

    res = task4_lambda(task4_list)
    print(res)
