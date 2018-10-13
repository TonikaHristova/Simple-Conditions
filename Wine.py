import math

area = int(input())
grape_per_m2 = float(input())
needed_wine = int(input())
workers = int(input())

total_liters = area * grape_per_m2 / 2.5
our_wine = 0.4 * total_liters

if our_wine < needed_wine:
    diff = math.floor(needed_wine - our_wine)
    print("It will be a tough winter! More " + str(diff) + " liters wine needed.")
elif our_wine > needed_wine:
    our = math.floor(our_wine)
    diff = math.ceil(our_wine - needed_wine)
    wine_per_person = math.ceil(diff / workers)

    print("Good harvest this year! Total wine: " + str(our) + " liters.")
    print(str(diff) + " liters left -> " + str(wine_per_person) + " liters per person.")