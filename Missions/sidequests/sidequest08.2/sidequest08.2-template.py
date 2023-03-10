#
# CS1010X --- Programming Methodology
#
# Sidequest 08.2 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

possible_birthdays = (('May', '15'),
                      ('May', '16'),
                      ('May', '19'),
                      ('June', '17'),
                      ('June', '18'),
                      ('July', '14'),
                      ('July', '16'),
                      ('August', '14'),
                      ('August', '15'),
                      ('August', '17'))

# Albert and Bernard just became friends with Cheryl,
# and they want to know when her birthday is.
# Cheryl gave Albert and Bernard a tuple of 10 possible dates.

#############
# Task 1(a) #
#############

def unique_day(day, possible_birthdays):
    is_unique = False
    for _, possible_day in possible_birthdays:
        if day == possible_day:
            if is_unique:
                is_unique = False
                return is_unique
            else:
                is_unique = True
    return is_unique
            
            

print("\n## Task 1a ##")
print(unique_day("16", possible_birthdays)) # False
print(unique_day("17", possible_birthdays)) # False
print(unique_day("18", possible_birthdays)) # True
print(unique_day("19", possible_birthdays)) # True

#############
# Task 1(b) #
#############

def unique_month(month, possible_birthdays):
    is_unique = False
    for possible_month, _ in possible_birthdays:
        if month == possible_month:
            if is_unique:
                is_unique = False
                return is_unique
            else:
                is_unique = True
    return is_unique

print("\n## Task 1b ##")
print(unique_month('May', possible_birthdays)) # False
print(unique_month('June', possible_birthdays)) # False
print(unique_month('March', (('August', '1'), ('March', '2'), ('March', '3')))) # False
print(unique_month('August', (('August', '1'), ('March', '2'), ('March', '3')))) # True

#############
# Task 1(c) #
#############

def contains_unique_day(month, possible_birthdays):
    days_in_other_months = ()
    days_in_month = ()
    for possible_month, possible_day in possible_birthdays:
        if possible_month == month:
            days_in_month += (possible_day,)
        else:
            days_in_other_months += (possible_day,)
    for day in days_in_month:
        if day not in days_in_other_months:
            return True
    return False
            

print("\n## Task 1c ##")
print(contains_unique_day("May", possible_birthdays)) # True
print(contains_unique_day("June", possible_birthdays)) # True
print(contains_unique_day("July", possible_birthdays)) # False

#############
# Task 2(a) #
#############

# Albert (given month):
# I don't know Cheryl's birthday, but I know that Bernard does not know too.

def statement1(birthday, possible_birthdays):
    month = birthday[0]
    day = birthday[1]
    is_month_unique = unique_month(month, possible_birthdays)
    is_unique_day_in_month = contains_unique_day(month, possible_birthdays)
    return not is_month_unique and not is_unique_day_in_month
    

print("\n## Task 2a ##")
print(statement1(('May', '19'), possible_birthdays)) # False
print(statement1(('August', '14'), possible_birthdays)) # True

#############
# Task 2(b) #
#############

# Bernard (given day):
# At first I don't know when Cheryl's birthday is, but I know now.

def statement2(birthday, possible_birthdays):
    day = birthday[1]
    return unique_day(day, possible_birthdays)

print("\n## Task 2b ##")
print(statement2(('May', '19'), possible_birthdays)) # True
print(statement2(('August', '14'), possible_birthdays)) # False
print(statement2(('August', '17'), possible_birthdays)) # False
print(statement2(('July', '16'), possible_birthdays)) # False

#############
# Task 2(c) #
#############

# Albert (given month):
# Then I also know when Cheryl's birthday is.

def statement3(birthday, possible_birthdays):
    month = birthday[0]
    return unique_month(month, possible_birthdays)

print("\n## Task 2c ##")
print(statement3(('May', '19'), possible_birthdays)) # False
print(statement3(('August', '14'), (('August', '14'),))) # True

##########
# Task 3 #
##########

# Based on statement 1, we can filter out some birthdays.
# From statement 2, we can filter out some more birthdays.
# Finally, using statement 3, we can filter out the remaining wrong birthdays

def get_birthday(possible_birthdays):
    def follows_statement(statement):
        return lambda birthday: statement(birthday, possible_birthdays)

    def filter_by_statement(statement):
        return tuple(filter(follows_statement(statement), possible_birthdays))
    
    possible_birthdays = filter_by_statement(statement1)
    possible_birthdays = filter_by_statement(statement2)
    possible_birthdays = filter_by_statement(statement3)
    return possible_birthdays

print("\n## Task 3 ##")
print(get_birthday(possible_birthdays)) # (('July', '16'),)
