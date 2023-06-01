##########################################
# Question 1a: Alien numbers [ 5 Marks ] #
##########################################

def ET_number(num, mapping):
    # One of the corner cases is when we need to generate the number 0
    if num == 0:
        return mapping[0]
    base = len(mapping)
    alien_num = ''
    count = 0
    while num > 0:
        alien_num = mapping[num%base] + alien_num
        num = num//base
        count += 1
    return alien_num

def test1a():
    print("=====Test 1a=====")
    # checking if simple decimal numbers can be produced
    print(ET_number(5, ('0','1','2','3','4','5','6','7','8','9')) == '5')
    # checking for switching some digits
    print(ET_number(20, ('9','8','7','6','5','4','3','2','1','0')) == '79')
    # checking for different bases
    print(ET_number(10, ('0','1','2','3','4','5')) == '14')
    print(ET_number(6, ('0','4')) == '440')
    print(ET_number(5, ('1', '0')) == '010')
    print(ET_number(10, ('a', 'b', 'c')) == 'bab')

def test1a_e():
    print("=====Test 1a Evaluation=====")
    # checking for 0 case [0.5 mark each] 
    print(ET_number(0, ('1', '2', '3')) == '1') 
    # checking if simple decimal numbers can be produced [0.5 mark each]
    print(ET_number(5, ('0','1','2','3','4','5','6','7','8','9')) == '5')
    print(ET_number(100, ('0','1','2','3','4','5','6','7','8','9')) == '100')
    # checking for switching some digits [0.5 mark each]
    print(ET_number(20, ('9','8','7','6','5','4','3','2','1','0')) == '79')
    # checking for different bases and characters [0.5 mark each]
    print(ET_number(4, ('1','2','9')) == '22')
    print(ET_number(5, ('1', '0')) == '010')
    print(ET_number(10, ('a', 'b', 'c')) == 'bab')
    print(ET_number(1736, ('?', 'a', '+', '0')) == 'a+0?+?')
    # checking for repeating characters [0.5 mark each]
    print(ET_number(12, ('a', 'a')) == 'aaaa')
    print(ET_number(10, ('a', 'a', 'c')) == 'aaa')

test1a()
test1a_e()

#################################################
# Question 1b: Largest alien number [ 5 Marks ] #
#################################################

# A simple helper function to return the integer value of a alien number
def val(alien_num, digits):
        val = 0
        for i in alien_num:
            val = val*len(digits) + digits[i]
        return val

def max_ET_number(ET_numbers, mapping):
    max_index = 0
    digits = {}
    count = 0
    for num in mapping:
        digits[num] = count
        count += 1
    # we are going to track the max ET number via its index
    index = 0
    for i in ET_numbers:
        if val(ET_numbers[max_index], digits) < val(i, digits):
            max_index = index
        index += 1
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

def test1b_e():
    print("=====Test 1b Evaluation=====")
    # checking for normal decimal [0.5 ark each]
    print(max_ET_number(('25','32','71','54','51'), ('0','1','2','3','4','5','6','7','8','9')) == '71')
    print(max_ET_number(('01', '10', '20', '02'), ('0','1','2','3','4','5','6','7','8','9')) == '20')
    # checking for swapped digits [0.5 mark each]
    print(max_ET_number(('12','34','42','58'), ('0','1','8','3','5','4','6','7','2','9')) == '42')
    print(max_ET_number(('19','20','21','22','23'), ('0','2','1','3','4','5','6','7','8','9')) == '19')
    print(max_ET_number(('27', '35', '33', '22'), ('2', '7', '5', '3')) == '33')
    # different bases and characters [0.5 mark each]
    print(max_ET_number(('14','05'),('1','2', '0', '3','5','4'))=='05')
    print(max_ET_number(('707','700','770'),('7','0'))=='700')
    print(max_ET_number(('0', '4', '40', '44', '400', '404', '440', '444', '4000', '4004', '4040'),('0','4'))=='4040')
    print(max_ET_number(('317','311'),('7','1','3','4'))=='311')
    # handling repeating digits [0.5 mark each]
    #print(max_ET_number(('e', 'eee', 'eeee'), ('e', 'e')) == 'eeee')

