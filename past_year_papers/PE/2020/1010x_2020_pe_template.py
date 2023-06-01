##########################################
# Question 1a: Alien numbers [ 5 Marks ] #
##########################################

def dec_to_bin(n):
    """ (int) -> String

    Returns the binary representation of a decimal number n in string form
    """
    result = ""
    mapping = ("0","1")

    while n > 1:
        digit = str(n % 2)
        n //= 2
        result = digit + result
    result = str(n) + result
    return result

print(dec_to_bin(10))
print(dec_to_bin(5))

def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')

def ET_number(n, mapping):
    base = len(mapping)
    if n >= 1:
        return ET_number(n//base, mapping) + mapping[n % base]
    else:
        return ""

# def ET_number(n, mapping):
#     result = ""
#     base = len(mapping)

#     while n > base-1:
#         digit = mapping[n % base]
#         n //= base
#         result = digit + result
#     result = mapping[n] + result
#     return result

def test1a():
    print("=====Test 1a=====")
    # checking if simple decimal numbers can be produced
    print(ET_number(5, ('0','1','2','3','4','5','6','7','8','9')) == '5', \
          ET_number(5, ('0','1','2','3','4','5','6','7','8','9')))
    # checking for switching some digits
    print(ET_number(20, ('9','8','7','6','5','4','3','2','1','0')) == '79', \
          ET_number(20, ('9','8','7','6','5','4','3','2','1','0')))
    # checking for different bases
    print(ET_number(10, ('0','1','2','3','4','5')) == '14', \
          ET_number(10, ('0','1','2','3','4','5')) )
    print(ET_number(6, ('0','4')) == '440', \
          ET_number(6, ('0','4')))
    print(ET_number(5, ('1', '0')) == '010', \
          ET_number(5, ('1', '0')))
    print(ET_number(10, ('a', 'b', 'c')) == 'bab', \
          ET_number(10, ('a', 'b', 'c')))

# test1a()

#################################################
# Question 1b: Largest alien number [ 5 Marks ] #
#################################################

def deconvert(ET_number, mapping):
    result = 0
    base = len(mapping)
    first = ET_number[0]
    rest = ET_number[1:]
    result += mapping.index(first)
    for digit in rest:
        i = mapping.index(digit)
        result *= base
        result += i
    return result
    

def max_ET_number(ET_numbers, mapping):
    values = list(map(lambda et: deconvert(et, mapping), ET_numbers))
    max_value = max(values)
    max_index = values.index(max_value)
    return ET_numbers[max_index]

def test1b():
    print("=====Test 1b=====")
    # checking for normal decimal
    print(max_ET_number(('1','2','3','4','5'), ('0','1','2','3','4','5','6','7','8','9')) == '5')
    # checking for swapped digits
    print(max_ET_number(('12','34','42','58'), ('0','1','8','3','5','4','6','7','2','9')) == '42')
    print(max_ET_number(('19','20','21','22','23'), ('0','2','1','3','4','5','6','7','8','9')) == '19')
    # different bases
    print(max_ET_number(('14','15'),('0','1','2','3','5','4'))=='14')
    print(max_ET_number(('707','700','770'),('0','7'))=='770')
    print(max_ET_number(('0', '4', '40', '44', '400', '404', '440', '444', '4000', '4004', '4040'),('0','4'))=='4040')
    print(max_ET_number(('317','311','713','413'),('7','1','3','4'))=='413')
    print(max_ET_number(('aba', 'abc', 'ca', 'cb'), ('a', 'b', 'c')) == 'cb')

# test1b()

############################
# Question 2: Tesla stocks #
############################

import csv
import datetime

def read_csv(csvfilename):
    """
    Reads a csv file and returns a list of list
    containing rows in the csv file and its entries.
    """
    rows = []

    with open(csvfilename, 'r') as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows.append(row)
    return rows

######################################################
# Question 2a: Retrieving tweets by date [ 3 Marks ] #
######################################################
def get_tweet_by_date(date):
    pass

def test2a():
    print("=====Test 2a=====")
    print(get_tweet_by_date('12/21/2019') == ('Great show  https://t.co/12rguHHpgz', 'Holiday gift ideas https://t.co/uBBofvkYAI'))
    print(get_tweet_by_date('5/1/2020') == ('Now give people back their FREEDOM', 'I am selling almost all physical possessions. Will own no house.', 'Tesla stock price is too high imo', "And the rocket's red glare, the bombs bursting in air", 'Rage, rage against the dying of the light of consciousness'))
    print(get_tweet_by_date('12/12/2001') == ())
    print(get_tweet_by_date('5/21/2021') == ()) 

#test2a()

#############################################################
# Question 2b: Effect of tweets on stock prices [ 3 Marks ] #
#############################################################
def tweet_effect(date):
    pass

def test2b():
    print("=====Test 2b=====")
    print(tweet_effect('5/8/2013') == ("Just want to say thanks to customers & investors that took a chance on Tesla through the long, dark night. We wouldn't be here without you.", [55.790001, 69.400002, 76.760002, 87.800003]))
    print(tweet_effect('3/23/2017') == None)
    print(tweet_effect('7/14/2019') == ('To Infinity and Beyond! https://t.co/dgysTBqWfV', [253.5, 252.380005, 254.860001, 253.539993, 258.179993]))

#test2b()

##########################################
# Question 2c: Money tweets [ 4 Marks ]  #
##########################################

def money_tweets(start_date, end_date):
    pass           

def test2c():
    print("=====Test 2c=====")
    print(money_tweets('5/12/2020', '5/21/2020') == (('Ice cream sundae in a martini glass https://t.co/zAVFlOsYkM', 'Super exciting day coming up! https://t.co/7ZdFsJE9zR', 'https://t.co/lQWpSwtRj7'), 22.669983000000002))
    print(money_tweets('4/29/2020', '5/1/2020') == (('FREE AMERICA NOW', 'Give people their freedom back! https://t.co/iG8OYGaVZ0', 'Bravo Texas! https://t.co/cVkDewRqGv'), 99.19000299999993))

#test2c()

############################################
# Question 3: TOY TRAIN                    #
############################################

class carriage:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.attached = None

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_pos(self):
        return (self.get_x(), self.get_y())
    
    def attach(self, car):
        x_gap = abs(self.get_x() - car.get_x())
        y_gap = abs(self.get_y() - car.get_y())
        if (x_gap, y_gap) == (0,1) or (x_gap, y_gap) == (1,0):
            self.attached = car
            return "Attached."
        else:
            return "Can't attach."
    

class engine (carriage):
    def __init__(self, x, y):
        super().__init__(x,y)

    def move (self, track):
        """ (String) -> None or String
        """
        def move_attached(shift):
            """ ((int, int)) -> bool
            
                    
            Returns True if the move is successful
            (i.e. if the move can occur without causing collisions)
            """
            queue = [self]
            curr = self.attached

            while curr is not None:
                queue.append(curr)
                curr = curr.attached

            other_pos = list(map(lambda c: c.get_pos(), queue[1:].copy()))
            # print(f"other_pos: {other_pos}")

            # Check if the new pos of engine collides with any
            # other carriage
            x_pos = self.get_x()
            y_pos = self.get_y()
            new_head_pos = (x_pos+shift[0], y_pos+shift[1])
            # print(f"new_head_pos: {new_head_pos}")

            if new_head_pos in other_pos:
                return False
            else:
                curr = self.attached
                prev_x, prev_y = self.x, self.y

                for curr in queue:
                    # print(f"Curr old: {curr.get_pos()}")
                    curr.x, curr.y, prev_x, prev_y \
                    = prev_x, prev_y, curr.x, curr.y
                    other_pos.pop()
                    other_pos.append(curr)
                    # print(f"Curr new: {curr.get_pos()}")
                    # print()
                self.x, self.y = new_head_pos
                # print(f"Current queue: {[c.get_pos() for c in queue]}\n")
                # print(f"Actual new engine position: {self.get_pos()}")
                return True
                    
        if track == "":
            return None
        else:
            first_move = track[0]
            other_moves = track[1:]
            
            if first_move == "u":
                msg = move_attached((0,1))
            elif first_move == "d":
                msg = move_attached((0,-1))
            elif first_move == "r":
                msg = move_attached((1,0))
            elif first_move == "l":
                msg = move_attached((-1,0))

            if msg:
                return self.move(other_moves)
            else:
                return "Collision!"

def test3():
    print("=====Test 3=====")
    c0 = carriage(1,0)
    c1 = carriage(1,1)
    c2 = carriage(1,2)
    c3 = carriage(2,2)
    c4 = carriage(3,4)
    e  = engine(2,3)

    print("Checking for get_x and get_y functions")
    print(c1.get_x() == 1)
    print(c3.get_y() == 2)
    print()

    print("Checking for get_pos function")
    print(c0.get_pos() == (1,0))
    print()

    print("Attaching carriages together to build the train")
    print(e.attach(c3) == "Attached.")
    print(c3.attach(c2) == "Attached.")
    print(c2.attach(c1) == "Attached.")
    print()

    print("c1 and c4 are not adjacent")
    print(c1.attach(c4) == "Can't attach.")
    print(c1.attach(c0) == "Attached.")
    print()

    print("Checking for movement")
    print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) == ((2, 3), (2, 2), (1, 2), (1, 1), (1, 0)))
    print(e.move('uuu') == None)
    print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) == ((2, 6), (2, 5), (2, 4), (2, 3), (2, 2)))
    print(e.move('r') == None)
    print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) == ((3, 6), (2, 6), (2, 5), (2, 4), (2, 3)))
    print(e.move('uuuuuu') == None)
    print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) == ((3, 12), (3, 11), (3, 10), (3, 9), (3, 8)))
    print(e.move('rdll') == "Collision!")
    print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) == ((4, 11), (4, 12), (3, 12), (3, 11), (3, 10)))
    print(e.move('ldrr') == "Collision!")
    print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) == ((4, 11), (4, 12), (3, 12), (3, 11), (3, 10)))
    print(e.move('d') == None)
    print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) == ((4, 10), (4, 11), (4, 12), (3, 12), (3, 11)))

test3()