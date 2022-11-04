"""creating func to calc average"""
def calc_avg(*args):
    """calculationg average value of inputs"""
    sum_nums = 0
    for number in args:
        sum_nums += number

    result = round(sum_nums / len(args),2)
    return result

print(calc_avg(10.8, 22, 37.2))
