''' select the portions of test code and
    press Alt+3 to comment or
    press Alt+4 to uncomment '''

''' iterative while fibonacci '''
def fib(n):
    counter = 0
    a, b = 1, 0
    while counter < n:
        a, b = a+b, a
        counter = counter + 1
    return b


##for i in range(10):
##    print(fib(i))

''' recursive fibonacci '''
def fib(n):
   if (n == 0): return 0
   elif (n == 1): return 1
   else: return (fib(n - 1) + 
                 fib(n - 2)) 

##for i in range(10):
##    print(fib(i))
