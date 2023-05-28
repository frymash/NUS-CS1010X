FN_LOOKUP_TABLE = {"+": lambda x,y: x+y, "-": lambda x,y: x-y, \
                   "*": lambda x,y: x*y, "/": lambda x,y: x/y}

class Number(object):
    # complete the class definition #
    def __init__(self, num):
        self.num = num
        
    def value(self):
        return self.num
        
    def __oplookup(self, op, amt):
        """ (String, Number) -> Number
        """
        if type(amt.value()) != int or type(self.value()) != int:
            return Number("Undefined")
        else:
            return Number(FN_LOOKUP_TABLE[op](self.value(), amt.value()))
    
    def plus(self, num):
        """ (Number) -> Number
        """
        return self.__oplookup("+", num)
    
    def times(self, num):
        """ (Number) -> Number
        """
        return self.__oplookup("*", num)
    
    def divide(self, num):
        """ (Number) -> Number
        """
        if num.value() == 0:
            return Number("Undefined")
        else:
            return self.__oplookup("/", num)
    
    def minus(self, num):
        """ (Number) -> Number
        """
        return self.__oplookup("-", num)
        
    def spell(self):
        """ (None) -> String
        """
        small_digit_str = \
        {1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
         6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"
,
         11: "eleven", 12: "twelve"
        }
        
        teen_str = \
        {13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
         17: "seventeen", 18: "eighteen", 19: "nineteen"
        }
        
        ty_str = \
        {2: "twenty", 3: "thirty", 4: "fourty", 5: "fifty",
         6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"
        }
        
        
        def before_last_n_digits(num, n):
            result_str = str(num)[:-n]
            return int(result_str)
            
        def last_n_digits(num, n):
            result_str = str(num)[-n:]
            return int(result_str)

        def general_spell(number_to_spell, n, keyword1, keyword2):
            initial = Number(before_last_n_digits(self.value(), n))
            if not self.value() % number_to_spell:
                return f"{initial.spell()} {keyword1}"
            last_n = Number(last_n_digits(self.value(), n))
            return f"{initial.spell()} {keyword1}{keyword2} {last_n.spell()}"
        
        if self.value() > 10000000:
            return "really large number"
        elif self.value() < 0:
            raise ValueError("Number value is below 0.")
        elif 0 <= self.value() < 13:
            return small_digit_str[self.value()]
        elif self.value() < 20:
            return teen_str[self.value()]
        elif self.value() < 100:
            initial = before_last_n_digits(self.value(), 1)
            initial = ty_str[initial]
            last_1 = Number(last_n_digits(self.value(), 1))
            return f"{initial} {last_1.spell()}"           
        elif self.value() < 1000:
            return general_spell(100, 2, "hundred", " and")
        elif self.value() < 1000000:
            return general_spell(1000, 3, "thousand", ",")
        elif self.value() < 10000000:
            return general_spell(1000000, 6, "million", ",")
        else:
            raise ValueError("Number value is above 10 million.")
            
            
        
### Uncomment the lines below ###
    
elite_number=Number(1337)
good_day_number=Number(210792)
bigno=good_day_number.times(elite_number)

### Uncomment the lines above ###
