def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i !=0:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    print([x for x in factors])
    return #list(factors)

prime_factors(20633239)