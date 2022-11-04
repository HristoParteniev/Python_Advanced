# """task140_4 calculate lucas number's prime factors"""
# def prime_factors(function):
#     """feeding create_lucas_list func to this one"""
#     def wrapper(*args):
#         i = 2
#         factors = []
#         n = function(*args)
#         while i * i <= n:
#             if n % i !=0:
#                 i += 1
#             else:
#                 n //= i
#                 factors.append(i)
#         if n > 1:
#             factors.append(n)
#         return [x for x in factors]
#     return wrapper

# @prime_factors
def create_lucas_list(m):
    """func creating lucas list"""
    if m < 2:
        return m
    sequence = [2, 1]

    for i in range(2, m + 1):

        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence[m]
    
l_60 = create_lucas_list(60)
l_61 = create_lucas_list(61)

print(f"{l_60}: L(60)")
print(f"{l_61}: L(61)")

