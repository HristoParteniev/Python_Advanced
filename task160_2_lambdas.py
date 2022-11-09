# Map a lambda which applies the logistic function to the list [-3, -5, 1, 4] . 
# Round each number to 4 decimal places. (ermm…. that's two nested maps) 
import math

numbers = [-3, -5, 1, 4]
logistic_func_list = list(map(lambda x: round(1 / (1 + math.exp(-x)), 4), numbers))

print(logistic_func_list)

# for x in numbers:        
#     sigmoid_lambda = lambda x: round(1 / (1 + math.exp(-x)), 4)

#     print(sigmoid_lambda(x))