test1b()
test1b_e()

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
    tweets = read_csv('tweets.csv')
    tweet = ()
    d = datetime.datetime.strptime(date, '%m/%d/%Y')
    for t in tweets[1:]:
        dd = datetime.datetime.strptime(t[6], '%m/%d/%Y')
        if dd == d:    
            tweet += (t[2],) 
    return tweet

def test2a():
    print("=====Test 2a=====")
    print(get_tweet_by_date('12/21/2019') == ('Great show  https://t.co/12rguHHpgz', 'Holiday gift ideas https://t.co/uBBofvkYAI'))
    print(get_tweet_by_date('5/1/2020') == ('Now give people back their FREEDOM', 'I am selling almost all physical possessions. Will own no house.', 'Tesla stock price is too high imo', "And the rocket's red glare, the bombs bursting in air", 'Rage, rage against the dying of the light of consciousness'))
    print(get_tweet_by_date('12/12/2001') == ())
    print(get_tweet_by_date('5/21/2021') == ()) 

def test2a_e():
    print("=====Test 2a Evaluation=====")
    # retrieving single tweets correctly [ 0.5 Marks each ]
    print(get_tweet_by_date('12/5/2012') == ('Interesting possible answer to the Fermi Paradox http://t.co/ASZdxBAl',))
    # retrieving multiple tweets correctly [ 0.5 Marks each ]
    print(get_tweet_by_date('4/1/2013') == ('First profitable Q for Tesla thanks to awesome customers & hard work by a super dedicated team http://t.co/njumz2SDmx', "To be clear, Tesla is in California, so it is not April Fool's yet! Also, some may differ, but imo the Tues news is arguably more important."))
    print(get_tweet_by_date('4/8/2016') == ('Screen cap from the stern cam of droneship "Of Course I Still Love You" https://t.co/4rGOJMTzVn', 'SolarCity panels produce enough zero carbon energy to charge entire Tesla fleet https://t.co/bn4LRzii1V'))
    print(get_tweet_by_date('6/29/2016') == ('My son recently asked what my favorite animal was. Well, of course  https://t.co/hpTniMe1mF', 'Thoughtful analysis of the Tesla/SolarCity merger by @tsrandall https://t.co/4Ba3px7hb8'))
    # retriveing tweets from invalid dates [ 0.5 Marks each ]
    print(get_tweet_by_date('1/1/2001') == ())
    print(get_tweet_by_date('7/24/2023') == ())

test2a()
test2a_e()

#############################################################
# Question 2b: Effect of tweets on stock prices [ 3 Marks ] #
#############################################################
def tweet_effect(date):
    stock  = read_csv("TSLA.csv")
    d = datetime.datetime.strptime(date, "%m/%d/%Y")
    ans = ()
    tweet = get_tweet_by_date(date)
    if tweet == ():
        return 
    stock_prices = []
    end_date = d + datetime.timedelta(days=5)
    for s in stock[1:]:
        cur_date = datetime.datetime.strptime(s[0], "%m/%d/%Y")
        if  d <= cur_date <= end_date:
            stock_prices.append(float(s[1])) 
        if cur_date > end_date:
            break
    ans = tweet + (stock_prices,)
    return ans

def test2b():
    print("=====Test 2b=====")
    print(tweet_effect('5/8/2013') == ("Just want to say thanks to customers & investors that took a chance on Tesla through the long, dark night. We wouldn't be here without you.", [55.790001, 69.400002, 76.760002, 87.800003]))
    print(tweet_effect('3/23/2017') == None)
    print(tweet_effect('7/14/2019') == ('To Infinity and Beyond! https://t.co/dgysTBqWfV', [253.5, 252.380005, 254.860001, 253.539993, 258.179993]))

