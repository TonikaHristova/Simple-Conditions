import math

needed_hours = int(input())
days = int(input())
workers = int(input())


education = 0.1 * days
working_hours = (days - education) * 8
out_of_office = workers * (2 * days)

total_hours = math.floor(working_hours + out_of_office)

if total_hours > needed_hours:
    left_hours = math.floor(total_hours - needed_hours)
    print("Yes!" + str(left_hours) + " hours left.")

elif total_hours < needed_hours:
    not_enough = math.floor(needed_hours - total_hours)
    print("Not enough time!" + str(not_enough) + " hours needed.")







