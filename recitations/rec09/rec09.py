# Question 1

class Food(object):
    def __init__(self, name, nutrition, good_until):
        self.name = name
        self.nutrition = nutrition
        self.good_until = good_until
        self.age = 0

    def sit_there(self, time):
        self.age += time

    def eat(self):
        return self.nutrition if self.age < self.good_until else 0
    

# Question 2

class AgedFood(Food):
    def __init__(self, name, nutrition, good_until):
        super.__init__(name, nutrition, good_until)
        self.good_after = 0

    def sniff(self):
        return self.age >= self.good_after
    
    def eat(self):
        return 0 if self.sniff() else Food.eat()
    

# Question 3

class VendingMachine(object):
    def __init__(self, name, nutrition, good_until):
        Food.__init__(name, nutrition, good_until)

    def sit_there(self, time):
        self.age += time / 2

    def sell_food(self, time):
        return Food(self.name, self.nutrition, self.good_until)
    

# Question 4

def mapn(fn, lsts):
    map_first_elts = fn(*tuple(map(lambda lst: lst[0], lsts)))
    if len(lsts[0]) == 1:
        return map_first_elts
    else:
        return map_first_elts \
               + mapn(fn, tuple(map(lambda lst: lst[1:], lsts)))

print(mapn(lambda x,y,z: (z, x+y), ((1,2,3), (4,5,6), ('first','second','third'))))
# Output: (('first', 5), ('second', 7), ('third', 9))