def test2b_e():
    print("=====Test 2b Evaluation=====")
    #Checking normal dates (with valid tweets) [ 0.5 Marks each ]
    print(tweet_effect('3/23/2018') == ('No technology is too advanced for The Boring Company! https://t.co/r3EJYpcpkO', [301.540009, 304.179993, 279.179993, 257.779999]))    
    print(tweet_effect('5/1/2020') == ('Now give people back their FREEDOM', 'I am selling almost all physical possessions. Will own no house.', 'Tesla stock price is too high imo', "And the rocket's red glare, the bombs bursting in air", 'Rage, rage against the dying of the light of consciousness', [701.320007, 761.190002, 768.210022, 782.580017]))
    print(tweet_effect('12/12/2012') == ('Tesla articles 30 mins apart: "This Stock is Screaming Buy" http://t.co/jb9DCw4s and "This Stock Could Get DESTROYED" http://t.co/dqxTK4LJ', 'Cool video recap of the big events of the year by Google #Zeitgeist2012 http://t.co/FZjy4vkL', [35.259998, 33.610001, 33.810001, 34.400002]))
    # Checking for invalid dates or dates without any tweets [ 0.5 Marks each]
    print(tweet_effect('1/1/2018') == None)
    print(tweet_effect('7/23/2020') == None)
    print(tweet_effect('1/3/1999') == None)

test2b()
test2b_e()

##########################################
# Question 2c: Money tweets [ 4 Marks ]  #
##########################################

def date_to_string(date):
    return str(date.month) + "/" + str(date.day) + "/" + str(date.year)

def money_tweets(start_date, end_date):
    change = -1
    start = datetime.datetime.strptime(start_date, "%m/%d/%Y")
    end = datetime.datetime.strptime(end_date, "%m/%d/%Y")
    cur_date = start
    while cur_date <= end:
        effect = tweet_effect(date_to_string(cur_date))
        if effect:
            prices = effect[-1]
            delta = max(prices) - min(prices)
            if delta > change:
                change = delta
                tweet = effect[:-1] 
        cur_date = cur_date + datetime.timedelta(days=1)
    if change == -1:
        return
    else:
        return (tweet, change)           


def test2c():
    print("=====Test 2c=====")
    print(money_tweets('5/12/2020', '5/21/2020') == (('Ice cream sundae in a martini glass https://t.co/zAVFlOsYkM', 'Super exciting day coming up! https://t.co/7ZdFsJE9zR', 'https://t.co/lQWpSwtRj7'), 22.669983000000002))
    print(money_tweets('4/29/2020', '5/1/2020') == (('FREE AMERICA NOW', 'Give people their freedom back! https://t.co/iG8OYGaVZ0', 'Bravo Texas! https://t.co/cVkDewRqGv'), 99.19000299999993))

def test2c_e():
    print("=====Test 2c Evaluation=====")
    # time span with no tweets [ 0.5 Marks each ]
    print(money_tweets('11/7/2016', '11/12/2016') == None)
    print(money_tweets('1/1/2003', '3/2/2003') == None)
    # time span with multiple tweets [ 1 Mark each]
    print(money_tweets('4/29/2020', '5/1/2020') == (('FREE AMERICA NOW', 'Give people their freedom back! https://t.co/iG8OYGaVZ0', 'Bravo Texas! https://t.co/cVkDewRqGv'), 99.19000299999993))
    print(money_tweets('3/12/2020', '3/20/2020') == (('Fear is the mind-killer',), 83.85000599999995))
    print(money_tweets('3/4/2012', '3/25/2012') == (('Interesting interview with Vinge about superhuman AI and optimistic apocalypses http://t.co/TVoqGpEG',), 3.859997))

test2c()
test2c_e()

############################################
# Question 3: TOY TRAIN                    #
############################################

