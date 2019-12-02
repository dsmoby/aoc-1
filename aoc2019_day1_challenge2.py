# created by Moby
# aoc2019 day 1,  challenge 2

import math, csv



## load data from the input file 
masses = [] # list of module masses

with open('data/input.txt', 'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        for mf in row:
            masses.append(float(mf))

## Calculate the mass
fuel_calc = lambda mass: math.floor(mass/3) - 2
fuel_per_module = [fuel_calc(m)  for m in masses]          




def total_module_fuel(module_mass):
    """This function calculates the total fuel for a module iteratively
    --------------------------------------------------------------------
    input arguments 
    module_mass 
    -----------------
    output 
    total_fuel
    """
    
    fuel_req = fuel_calc(module_mass)
    module_fuel = 0
    
    while fuel_req > 0:
        module_fuel += fuel_req
        fuel_req = fuel_calc(fuel_req)
    return module_fuel






total_fuel_4_modules = [total_module_fuel(mass) for mass in masses]

total_fuel_spaceship = sum(total_fuel_4_modules)

print(f"Total module fuel: {total_fuel_spaceship}")
