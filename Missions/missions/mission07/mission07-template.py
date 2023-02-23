# CS1010S --- Programming Methodology
#
# Mission 7 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

import datetime
import csv

###############
# Pre-defined #
###############

def map(fn, seq):
    res = ()

    for ele in seq:
        res = res + (fn(ele), )
    return res

def filter(pred, seq):
    res = ()

    for ele in seq:
        if pred(ele):
            res = res + (ele, )
    return res

###############
# Station ADT #
###############

def make_station(station_code, station_name):
    return (station_code, station_name)

def get_station_code(station):
    return station[0]

def get_station_name(station):
    return station[1]

test_station1 = make_station('CC2', 'Bras Basah')
test_station2 = make_station('CC3', 'Esplanade')
test_station3 = make_station('CC4', 'Promenade')


############
## Task 1 ##
############

def make_train(train_code):
    ''' Do NOT modify this function'''
    return (train_code,)


test_train = make_train('TRAIN 0-0')

#############
# Task 1a   #
#############

def get_train_code(train):
    return train[0]

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 1A
print("## Task 1a ##")
print(get_train_code(test_train))

# Expected Output #
# TRAIN 0-0

#############
# Task 1b   #
#############

def make_line(name, stations):
    """ (name, tuple_of_stations) -> line
    """
    return (name, stations)

def get_line_name(line):
    """ (line) -> name
    """
    return line[0]
    

def get_line_stations(line):
    """ (line) -> tuple_of_stations
    """
    return line[1]

def get_station_by_name(line, station_name):
    """ (line, station_name) -> station or None
    """
    stations = get_line_stations(line)
    for (current_code, current_name) in stations:
        if current_name == station_name:
            return (current_code, current_name)
    return None

def get_station_by_code(line, station_code):
    """ (line, station_name) -> station or None
    """
    stations = get_line_stations(line)
    for (current_code, current_name) in stations:
        if current_code == station_code:
            return (current_code, current_name)
    return None

def get_station_position(line, station_code):
    """ (line, station_code) -> Number
    """
    stations = get_line_stations(line)
    for (index, (current_code, current_name)) in enumerate(stations):
        if current_code == station_code:
            return index
    return -1

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 1B
print("## Task 1b ##")
test_line = make_line('Circle Line', (test_station1, test_station2, test_station3))
print(get_line_name(test_line))
print(get_line_stations(test_line))
print(get_station_by_name(test_line, 'Bras Basah'))
print(get_station_by_code(test_line, 'CC4'))

# Expected Output #
# Circle Line
# (('CC2', 'Bras Basah'), ('CC3', 'Esplanade'), ('CC4', 'Promenade'))
# ('CC2', 'Bras Basah')
# ('CC4', 'Promenade')

#############
# Task 1c   #
#############

# Helpers for the functions below:
def get_from_station(train_position):
    return train_position[1]
    
def get_to_station(train_position):
    return train_position[2]

def get_station_order(station):
    """ e.g. returns 4 if station is ('CC4', 'Promenade')
    """
    return station[0]

def get_stopped_or_previous_station(train_position, target):
    """ (train_position) -> station or None
    """
    is_moving = get_is_moving(train_position)
    if target == "stopped":
        pred = is_moving
    else:
        pred = not(is_moving)
        
    if pred:
        return None
    else:
        return get_from_station(train_position)

#############

def make_train_position(is_moving, from_station, to_station):
    """ (is_moving, from_station, to_station) -> train_position
    """
    return (is_moving, from_station, to_station)

def get_is_moving(train_position):
    """ (train_position) -> True or False
    """
    return train_position[0]

def get_direction(line, train_position):
    """ (line, train_position) -> 0 or 1
    """
    from_stn = get_from_station(train_position)
    to_stn = get_to_station(train_position)
    line_stns = get_line_stations(line)
    for stn in line_stns:
        if stn == from_stn:
            return 0
        elif stn == to_stn:
            return 1
        # If the line's stations and the train_position's stations don't match
        # else:
        #     return -1
    
def get_stopped_station(train_position):
    """ (train_position) -> station or None
    """
    return get_stopped_or_previous_station(train_position, "stopped")

