# Python fails all 3 aspects of OOP:
# 1. Encapsulation - Java protects object implementation details
#    with access level keywords (public, private, protected)
# 2. Inheritance - Python doesn't have explicit attribute inheritance.
#    A child class will only inherit methods from its parent class.
#    For the child class to inherit its parent class's attributes, it
#    will need to call its parent class's __init__ method.
# 3. Polymorphism - no method overloading in Python;
#    you cannot call multiple methods of the same name.

# Question 1
# object is the mother of all classes -- all objects are derived from it.
# By convention, the 1st parameter of all object methods would be named "self".
# However, it will still work just fine even if it is given any other name.

# Class variables aren't private by default.

# 2 types of relationships between objects:
# 1. is-a (instance of child class is also an instance of a parent class)
# 2. has-a

class Food(object):
    num_of_objects = 0 # Class variable
    
    def __init__(self, name, nutrition, good_until):
        self.name = name
        self.nutrition = nutrition
        self.good_until = good_until
        self.age = 0
        Food.num_of_objects += 1

    def sit_there(self, time):
        self.age += time

    def eat(self):
        return self.nutrition if self.age < self.good_until else 0
    

# Question 2

class AgedFood(Food):
    def __init__(self, name, nutrition, good_until, good_after):
        super().__init__(name, nutrition, good_until)
        self.good_after = good_after

    def sniff(self):
        return self.age >= self.good_after
    
    def eat(self):
        return 0 if self.sniff() else super().eat()
    

# Question 3

class VendingMachine(object):
    def __init__(self, name, nutrition, good_until):
        self.name = name
        self.nutrition = nutrition
        self.good_until = good_until
        self.age = 0

    def sit_there(self, time):
        self.age += time / 2

    def sell_food(self, time):
        return Food(self.name, self.nutrition, self.good_until)
      # f = Food(self.name, self.nutrition, self.good_until)
      # f.age = self.age
      # return f
    

# Question 4

def mapn(fn, lsts):
    map_first_elts = fn(*tuple(map(lambda lst: lst[0], lsts)))
    if len(lsts[0]) == 1:
        return map_first_elts
    else:
        return map_first_elts \
               + mapn(fn, tuple(map(lambda lst: lst[1:], lsts)))

"""
Prof's solutions:

def mapn(fn, tp):
    return tuple(map(fn, *tp))

def mapn(fn, tp):
    if len(tp[0]) == 0:
        return ()
    else:
	item = tuple(map(lambda x: x[0], tp))
	rest = tuple(map(lambda x: x[1:], tp))
	return (fn(*item),) + mapn(fn, rest)

def mapn(fn, tp):
    if len(tp[0]) == 0:
        return ()
    elif len(tp) == 1:
        return (fn(tp[0][0]),) + mapn(fn, (tp[0][1:],))
    else:
	item = mapn(lambda x: x[0], (tp,))
	rest = mapn(lambda x: x[1:], (tp,))
	return (fn(*item),) + mapn(fn, rest)


Prof's challenge:

def mapn(fn, *tp):
    if len(tp[0]) == 0:
        return ()
    elif len(tp) == 1:
        return (fn(tp[0][0]),) + mapn(fn, tp[0][1:])
    else:
	item = mapn(lambda x: x[0], tp)
	rest = mapn(lambda x: x[1:], tp)
	return (fn(*item),) + mapn(fn, *rest)

"""

print(mapn(lambda x,y,z: (z, x+y), ((1,2,3), (4,5,6), ('first','second','third'))))
# Output: (('first', 5), ('second', 7), ('third', 9))