class carriage:
    # simple carriage object. keeps track of x, y and the carriage that is attached behind it.
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.attached_car = None
    def get_x(self):
        return self.pos_x
    def get_y(self):
        return self.pos_y
    def get_pos(self):
        return (self.pos_x, self.pos_y)
    def attach(self, car):
        if self.pos_x == car.get_x() and 1 >= self.pos_y - car.get_y() >= -1:
            self.attached_car = car
            return "Attached."
        elif self.pos_y == car.get_y() and 1 >= self.pos_x - car.get_x() >= -1:
            self.attached_car = car
            return "Attached."
        else:
            return "Can't attach."
    # a simple util functions we'll be using for collision detection and movement later
    # get_all_pos calls get_all_pos on all carriages recursively and returns a tuple of tuples with all their locations
    def get_all_pos(self):
        if self.attached_car:
            return ((self.pos_x, self.pos_y),) + self.attached_car.get_all_pos()
        else:
            return ((self.pos_x, self.pos_y),)
    # the function pull updates the location of the carriage to the new location, and assigns the carriage it is
    # pulling its old location
    def pull(self, new_x, new_y):
        if self.attached_car:
            self.attached_car.pull(self.pos_x, self.pos_y)
        self.pos_x = new_x
        self.pos_y = new_y

class engine (carriage):
    def __init__(self, x, y):
        carriage.__init__(self, x, y)
    def move (self, track):
        all_pos = ()
        for direction in track:
            all_pos = self.get_all_pos()
            if direction == 'u':
                if (self.pos_x, self.pos_y+1) in all_pos:
                    return "Collision!"
                else:
                    if self.attached_car:
                        self.attached_car.pull(self.pos_x, self.pos_y)
                    self.pos_y += 1 
            elif direction == 'd':
                if (self.pos_x, self.pos_y-1) in all_pos:
                    return "Collision!"
                else:
                    if self.attached_car:
                        self.attached_car.pull(self.pos_x, self.pos_y)
                    self.pos_y -= 1 
            elif direction == 'r':
                if (self.pos_x+1, self.pos_y) in all_pos:
                    return "Collision!"
                else:
                    if self.attached_car:
                        self.attached_car.pull(self.pos_x, self.pos_y)
                    self.pos_x += 1 
            elif direction == 'l':
                if (self.pos_x-1, self.pos_y) in all_pos:
                    return "Collision!"
                else:
                    if self.attached_car:
                        self.attached_car.pull(self.pos_x, self.pos_y)
                    self.pos_x -= 1 

def test3():
    print("=====Test 3=====")
    c0 = carriage(1,0)
    c1 = carriage(1,1)
    c2 = carriage(1,2)
    c3 = carriage(2,2)
    c4 = carriage(3,4)
    e  = engine(2,3)

    # Checking for get_x and get_y functions
    print(c1.get_x() == 1)
    print(c3.get_y() == 2)
    # Checking for get_pos function
    print(c0.get_pos() == (1,0))

    # Attaching carraiges together to build the train
    print(e.attach(c3) == "Attached.")
    print(c3.attach(c2) == "Attached.")
    print(c2.attach(c1) == "Attached.")

    # c1 and c4 are not adjacent
    print(c1.attach(c4) == "Can't attach.")
    
    print(c1.attach(c0) == "Attached.")

    # Checking for movement
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

    #print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()))