def get_previous_station(train_position):
    """ (train_position) -> station or None
    """
    return get_stopped_or_previous_station(train_position, "previous")

def get_next_station(train_position):
    """ (train_position) -> station
    """
    return train_position[2]

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 1C
print("## Task 1c ##")
test_train_position1 = make_train_position(False, test_station1, test_station2)
test_train_position2 = make_train_position(True, test_station3, test_station2)
print(get_is_moving(test_train_position2))
print(get_direction(test_line, test_train_position1))
print(get_stopped_station(test_train_position1))
print(get_previous_station(test_train_position2))
print(get_next_station(test_train_position2))

# Expected Output #
# True
# 0
# ('CC2', 'Bras Basah')
# ('CC4', 'Promenade')
# ('CC3', 'Esplanade')

#############
# Task 1d   #
#############

def make_schedule_event(train, train_position, time):
    """ (train, train_position, time) -> schedule_event
    """
    return (train, train_position, time)

def get_train(schedule_event):
    """ (schedule_event) -> train
    """
    return schedule_event[0]

def get_train_position(schedule_event):
    """ (schedule_event) -> train_position
    """
    return schedule_event[1]

def get_schedule_time(schedule_event):
    """ (schedule_event) -> time
    """
    return schedule_event[2]

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 1D
print("## Task 1d ##")
test_bd_event1 = make_schedule_event(test_train, test_train_position2, datetime.datetime(2016, 1, 1, 9, 27))
test_bd_event2 = make_schedule_event(test_train, test_train_position1, datetime.datetime(2016, 1, 1, 2, 25))
print(get_train(test_bd_event1))
print(get_train_position(test_bd_event1))
print(get_schedule_time(test_bd_event1))

# Expected Output #
# ('TRAIN 0-0',)
# (True, ('CC4', 'Promenade'), ('CC3', 'Esplanade'))
# 2016-01-01 09:27:00


############
## Task 2 ##
############

def read_csv(csvfilename):
    rows = ()
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows += (tuple(row), )
    return rows

#############
# Task 2a   #
#############

def parse_lines(data_file):
    rows = read_csv(data_file)[1:]
    lines = ()
    curr_line_name = rows[0][2]
    curr_line_stations = ()
    for row in rows:
        code, station_name, line_name = row
        if line_name == curr_line_name:
            curr_line_stations += (make_station(code, station_name),)
        else:
            lines += (make_line(curr_line_name, curr_line_stations),)
            curr_line_name = line_name
            curr_line_stations = (make_station(code, station_name),)
    lines += (make_line(curr_line_name, curr_line_stations),)
    return lines

# UNCOMMENT THE CODE BELOW WHEN YOU ARE DONE WITH TASK 2A. THIS IS NOT OPTIONAL TESTING!
LINES = parse_lines('station_info.csv')
CCL = filter(lambda line: get_line_name(line) == 'Circle Line', LINES)[0]

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 2A
print("## Task 2a ##")
print(get_line_stations(CCL)[5:8])

# Expected Output #
# (('CC6', 'Stadium'), ('CC7', 'Mountbatten'), ('CC8', 'Dakota'))

#############
# Task 2b   #
#############

# ScheduleEvent: (train, train_position, time)

def parse_events_in_line(data_file, line):
    rows = read_csv(data_file)[1:]
    events = ()
    for row in rows:
        train_code, is_moving, from_code, to_code, date, clock_time = row
        from_stn = get_station_by_code(line, from_code)
        
        if from_stn is not None: # Station is found in the line
            # Create train for schedule_event
            train = make_train(train_code)
            
            # Create train_position for schedule_event
            to_stn = get_station_by_code(line, to_code)
            is_moving = True if is_moving == "True" else False
            train_position = make_train_position(is_moving, from_stn, to_stn)
            
            # Create time for schedule_event
            day, month, year = map(int, (date[:2], date[3:5], date[6:]))
            hour, minute = map(int, (clock_time[:2], clock_time[3:]))
            time = datetime.datetime(year, month, day, hour, minute)

            # Create schedule_event
            schedule_event = make_schedule_event(train, train_position, time)

            # Append schedule_event to events
            events += (schedule_event,)
        
    return events

