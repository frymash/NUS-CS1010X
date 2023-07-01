''' select the portions of test code and
    press Alt+3 to comment or
    press Alt+4 to uncomment '''

'''recursive fact '''
def factorial(n):
    if (n == 1):
        return 1
    else:
        return n * factorial(n - 1)


    
##for i in range(1, 10):
##    print(factorial(i))

''' iterative for factorial '''
def factorial(n):
    product = 1
    for counter in range(2, n+1):  
        product = product * counter

    return product


##for i in range(1, 10):
##    print(factorial(i))


''' iterative while factorial '''
def factorial(n):
    product, counter = 1, 1
    while counter <= n:
        product = product * counter
        counter = counter + 1
    return product

##for i in range(1, 10):
##    print(factorial(i))
