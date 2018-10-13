import math


days_off = int(input())
norm_per_year_min = 30000

working_days = 365 - days_off
time_to_play = (days_off * 127) + (working_days * 63)

if norm_per_year_min > time_to_play:
    diff = (norm_per_year_min - time_to_play)
    hour = math.floor(diff / 60)
    min = diff - hour * 60

    print("Tom sleeps well")
    print(str(hour) + " hours and " + str(min) + " minutes less for play")

elif norm_per_year_min < time_to_play:
    diff = time_to_play - norm_per_year_min
    hour = math.floor(diff/60)
    min = diff - hour*60

    print("Tom will run away")
    print(str(hour) + " hours and " + str(min) + " minutes more for play")