# UNCOMMENT THE CODE BELOW WHEN YOU ARE DONE WITH TASK 2B. THIS IS NOT OPTIONAL TESTING!
BD_EVENTS = parse_events_in_line('breakdown_events.csv', CCL)

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 2B
print("## Task 2b ##")
print(BD_EVENTS[9])

# Expected Output #
# (('TRAIN 1-11',), (False, ('CC23', 'one-north'), ('CC22', 'Buona Vista')), datetime.datetime(2017, 1, 6, 7, 9))

############
## Task 3 ##
############

#############
# Task 3a   #
#############

def is_valid_event_in_line(bd_event, line):
    """ (bd_event, line) -> True or False
    """
    def get_from_station(train_position):
        return train_position[1]
        
    def get_to_station(train_position):
        return train_position[2]
        
    def are_stns_adjacent(stn1, stn2):
        stn1_code = get_station_code(stn1)
        stn2_code = get_station_code(stn2)
        stn1_position = get_station_position(line, stn1_code)
        stn2_position = get_station_position(line, stn2_code)
        return abs(stn1_position - stn2_position) == 1
    
    def from_to_adjacent(train_position):
        from_stn = get_from_station(train_position)
        to_stn = get_to_station(train_position)
        return are_stns_adjacent(from_stn, to_stn)
        
    def within_op_hours(opening_hr, closing_hr):
        event_time = get_schedule_time(bd_event)
        hour_and_minute = datetime.time(event_time.hour, event_time.minute)
        return opening_hr <= hour_and_minute <= closing_hr
    
    def main():
        train_position = get_train_position(bd_event)
        opening_hr = datetime.time(7,0)
        closing_hr = datetime.time(23,0)
        criterion_1 = from_to_adjacent(train_position)
        criterion_2 = within_op_hours(opening_hr, closing_hr)
        return criterion_1 and criterion_2
    
    return main()


def get_valid_events_in_line(bd_events, line):
    ''' Do NOT modify this function'''
    return filter(lambda ev: is_valid_event_in_line(ev, line), bd_events)

# UNCOMMENT THE CODE BELOW WHEN YOU ARE DONE WITH TASK 3A. THIS IS NOT OPTIONAL TESTING!
VALID_BD_EVENTS = get_valid_events_in_line(BD_EVENTS, CCL)

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 3A
# False
test_bd_event3 = (('TRAIN 0-0',),
                 (False, ('CC2', 'Bras Basah'), ('CC29', 'Harbourfront')),
                 datetime.datetime(2016, 1, 1, 9, 25))
# False
test_bd_event4 = (('TRAIN 0-0',),
                 (False, ('CC29', 'Harbourfront'), ('CC2', 'Bras Basah')),
                 datetime.datetime(2016, 1, 1, 2, 38))
# True
test_bd_event5 = (('TRAIN 0-0',),
                 (True, ('CC20', 'Farrer Road'), ('CC19', 'Botanic Gardens')),
                 datetime.datetime(2016, 1, 1, 7, 00))
# True
test_bd_event6 = (('TRAIN 0-0',),
                 (True, ('CC19', 'Botanic Gardens'), ('CC20', 'Farrer Road')),
                 datetime.datetime(2016, 1, 1, 23, 00))
# True
test_bd_event7 = (('TRAIN 0-0',),
                 (True, ('CC19', 'Botanic Gardens'), ('CC20', 'Farrer Road')),
                 datetime.datetime(2016, 1, 1, 22, 59))
# False
test_bd_event8 = (('TRAIN 0-0',),
                 (True, ('CC19', 'Botanic Gardens'), ('CC20', 'Farrer Road')),
                 datetime.datetime(2016, 1, 1, 23, 1))

# True
test_bd_event7 = (('TRAIN 0-0',),
                 (False, ('CC19', 'Botanic Gardens'), ('CC20', 'Farrer Road')),
                 datetime.datetime(2016, 1, 1, 22, 59))

