# Created by Moby
# For AOC 2019



import math
import csv

masses = []
with open('input.txt', 'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        for mf in row:
            masses.append(float(mf))
fuel_per_module = [math.floor(m/3) - 2  for m in masses]          
total_fuel = sum(fuel_per_module)
print(total_fuel)