#
# CS1010S --- Programming Methodology
#
# Mission 8 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from ippt import *
import csv

##########
# Task 1 #
##########

# Function read_csv has been given to help you read the csv file.
# The function returns a tuple of tuples containing rows in the csv
# file and its entries.

# Alternatively, you may use your own method.

def read_csv(csvfilename):
    rows = ()
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows += (tuple(row), )
    return rows

def read_data(filename):
    rows = read_csv(filename)
    data = ()
    age_title = ()
    rep_title_str = rows[0][1:]
    rep_title = map(int, rep_title_str)
    rows_except_header_row = rows[1:]
    for row_str in rows_except_header_row:
        row_int = map(int, row_str)
        age = int(row_int[0])
        age_title += (age,)
        new_row = row_int[1:]
        data += (new_row,)
    # print(f"age_title: {age_title}")
    # print(f"rep_title: {rep_title}")
    # print(f"data: {data}")
    return create_table(data, age_title, rep_title)
            
pushup_table = read_data("pushup.csv")
situp_table = read_data("situp.csv")
run_table = read_data("run.csv")

ippt_table = make_ippt_table(pushup_table, situp_table, run_table)

print("## Q1 ##")
print("Sit-up score of a 24-year-old who did 10 sit-ups.")
print(access_cell(situp_table, 24, 10))    # 0

print("Push-up score of a 18-year-old who did 30 push-ups.")
print(access_cell(pushup_table, 18, 30))   # 16

print("Run score of a 30-year old-who ran 12 minutes (720 seconds)")
print(access_cell(run_table, 30, 720))     # 36

# Since our run.csv file does not have data for 725 seconds, we should
# get None if we try to access that cell.
print(access_cell(run_table, 30, 725))     # None


##########
# Task 2 #
##########

def table_score(table, age, activity_score, min_score, max_score):
    def last_digit_of(n):
        return n % 10
    
    if activity_score > max_score:
        return table_score(table, age, max_score, min_score, max_score)
    elif activity_score < min_score:
        return table_score(table, age, min_score, min_score, max_score)
    else:
        last_digit = last_digit_of(activity_score)
        if table == run_table and last_digit != 0:
            rounding_offset = 10 - last_digit
            next_band = activity_score + rounding_offset
            return table_score(table, age, next_band, min_score, max_score)
        else:
            return access_cell(table, age, activity_score)

def pushup_score(pushup_table, age, pushup):
    return table_score(pushup_table, age, pushup, 1, 60)

def situp_score(situp_table, age, situp):
    return table_score(situp_table, age, situp, 1, 60)

def run_score(run_table, age, run):
    return table_score(run_table, age, run, 510, 1100)

print("## Q2 ##")
print(pushup_score(pushup_table, 18, 61))   # 25
print(pushup_score(pushup_table, 18, 70))   # 25
print(situp_score(situp_table, 24, 0))      # 0

print(run_score(run_table, 30, 720))        # 36
print(run_score(run_table, 30, 725))        # 35
print(run_score(run_table, 30, 735))        # 35
print(run_score(run_table, 30, 500))        # 50
print(run_score(run_table, 30, 1300))       # 0


##########
# Task 3 #
##########

def ippt_award(score):
    if score >= 85:
        return "G"
    elif score >= 75:
        return "S"
    elif score >= 61:
        return "P$"
    elif score >= 51:
        return "P"
    else:
        return "F"

print("## Q3 ##")
print(ippt_award(50))     # F
print(ippt_award(51))     # P
print(ippt_award(61))     # P$
print(ippt_award(75))     # S
print(ippt_award(85))     # G


##########
# Task 4 #
##########

def ippt_results(ippt_table, age, pushup, situp, run):
    pushup_table = ippt_table[0]
    situp_table = ippt_table[1]
    run_table = ippt_table[2]
    pushup_points = pushup_score(pushup_table, age, pushup)
    situp_points = situp_score(situp_table, age, situp)
    run_points = run_score(run_table, age, run)
    total_ippt_score = pushup_points + situp_points + run_points
    award = ippt_award(total_ippt_score)
    return (total_ippt_score, award)

print("## Q4 ##")
print(ippt_results(ippt_table, 25, 30, 25, 820))      # (53, 'P')
print(ippt_results(ippt_table, 28, 56, 60, 530))      # (99, 'G')
print(ippt_results(ippt_table, 38, 18, 16, 950))      # (36, 'F')
print(ippt_results(ippt_table, 25, 34, 35, 817))      # (61, 'P$')
print(ippt_results(ippt_table, 60, 70, 65, 450))      # (100, 'G')