print("## Task 3a ##")
print(is_valid_event_in_line(test_bd_event1, CCL))
print(is_valid_event_in_line(test_bd_event2, CCL))
print(is_valid_event_in_line(test_bd_event3, CCL))
print(is_valid_event_in_line(test_bd_event4, CCL))
print(is_valid_event_in_line(test_bd_event5, CCL))
print(is_valid_event_in_line(test_bd_event6, CCL))
print(is_valid_event_in_line(test_bd_event7, CCL))
print(is_valid_event_in_line(test_bd_event8, CCL))

# Expected Output #
# True
# False


#############
# Task 3b   #
#############

def get_location_id_in_line(bd_event, line):
    """ (schedule_event, line) -> location_id: int
    """
    def get_stopped_stn_posn(train_posn):
        stopped_stn = get_stopped_station(train_posn)
        stopped_stn_code = get_station_code(stopped_stn)
        return get_station_position(line, stopped_stn_code)
    
    def get_lower_stn_number(train_posn):
        prev_stn = get_previous_station(train_posn)
        prev_stn_code = get_station_code(prev_stn)
        prev_stn_posn = get_station_position(line, prev_stn_code)

        next_stn = get_next_station(train_posn)
        next_stn_code = get_station_code(next_stn)
        next_stn_posn = get_station_position(line, next_stn_code)
        return min(prev_stn_posn, next_stn_posn)

    def main():
        train_posn = get_train_position(bd_event)
        is_moving = get_is_moving(train_posn)
        if not is_moving:
            location_id = get_stopped_stn_posn(train_posn)
        else:
            lower_stn_number = get_lower_stn_number(train_posn)
            location_id = 0.5 + lower_stn_number
        return location_id

    return main()


# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 3B
print("## Task 3b ##")
test_loc_id1 = get_location_id_in_line(test_bd_event1, CCL)
test_loc_id2 = get_location_id_in_line(test_bd_event2, CCL)
print(test_loc_id1)
print(test_loc_id2)

# Expected Output #
# 2.5
# 1

############
## Task 4 ##
############

# UNCOMMENT the following to read the entire train schedule
FULL_SCHEDULE = parse_events_in_line('train_schedule.csv', CCL)    # this will take some time to run

#############
# Task 4a   #
#############

def get_schedules_at_time(train_schedule, time):
    """ (Tuple[schedule_event], datetime.datetime) -> Tuple[schedule_event])
    """
    def is_schedule_at_time(schedule_event):
        schedule_time = get_schedule_time(schedule_event)
        return schedule_time == time
    
    return filter(is_schedule_at_time, train_schedule)

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 4A
print("## Task 4a ##")
test_datetime = datetime.datetime(2017, 1, 6, 6, 0)
test_schedules_at_time = get_schedules_at_time(FULL_SCHEDULE[:5], test_datetime)
print(test_schedules_at_time[1])

# Expected Output #
# (('TRAIN 1-0',), (False, ('CC29', 'HarbourFront'), ('CC28', 'Telok Blangah')), datetime.datetime(2017, 1, 6, 6, 0))

#############
# Task 4b   #
#############

def get_schedules_near_loc_id_in_line(train_schedule, line, loc_id):
    """ (Tuple[schedule_event], line, loc_id) -> Tuple[schedule_event]
    """
    def close_to_loc_id(schedule_event):
        event_loc_id = get_location_id_in_line(schedule_event, line)
        is_close = abs(event_loc_id - loc_id) <= 0.5
        return is_close
    
    return filter(close_to_loc_id, train_schedule)

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 4B
print("## Task 4b ##")
test_schedules_near_loc_id = get_schedules_near_loc_id_in_line(FULL_SCHEDULE[:10], CCL, test_loc_id1)
print(test_schedules_near_loc_id[1])

# Expected Output #
# (('TRAIN 0-0',), (True, ('CC3', 'Esplanade'), ('CC4', 'Promenade')), datetime.datetime(2017, 1, 6, 6, 5))

#############
# Task 4c   #
#############

