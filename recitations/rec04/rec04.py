def make_module(course_code, units):
    """ (String * Tuple[String]) -> Tuple[String * Tuple[String]]
    """
    return (course_code, units)

def make_units(lecture, tutorial, lab, homework, prep):
    """ (int * int * int * int * int) -> Tuple[int]
    """
    return (lecture, tutorial, lab, homework, prep)

def get_module_code(course):
    """ (Tuple[String * Tuple[String]]) -> String
    """
    return course[0]

def get_module_units(course):
    """ (Tuple[String * Tuple[String]]) -> Tuple[String]]
    """
    return course[1]

def get_module_total_units(units):
    """ efefefef
    """
    return units[0] + units[1] + units[2] + units[3] + units[4]

def make_empty_schedule():
    return ()

def add_class(course, schedule):
    return schedule + (course,)

def total_scheduled_units(schedule):
    result = 0
    for course in schedule:
        course_units = get_module_units(course)
        units = get_module_total_units(course_units)
        result += units
    return result

def drop_class(schedule, course):
    def find_course_index():
        for index in range(len(schedule)):
            if schedule[index] == course:
                break
        return index

    course_index = find_course_index()
    schedule = schedule[:course_index] + schedule[course_index+1:]
    return schedule

"""
def drop_class(schedule, course):
    new_schedule = make_empty_schedule()
    for item in schedule:
        if item == course:
            continue
        else:
            new_schedule += (course,)
    return new_schedule
"""

def credit_limit(schedule, max_credits):
    credits_in_schedule = total_scheduled_units(schedule)
    credits_to_remove = max_credits - credits_in_schedule
    while credits_to_remove > 0:
        removed_course = schedule[0]
        course_units = get_module_units(removed_course)
        course_unit_num = get_module_total_units(course_units)
        schedule = drop_class(removed_course)
        credits_to_remove -= course_unit_num
    return schedule

"""
def credit_limit(schedule, max_credits):
    total_units = total_scheduled_units(schedule)
    while total_units > max_credits:
        removed_course = schedule[-1]
        removed_units = get_module_total_units \
                            (get_module_units(removed_course))
        total_units -= removed_units
        schedule = drop_class(schedule, removed_course)
    return schedule
"""