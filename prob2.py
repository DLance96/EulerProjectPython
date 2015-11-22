# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def fib(number):
    if (number == 1 or number == 0):
        return 1
    if (number == 2):
        return 2
    else:
        return fib(number - 1) + fib(number - 2)

def fib_lessthan(upper):
    max_fib = 0;
    while ( fib( max_fib ) < upper ):
        max_fib += 1
    return max_fib

def sum_even_fib(max_fib):
    fib_sum = 0
    current_fib = 0
    for x in range (1, max_fib):
        current_fib = fib( x )
        if ( current_fib % 2 == 0 ):
            fib_sum += current_fib
    return fib_sum

print ( sum_even_fib( fib_lessthan( 4000000 )  ) )
