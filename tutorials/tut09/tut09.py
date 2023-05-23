from hungry_games import *

# Q1

class Thing(object):
    def __init__(self, name):
        self.name = name
        self.owner = None
        
    def is_owned(self):
        # Python usually recommends the use of the 
        # 'is' keyword to check if something is equal to None.
        # 'is' checks if the identity of self.owner is None
        # If we use Boolean operators to check self.owner for
        # equivalence to None (such as "not None"), 
        # we may get different values if self.owner
        # is equal to a value that evals to False under a Boolean
        # operator. This is because None also evals to False
        # under a Boolean operator.
        return self.owner is not None
    
    def get_owner(self):
        return self.owner


# Q2

class Thing(object):
    def __init__(self, name):
        self.name = name
        self.owner = None
        self.place = None
        
    def is_owned(self):
        return self.owner is not None
    
    def get_owner(self):
        return self.owner
        
    def get_name(self):
        return self.name
        
    def get_place(self):
        return self.place


# Q3

# The issue with his code is that he did not inherit the self.place
# attribute from his superclass.

# Correction:
# class Thing(MobileObject):
#     def __init__(self, name):
#         super()__init__(name, None)
#         self.name = name
#         self.owner = None

# TA Yi Siong's answer:
# Thing's constructor did not invoke its superclass MobileObject's constructor.
# In general, it should invoke its superclass's constructor unless 
# there are exceptions.
# The consequence is that Thing has no attribute place, therefore
# its method get_place() will not work.
# This is because place is initialized by MobileObject's constructor.


# Q4

# Part 1
"""
Refer to the image tut09_task4_pt1 in this folder.

Notice that Python doesn't support private attributes.

"""

# Part 2
"""
My answer:
>>> ice_cream.get_name()
"ice_cream"
>>> ice_cream.get_place()
>>> ice_cream.get_owner()
<beng : Person>

TA Yi Siong's answer:
print(dir(ice_cream))
print(ice_cream.get_owner() == beng)

"""

# Part 3
"""
Both statements are actually legal in Python.

The last 2 statements assign an object to a field directly, hence they
break abstraction (and don't respect encapsulation).

The moral of the story is that fields in an object should only be modified
via the object's getter or setter methods. They should not be modified directly.

"""

# Part 4
# ice cream and rum and raisin are not the same object.
# They are different instances of the same class with the same attributes.

# Part 5
"""
Are burger1 and burger2 the same object?
Your answer: No

Would burger1 == burger2 evaluate to True?
Your answer: False

Different objects with the same attributes are still going to be unequal.
This is because Python checks for equality between 2 objects by checking if
their ids (locations in memory) are the same.

This also means that object1 == object2 and object1 is object2 work in
the exact same way (assuming both objects don't have an __eq__ method).

How would you do it?
Your answer: I would implement an __eq__ method in the class definition for 
Thing. The __eq__ method would be invoked every time 2 objects are compared
with the "==" operator. When 2 Thing objects (we'll call them T1 and T2)
are passed to this method, it should return True 
if T1.get_name() == T2.get_name() and T1.get_place() == T2.get_place().

def __eq__(self,other):
    cond = isinstance(other, Thing) and \
           self.get_name() == other.get_name() and \
           self.get_owner() == other.get_owner()
    return cond

"""

"""
Additional note:
- Although Java objects inherit the attributes of their superclass,
  the programmer will still need to call the constructor method
  of a parent class in the constructor method of a child class
  if the parent's constructor has user-defined parameters.
"""

# Extra stuff:
# Read up on:
# 1. method resolution order
# 2. diamond inheritance
class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")
        super().__init__()

class C(A):
    def __init__(self):
        print("C")
        super().__init__()

class D(B,C):
    def __init__(self):
        print("D")
        super().__init__()

print(D.__mro__)

# Output: D, B, C, A
# Python will actually make C the superclass of B
# in order to prevent method conflicts.