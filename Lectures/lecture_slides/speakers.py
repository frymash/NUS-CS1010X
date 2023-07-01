class Speaker(object):
    def say(self, stuff):
        print(stuff)

ah_beng = Speaker()
ah_beng.say("Hello World")
#ah_beng.dance()

class Lecturer(Speaker):
    def lecture(self, stuff):
        self.say(stuff)
        self.say("You should be taking notes")

seth = Lecturer()
seth.lecture("Java is easy")
seth.say("You have a quiz today")

class ArrogantLecturer(Lecturer):
    def __init__(self, favourite_phrase):
        self.favourite_phrase = favourite_phrase
    def say(self, stuff):
        super().say(stuff + self.favourite_phrase)

ben = ArrogantLecturer(" ... How cool is that?")
ben.say("We’d have a re-midterm tomorrow")
ben.lecture("Python is cool")

class Singer(object):
    def say(self, stuff):
        print("tra-la-la -- " + stuff)
    def sing(self):
        print("tra-la-la")

class SingingArrogantLecturer(ArrogantLecturer, Singer):
    def __init__(self, favourite_phrase):
        super().__init__(favourite_phrase)

ben = SingingArrogantLecturer(" ... How cool is that")
ben.say("We'd have a re-midterm tommorrow")
ben.lecture("Python is cool")
ben.sing()

class Vehicle:
    pass

class Truck(Vehicle):
    pass 

isinstance(Vehicle(), Vehicle)  # returns True
type(Vehicle()) == Vehicle      # returns True
isinstance(Truck(), Vehicle)    # returns True
type(Truck()) == Vehicle        # returns False
