import math
import lcgrand
import sys

Q_LIMIT = 100
BUSY = 1
IDLE = 0

next_event_type = num_custs_delayed = num_delays_required = num_events = num_in_q = server_status = 0
area_num_in_q = area_server_status = mean_interarrival = mean_service = sim_time = time_last_event = total_of_delays = 0.0
time_arrival = [0.0] * (Q_LIMIT + 1)
time_next_event = [0.0] * 3
infile = outfile = None


def initialize():
    global server_status, num_in_q, time_last_event, num_custs_delayed, total_of_delays, area_num_in_q, area_server_status, next_event_type, time_next_event

    sim_time = 0.0
    server_status = IDLE
    num_in_q = 0
    time_last_event = 0.0

    num_custs_delayed = 0
    total_of_delays = 0.0
    area_num_in_q = 0.0
    area_server_status = 0.0

    next_event_type = 0
    time_next_event[1] = sim_time + expon(mean_interarrival)
    time_next_event[2] = 1.0e+30


def timing():
    global next_event_type, sim_time

    i = 0
    min_time_next_event = 1.0e+29
    next_event_type = 0

    for i in range(1, num_events + 1):
        if time_next_event[i] < min_time_next_event:
            min_time_next_event = time_next_event[i]
            next_event_type = i

    if next_event_type == 0:
        print(f"\nEvent list empty at time {sim_time}")
        sys.exit(1)

    sim_time = min_time_next_event


def arrive():
    global server_status, num_in_q, total_of_delays, num_custs_delayed, time_next_event

    delay = 0.0
    time_next_event[1] = sim_time + expon(mean_interarrival)

    if server_status == BUSY:
        num_in_q += 1
        if num_in_q > Q_LIMIT:
            print(f"\nOverflow of the array time_arrival at time {sim_time}")
            sys.exit(2)
        time_arrival[num_in_q] = sim_time
    else:
        delay = 0.0
        total_of_delays += delay
        num_custs_delayed += 1
        server_status = BUSY
        time_next_event[2] = sim_time + expon(mean_service)


def depart():
    global server_status, num_in_q, total_of_delays, num_custs_delayed, time_next_event

    if num_in_q == 0:
        server_status = IDLE
        time_next_event[2] = 1.0e+30
    else:
        num_in_q -= 1
        delay = sim_time - time_arrival[1]
        total_of_delays += delay
        num_custs_delayed += 1
        time_next_event[2] = sim_time + expon(mean_service)
        for i in range(1, num_in_q + 1):
            time_arrival[i] = time_arrival[i + 1]


def report():
    global area_num_in_q, area_server_status, total_of_delays, num_custs_delayed, sim_time, mean_interarrival, mean_service,
