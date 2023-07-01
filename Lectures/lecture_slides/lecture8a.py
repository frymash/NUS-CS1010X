
#########################################################
#
# Example 1: Reversing a sequence
#
#########################################################

#version 0
##print("version 0")
##def reverse(seq):
##    if seq==():
##        return ()
##    else:
##        return reverse(seq[1:]) + seq[0]

##print(reverse( (1,2,3,4,5) ))

print("version 1: recursion")
def reverse(seq):
    if seq == ():
        return ()
    else:
        return reverse(seq[1:]) +  (seq[0],)

print(reverse( (1,2,3,4,5) ))


print("version 2: recursion")
def reverse(seq):
    if seq == ():
        return ()
    else:
        return  (seq[-1],)   + reverse(seq[:-1])

print(reverse( (1,2,3,4,5) ))

print("version 3: iteration (wrong)")
def reverse(seq):
    result = ()
    for item in seq:
        result += (item, )
    return result

print(reverse( (1,2,3,4,5) ))

print("version 3: iteration")
def reverse(seq):
    result = ()
    for item in seq:
        result = (item, ) + result
    return result

print(reverse( (1,2,3,4,5) ))

print("version 4: iteration - wrong")
def reverse(seq):
    result = ()
    for item in seq[-1::-1]:
        result = (item, ) + result
    return result

print(reverse( (1,2,3,4,5) ))

print("version 4: iteration")
def reverse(seq):
    result = ()
    for item in seq[-1::-1]:
        result += (item, )
    return result

print(reverse( (1,2,3,4,5) ))

##########################################################
#
# Abstraction like in Lecture 6
#
# accumulate
#
##########################################################
print(">>> accumulate")
def accumulate(fn, initial, seq):
    if seq == ():
        return initial
    else:
        return fn(seq[0], accumulate(fn, initial, seq[1:]))

def reverse (seq):
    return accumulate( lambda x,y: y + (x,), (), seq)

print("use accumulate to solve reserve:", reverse( (1,"a",3,4,5,6)))

def sum (seq):
    return accumulate(lambda x,y: x + y, 0, seq)

print("use accumulate to solve sum:", sum((1,2,3)))

##########################################################
#
# map
#
##########################################################

def map(fn, seq):
    if seq == ():
        return ()
    else:
        return (fn(seq[0]), ) + map(fn, seq[1:])

def seq_square(seq):
    return map(lambda x:x**2, seq)

def seq_double(seq):
    return map(lambda x:x+x, seq)

print("seq_square", seq_square((1,2,3,4,5)))
print("seq_double", seq_double((1,2,3,4,5)))

##########################################################
#
# filter
#
##########################################################
def filter(predicate, seq):
    if seq == ():
        return ()
    else:
        if predicate(seq[0]):
            return (seq[0],) + filter(predicate, seq[1:])
        else:
            return filter(predicate, seq[1:])

def seq_even(seq):
    return filter(lambda x: x%2==0, seq)

print("seq_even:", seq_even( (1,2,3,4,5,6)))

def seq_divisible(seq, d):
    return filter(lambda x: x%d==0, seq) 

print("seq_divisible by 4:", seq_divisible( (1,2,3,4,5,6, 12, 15, 16, 22), 4))

##########################################################
#
# enumerate
#
##########################################################
def enumerate_interval(low, high):
    return tuple(range(low, high+1))

print("sequence from 5 to 20:", enumerate_interval(5, 20))

print("even 5 to 20", seq_even(enumerate_interval(5, 20)), "or", filter( lambda x: x%2==0, enumerate_interval(5, 20)))


##########################################################
#
# Eg 2. sum_square_of_odd_integers
#
##########################################################
## Lecture 6: working with numbers not in sequence, but generated on the fly
def sum(term, a, next, b):
    if a > b:
        return 0
    else:
        return term(a) + sum(term, next(a), next, b)

def sum_square_of_odd_integers(a, b):
    return sum(lambda x: x**2, a, lambda x: x+2, b)

print("sum_square_of_odd_integer from Lecture 6:", sum_square_of_odd_integers(1, 10))
# the above is not for general sequence

def sum_square_of_odd_integers(a, b):
    return accumulate( lambda x,y: x+y , 0, 
                           map(lambda x: x**2, 
                               filter( lambda x: x%2, 
                                   enumerate_interval(a, b))))

print("from signal_processing view:", sum_square_of_odd_integers(1, 10))

##########################################################
#
# Eg 3. sum_of_even_fibs
#
##########################################################
def fib(n):
    if n<=1:
        return n
    prev1, prev2 = 1, 0
    for i in range(2, n+1):
        result = prev1 + prev2
        prev1, prev2 = result, prev1
    return result

def sum_of_even_fibs(n):
    return accumulate(lambda x,y: x+y, 0,
                      filter(lambda x: x%2 == 0,
                             map(fib,
                                 enumerate_interval(1, n))))

print("sum_of_even_fibs:", sum_of_even_fibs(30))

# iterative version
def even_fibs(n):
    result = 0
    for k in range(1, n+1):
        f = fib(k)
        if f%2==0:
            result += f
    return result
print("iteratively calculated:", even_fibs(30))


