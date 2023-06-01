#################
# Q1a - Shuffle #
#################

def shuffle(a, times):
    shuffled = []
    cut_at = len(a)//2 if len(a) % 2 == 0 else len(a)//2 +1
    first_half_a = a[:cut_at]
    second_half_a = a[cut_at:]
    # print(f"first half: {first_half_a}")
    # print(f"second half: {second_half_a}")
    while first_half_a != [] and second_half_a != []:
        shuffled.append(first_half_a.pop(0))
        shuffled.append(second_half_a.pop(0))
    shuffled.extend(first_half_a)
    shuffled.extend(second_half_a)    

    if times == 1:
        return shuffled
    else:
        return shuffle(shuffled, times-1)

def test1a():
    print('=== Q1a ===')
    print(shuffle([1, 2, 3, 4, 5, 6, 7, 8], 1)==[1, 5, 2, 6, 3, 7, 4, 8])
    print(shuffle([1, 2, 3, 4, 5, 6, 7, 8], 2)==[1, 3, 5, 7, 2, 4, 6, 8])
    print(shuffle([1, 2, 3, 4, 5, 6, 7, 8], 3)==[1, 2, 3, 4, 5, 6, 7, 8])
    print(shuffle([1, 2, 3, 4, 5, 6, 7], 1)==[1, 5, 2, 6, 3, 7, 4])
    print(shuffle([1, 2, 3, 4, 5, 6, 7], 2)==[1, 3, 5, 7, 2, 4, 6])
 
# test1a()


##########################
# Q1b - Back to Original #
##########################

from time import sleep

def back_to_original(a):
    """ List[int] -> int
    """
    count = 1
    curr = shuffle(a, 1)
    while curr != a:
        curr = shuffle(curr, 1)
        count += 1
        # print(f"curr: {curr}")
        # print(f"count: {count}")
        # sleep(1)
    return count

def test1b():
    print('=== Q1b ===')    
    print(back_to_original([1, 2, 3, 4, 5, 6, 7, 8])==3)
    print(back_to_original([1, 2, 3, 4, 5])==4)
    print(back_to_original([1, 1, 1, 1])==1)
 
# test1b()

##############
# Question 2 #
##############

import csv
from datetime import datetime

def read_csv(csvfilename):
	"""
	Reads a csv file and returns a list of list
	containing rows in the csv file and its entries.
	"""
	rows = []

	with open(csvfilename) as csvfile:
		file_reader = csv.reader(csvfile)
		for row in file_reader:
			rows.append(row)
	return rows

###############
# Question 2a #
###############

def get_dates_for_hashtag(filename, hashtag):
    pass    

def test2a():
    print("===2a===")
    tweets = get_dates_for_hashtag("donald-tweets.csv", "ObamacareFail")	
    tweets.sort()
    print(tweets == ['16-10-25', '16-10-29', '16-10-31'])
    tweets = get_dates_for_hashtag("donald-tweets.csv", "ElectionDay")
    tweets.sort()
    print(tweets == ['16-08-09', '16-11-08'])
    print(get_dates_for_hashtag("donald-tweets.csv", "China")==[]) 

#test2a()

###############
# Question 2b #
###############

def active_hour(filename,start_date,end_date):
    pass
    
def test2b():
    print("===2b===")
    print(active_hour("donald-tweets.csv", "16-11-06", "16-11-08")==[21])
    print(active_hour("donald-tweets.csv", "16-08-23", "16-11-06")==[1])
    print(active_hour("donald-tweets.csv", "16-11-06", "16-11-06")==[0, 23])

#test2b()

###############
# Question 2c #
###############

def top_k(filename,k,start_date,end_date):
    pass
    
def test2c():
    print("===2c===")
    tweets = ['TODAY WE MAKE AMERICA GREAT AGAIN!']
    print(top_k("donald-tweets.csv", 1, "16-11-08", "16-11-08")==tweets)
    tweets = ['The media is spending more time doing a forensic analysis of Melanias speech than the FBI spent on Hillarys emails.', 'Such a great honor to be the Republican Nominee for President of the United States. I will work hard and never let you down! AMERICA FIRST!', 'Here is my statement. https://t.co/WAZiGoQqMQ']
    print(top_k("donald-tweets.csv", 3, "15-10-13", "16-10-11")==tweets)
    print(top_k("donald-tweets.csv", 1, "16-11-18", "16-11-20")==[])

