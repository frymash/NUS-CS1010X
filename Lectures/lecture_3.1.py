from math import ceil 

start_fare = 3.0 # starting fare given stage_start = 1000
stage_start = 1000 # the starting stage starts after 1000m
stage_beyond = 10000 # the later stage begins after 10000m
fare_unit = 0.22 # the taxi fare increases by $0.22 at every interval
fare_start_per = 400 # the interval for the starting stage is 400m
fare_beyond_per = 350 # the interval for the starting stage is 350m

def taxi_fare(distance):
    """ Returns the fare for a d-metre taxi ride.

	Parameters:
	d: the distance of the taxi ride in m

	float -> float
	"""
    if distance <= stage_start:
        return taxi_fare_start_fare()
    elif distance <= stage_beyond:
        return taxi_fare_stage_start(distance)
    else:
        return taxi_fare_stage_beyond(distance)

def taxi_fare_start_fare():
    return start_fare

def taxi_fare_stage_start(distance):
    return start_fare \
           + ceil((distance - stage_start)/fare_start_per) * fare_unit

def taxi_fare_stage_beyond(distance):
    return taxi_fare(stage_beyond) \
           + ceil((distance - stage_beyond)/fare_beyond_per) * fare_unit

print(taxi_fare(800) == 3.0)
print(taxi_fare(3300) == 4.32)
print(taxi_fare(10100) == 8.28)
print(round(taxi_fare(14500)) == 10.92) # without rounding, the result of taxi_fare(14500) would be an irrational number
