from icecream import ic

# Question 1
def foo():
    return 10

bar = foo() + foo()
print(f"bar = {bar}")


# Question 3
def triple(amt):
    return 3 * amt


# Question 5
def square(x):
    return x * x

def mean(x, y):
    return (x + y) / 2

def variance(x, y):
    return mean(square(x), square(y)) - square(mean(x,y))

ic(variance(1, 5)) # Answer: 4.0
ic(variance(2, 4)) # Answer: 1.0
ic(variance(3, 3)) # Answer: 0.0
ic(variance(5, 1)) # Answer: 4.0


# Question 7
def greet(name, language):
    if language == 'English':
        return "Nice to meet you " + name
    elif language == 'Klingon':
        return "nuqneH " + name
    elif language == 'Elvish':
        return "Gi suilon " + name

ic(greet('Ben', 'English')) # Answer: Nice to meet you Ben
ic(greet('Okrand', 'Klingon')) # Answer: nuqneH Okrand
ic(greet('Elrond', 'Elvish')) # Answer: Gi suilon Elrond


# Question 8
def area_rect(x,y):
    return x * y

def area_square(x):
    if x <= 0:
        return 0
    else:
        return area_rect(x, x)


# Question 9
def is_odd(x):
    return x % 2 != 0
    
def is_negative(x):
    return x < 0
    
def is_even_and_positive(x):
    return x % 2 == 0 and x > 0
