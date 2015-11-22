# Sum the multiples of 3 and 5 between 1 and 1000
# https://projecteuler.net/problem=1

def make_3_5_list(upper):
    mult_list = []
    for x in range(0, upper):
        if (x % 3 == 0 or x % 5 == 0):
            mult_list.append(x)
    return mult_list

def sum_list(alist):
    sum = 0
    for x in alist:
        sum = sum + x
    return sum

print ( sum_list( make_3_5_list(1000) ) ) 