#test2c()


##############
# Question 3 #
##############

from collections import defaultdict
 
class Student:

    course_students = defaultdict(list)
    
    def __init__(self, name):
        self.name = name
        self.courseload = []

    def add_courses(self, *courses):
        for mod in courses:
            self.courseload.append(mod)
            Student.course_students[mod].append(self)

    def drop_courses(self, *courses):
        for mod in courses:
            if mod in self.courseload:
                self.courseload.remove(mod)
                Student.course_students[mod].remove(self)

    def get_courses(self):
        return self.courseload
            
    def common_courses(self,other):
        """ (Student) -> List[String]

        Returns the list of courses shared bt. other and self
        """
        own_courses = set(self.courseload)
        other_courses = set(other.courseload)
        result = own_courses.intersection(other_courses)
        return sorted(list(result))

    def is_coursemate(self,other):
        """ (Student) -> bool

        Returns True if other is a coursemate of self.
        """
        return self.common_courses(other) != []

    def friends(self):
        """ () -> Set[Student]
        
        Returns a set of students which the specified student
        shares classes with
        """
        own_friends = set()
        for mod in Student.course_students:
            students = Student.course_students[mod]
            if self in students:
                own_friends.update(students)
        own_friends.remove(self)
        return own_friends

    def common_friends_nonstr(self,other):
        """ (Student) -> List[String]

        Returns a list of the names of the students who are common friends between a
        student and the specified student. Common friends are students who
        take at least one course in common with each of them.
        Do note that Students cannot be their own friends.
        """
        own_friends = self.friends()
        other_friends = other.friends()
        if self is other:
            return []
        else:
            return own_friends.intersection(other_friends)
        
    def common_friends(self, other):
        return list(map(lambda student: student.name, list(self.common_friends_nonstr(other))))

    def six_degrees(self,other):
        """ (Student) -> int
        """
        visited = set()
        def helper(self, other):
            nonlocal visited
            if self.is_coursemate(other):
                return
            elif visited.issuperset(self.common_friends_nonstr(other)):
                return
            else:
                for friend in self.friends():
                    visited.add(friend)
                    helper(friend, other)
                    
        helper(self, other)
        return len(visited)
            
    
print("===3===")
benj = Student("Ben Junior")
benj.add_courses("CS1010", "CS1014", "CS2010", "CS2060", "CS2016", "GEM2455")
tanj = Student("Tan Junior")
tanj.add_courses("CS1010", "CS1014", "CS2010", "CS2060", "CS3243")
amanda = Student("Amanda See")
amanda.add_courses("GEM1010", "CS1014",  "CS1231", "CS2017", "GEM2455")
ad = Student("Ad Lee")
ad.add_courses("CS1010", "CS1000", "CS2010", "CS2040", "CS1207")
ayush = Student("Ayush")
ayush.add_courses("MA1016", "MA1014", "MA2050", "MA2016")


# sample execution
def test3():

    print(benj.is_coursemate(tanj))
    print(benj.is_coursemate(amanda))
    print(benj.is_coursemate(ad))
    print(benj.is_coursemate(ayush)==False)
    print(benj.common_courses(tanj)==['CS1010', 'CS1014', 'CS2010', 'CS2060'])
    print(benj.common_courses(amanda)==['CS1014', 'GEM2455']) # Found interesting girl in class!
    print(benj.common_courses(ad)==['CS1010', 'CS2010'])
    print(benj.common_courses(ayush)==[])

    amanda.drop_courses("CS1014", "GEM2455") # She disappears from our class :'(
    amanda.add_courses("CS3243")
    print(benj.is_coursemate(amanda)==False)
    print(benj.common_courses(amanda)==[]) # Girl disappears
    print(amanda.get_courses()==['GEM1010', 'CS1231', 'CS2017', 'CS3243']) # What is she taking now? 

    print(benj.six_degrees(amanda)==2) # How can we get to know her?
    print(benj.common_friends(amanda)==['Tan Junior'])
    print(amanda.common_courses(tanj)==['CS3243'])

    tanj.drop_courses("CS3243")
    print(benj.six_degrees(amanda)==None) 
    print(benj.common_friends(amanda)==[])

    amanda.add_courses("MA2050")
    ayush.add_courses("CS1000")
    print(benj.six_degrees(amanda)==3)

    
test3()