##########
# Task 5 #
##########
def make_training_program(rate_pushup, rate_situp, rate_run):
    def training_program(ippt_table, age, pushup, situp, run, days):
        pushup_improvement = days // rate_pushup
        situp_improvement = days // rate_situp
        run_improvement = days // rate_run

        final_pushups = pushup + pushup_improvement
        final_situps = situp + situp_improvement
        final_run_time = run - run_improvement
        
        award = ippt_results(ippt_table,
                            age,
                            final_pushups,
                            final_situps,
                            final_run_time)
        result = (final_pushups, final_situps, final_run_time, award)
        return result
        
    return training_program

# print("## Q5 ##")
tp = make_training_program(7, 3, 10)
print(tp(ippt_table, 25, 30, 25, 820, 30))        # (34, 35, 817, (61, 'P$'))


##########
# Bonus  #
##########

def make_tp_bonus(rate_pushup, rate_situp, rate_run):
    pushup_table = ippt_table[0]
    situp_table = ippt_table[1]
    run_table = ippt_table[2]
    
    def tp_bonus(ippt_table, age, pushup, situp, run, days):
        def new_ippt_result(pushup, situp, run, days):
            def days_to_next_pt(reps_or_time, station):
                def new_reps_or_time(score_fn, station_table, reps_or_time):
                    def unit_improvement(reps_or_time):
                        if station_table == run_table:
                            reps_or_time -= 10
                        else:
                            reps_or_time += 1
                        return reps_or_time
                        
                    og_score = score_fn(station_table, age, reps_or_time)
                    score = og_score
                    while score == og_score:
                        reps_or_time = unit_improvement(reps_or_time)
                        score = score_fn(station_table, age, reps_or_time)
                        # print(f"score_fn: {score_fn.__name__} | age: {age} | reps_or_time: {reps_or_time} | score: {score} | og_score: {og_score}")
                    return reps_or_time
                
                if station == "run":
                    nonlocal run_table
                    next_pt_run = new_reps_or_time(run_score, run_table, run)
                    # print(f"run: {run} | next_pt_run: {next_pt_run} | rate_run: {rate_run}\n")
                    days = (run - next_pt_run) * rate_run
                        
                elif station == "pushup":
                    nonlocal pushup_table
                    next_pt_pushup = new_reps_or_time(pushup_score, pushup_table, pushup)
                    # print(f"pushup: {pushup} | next_pt_pushup: {next_pt_pushup} | rate_pushup: {rate_pushup}\n")
                    days = (next_pt_pushup - pushup) * rate_pushup
                else:
                    nonlocal situp_table
                    next_pt_situp = new_reps_or_time(situp_score, situp_table, situp)
                    # print(f"situp: {situp} | next_pt_situp: {next_pt_situp} | rate_situp: {rate_situp}\n")
                    days = (next_pt_situp - situp) * rate_situp
                return days
            
            if days == 0:
                return (pushup, situp, run)
            else:
                pushup_days_to_next_pt = days_to_next_pt(pushup, "pushup")
                situp_days_to_next_pt = days_to_next_pt(situp, "situp")
                run_days_to_next_pt = days_to_next_pt(run, "run")

                days_to_deduct = min(pushup_days_to_next_pt,
                                     situp_days_to_next_pt,
                                     run_days_to_next_pt)
                # print(f"days_to_deduct: {days_to_deduct}")

                max_deductible_days = days - days_to_deduct
                if max_deductible_days < 0:
                    return (pushup, situp, run)

                else:
                    if days_to_deduct == pushup_days_to_next_pt:
                        pushup_improvement = days_to_deduct // rate_pushup
                        pushup += pushup_improvement
                    elif days_to_deduct == situp_days_to_next_pt:
                        situp_improvement = days_to_deduct // rate_situp
                        situp += situp_improvement
                    else:
                        run_improvement = days_to_deduct // rate_run
                        run -= run_improvement
                    days -= days_to_deduct
                    # print(f"Days left: {days}")            
                    return new_ippt_result(pushup, situp, run, days)
        
        final_pushups, final_situps, final_run_time = new_ippt_result(pushup, situp, run, days)
        # print(f"final_pushups: {final_pushups} | final_situps: {final_situps} | final_run_time: {final_run_time}")
        award = ippt_results(ippt_table,
                            age,
                            final_pushups,
                            final_situps,
                            final_run_time)
        result = (final_pushups, final_situps, final_run_time, award)
        return result

    return tp_bonus


tp_bonus = make_tp_bonus(7, 3, 10)


# Note: Depending on your implementation, you might get a different number of
# sit-up, push-up, and 2.4km run timing. However, the IPPT score and grade
# should be the same as the sample output.

print(f"Bonus test 1: {tp_bonus(ippt_table, 25, 20, 30, 800, 30)}")      # (20, 40, 800, (58, 'P'))
print(f"Bonus test 2: {tp_bonus(ippt_table, 25, 20, 30, 800, 2)}")       # (20, 30, 800, (52, 'P'))
print(f"Bonus test 3: {tp_bonus(ippt_table, 25, 20, 30, 800, 43)}")