def get_rogue_schedules_in_line(train_schedule, line, time, loc_id):
    at_time = get_schedules_at_time(train_schedule, time)
    at_time_and_near_loc_id = get_schedules_near_loc_id_in_line(at_time, line, loc_id)
    return at_time_and_near_loc_id

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 4C
print("## Task 4c ##")
test_bd_event3 = VALID_BD_EVENTS[0]
test_loc_id3 = get_location_id_in_line(test_bd_event3, CCL)
test_datetime3 = get_schedule_time(test_bd_event3)
test_rogue_schedules = get_rogue_schedules_in_line(FULL_SCHEDULE[1000:1100], CCL, test_datetime3, test_loc_id3)
print(test_rogue_schedules[2])

# Expected Output #
# (('TRAIN 1-11',), (True, ('CC24', 'Kent Ridge'), ('CC23', 'one-north')), datetime.datetime(2017, 1, 6, 7, 9))

############
## Task 5 ##
############

###############
# Scorer ADT  #
###############

def make_scorer():
    return {}

def blame_train(scorer, train_code):
    scorer[train_code] = scorer.get(train_code, 0) + 1
    return scorer

def get_blame_scores(scorer):
    return tuple(scorer.items())

# Use this to keep track of each train's blame score.
SCORER = make_scorer()

#############
# Task 5a   #
#############

def calculate_blame_in_line(full_schedule, valid_bd_events, line, scorer):
    """ (Tuple[schedule_event], Tuple[schedule_event], line, scorer) -> scorer
    """
    # loops = 0
    # Step 1
    for valid_bd_event in valid_bd_events:
        time = get_schedule_time(valid_bd_event)
        loc_id = get_location_id_in_line(valid_bd_event, line)
        nearby_train_schedules = get_rogue_schedules_in_line(full_schedule,
                                                             line,
                                                             time,
                                                             loc_id)
        # print(f"nearby_train_schedules: {nearby_train_schedules}")
        blamed_trains = ()
            
    # Step 2
        for nearby_train_schedule in nearby_train_schedules:
            train = get_train(nearby_train_schedule)
            train_code = get_train_code(train)
            if train_code not in blamed_trains:
                blame_train(scorer, train_code)
                blamed_trains += (train_code,)
        # loops += 1
        # print(f"blamed_trains: {blamed_trains}")
        # if loops == 3:
        #     break
    return scorer

# UNCOMMENT THE CODE BELOW WHEN YOU ARE DONE WITH TASK 5A. THIS IS NOT OPTIONAL TESTING!
calculate_blame_in_line(FULL_SCHEDULE, VALID_BD_EVENTS, CCL, SCORER)

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 5A
print("## Task 5a ##")
print(sorted(get_blame_scores(SCORER))[7])
# print(sorted(get_blame_scores(SCORER)))

# Expected Answer
# ('TRAIN 0-5', 2)

#############
# Task 5b   #
#############

def find_max_score(scorer):
    trains_and_scores = get_blame_scores(scorer)
    scores = list(map(lambda train_and_score: train_and_score[1], trains_and_scores))
    return max(scores)

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 5B
print("## Task 5b ##")
test_max_score = find_max_score(SCORER)
print(test_max_score)

# Expected answer
# 180

#############
# Task 5c   #
#############

# UNCOMMENT THE CODE BELOW TO VIEW ALL BLAME SCORES. THIS IS NOT OPTIONAL TESTING!
print("## Task 5c ##")
train_scores = get_blame_scores(SCORER)
print("############### Candidate rogue trains ###############")
for score in train_scores:
    print("%s: %d" % (score[0], score[1]))
print("######################################################")

''' Please type your answer into the Task 5c textbox on Coursemology
Yes.

Every candidate rogue train apart from TRAIN 0-4 could only be blamed for
<20 breakdown events. TRAIN 0-4 could be blamed for a significantly greater
number of breakdown events than the other candidates -- it can be blamed for
a total of 180 breakdown events. This difference supports the hypothesis that
the breakdown events are caused by a single rogue train.

'''
#############
# Task 5d   #
#############

def find_rogue_train(scorer, max_score):
    blame_scores = get_blame_scores(scorer)
    for (train_code, score) in blame_scores:
        if score == max_score:
            return train_code

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 5D
print("## Task 5d ##")
print("Rogue Train is '%s'" % find_rogue_train(SCORER, test_max_score))

# Expected Answer
# Rogue Train is 'TRAIN 0-4'