def test3_e():
    print("=====Test 3 Evaluation=====")
    # PLacing carriages in the following formation:

    #    ----------------------------------------------
    # 5  |     |     |     |     |     |     |     |
    #    ----------------------------------------------
    # 4  |  C6 |     |  E  |  C0 |     |     |     |
    #    ----------------------------------------------
    # 3  |  C7 |     |     |  C1 |     |     |     |
    #    ----------------------------------------------
    # 2  |     |     |     |  C2 |  C3 |     |     |
    #    ----------------------------------------------
    # 1  |     |  C8 |     |     |  C4 | C5  |     |
    #    ----------------------------------------------
    # 0  |     |     |     |     |     |     |     |
    #    ----------------------------------------------
    #       0     1     2     3     4     5     6

    # Checking for correct carriage creation and placement [2]
    e = engine(2,4)
    c0 = carriage(3,4)
    c1 = carriage(3,3)
    c2 = carriage(3,2)
    c3 = carriage(4,2)
    c4 = carriage(4,1)
    c5 = carriage(5,1)
    c6 = carriage(0,4)
    c7 = carriage(0,3)
    c8 = carriage(1,1)

    pos = (e.get_pos(), c0.get_pos(), c1.get_pos(), c2.get_pos(), c3.get_pos(), c4.get_pos(), c5.get_pos(), c6.get_pos(), c7.get_pos(), c8.get_pos())
    ans = ((2,4), (3, 4), (3, 3), (3, 2), (4, 2), (4, 1), (5, 1), (0, 4), (0, 3), (1, 1))
    print(pos==ans)
    coord = (c0.get_x(), c7.get_y(), c4.get_y(), c4.get_x())
    print(coord == (3, 3, 1, 4))

    # Checking for attachment condition [2]    
    print(e.attach(c0) == 'Attached.')
    print(c0.attach(c1) == 'Attached.')
    print(c1.attach(c2) == 'Attached.')
    print(c2.attach(c3) == 'Attached.')
    print(c3.attach(c4) == 'Attached.')
    print(c4.attach(c5) == 'Attached.')

    print(c6.attach(c7) == 'Attached.')

    print(c8.attach(c7) == "Can't attach.")
    print(c5.attach(c6) == "Can't attach.")

    # Checking for movement [3]
    print(e.move('u') == None)
    pos = (e.get_pos(), c0.get_pos(), c1.get_pos(), c2.get_pos(), c3.get_pos(), c4.get_pos(), c5.get_pos(), c6.get_pos(), c7.get_pos(), c8.get_pos())
    ans = ((2, 5), (2, 4), (3, 4), (3, 3), (3, 2), (4, 2), (4, 1), (0, 4), (0, 3), (1, 1))
    print(pos==ans)

    print(e.move('llluluurr') == None)
    pos = (e.get_pos(), c0.get_pos(), c1.get_pos(), c2.get_pos(), c3.get_pos(), c4.get_pos(), c5.get_pos(), c6.get_pos(), c7.get_pos(), c8.get_pos())
    ans = ((0, 8), (-1, 8), (-2, 8), (-2, 7), (-2, 6), (-1, 6), (-1, 5), (0, 4), (0, 3), (1, 1))
    print(pos==ans)

    print(e.move('rulurululld') == None)
    pos = (e.get_pos(), c0.get_pos(), c1.get_pos(), c2.get_pos(), c3.get_pos(), c4.get_pos(), c5.get_pos(), c6.get_pos(), c7.get_pos(), c8.get_pos())
    ans = ((-2, 11), (-2, 12), (-1, 12), (0, 12), (0, 11), (1, 11), (1, 10), (0, 4), (0, 3), (1, 1))
    print(pos==ans)    

    # Checking for collision [3]

    print(e.move('rdlu')=='Collision!')
    pos = (e.get_pos(), c0.get_pos(), c1.get_pos(), c2.get_pos(), c3.get_pos(), c4.get_pos(), c5.get_pos(), c6.get_pos(), c7.get_pos(), c8.get_pos())
    ans = ((-2, 10), (-1, 10), (-1, 11), (-2, 11), (-2, 12), (-1, 12), (0, 12), (0, 4), (0, 3), (1, 1))
    print(pos==ans)

    print(e.move('druu')=='Collision!')
    pos = (e.get_pos(), c0.get_pos(), c1.get_pos(), c2.get_pos(), c3.get_pos(), c4.get_pos(), c5.get_pos(), c6.get_pos(), c7.get_pos(), c8.get_pos())
    ans = ((-1, 9), (-2, 9), (-2, 10), (-1, 10), (-1, 11), (-2, 11), (-2, 12), (0, 4), (0, 3), (1, 1))
    print(pos==ans)

    print(e.move('u')=='Collision!')
    pos = (e.get_pos(), c0.get_pos(), c1.get_pos(), c2.get_pos(), c3.get_pos(), c4.get_pos(), c5.get_pos(), c6.get_pos(), c7.get_pos(), c8.get_pos())
    ans = ((-1, 9), (-2, 9), (-2, 10), (-1, 10), (-1, 11), (-2, 11), (-2, 12), (0, 4), (0, 3), (1, 1))
    print(pos==ans)

test3()
test3_e()

    

