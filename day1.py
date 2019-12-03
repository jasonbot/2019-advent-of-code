import math

total = 0.0


def fuel(mass):
    # Take its mass, divide by three, round down, and subtract 2.
    return max([int(math.floor(float(mass) / 3.0) - 2.0), 0.0])


def integrated_fuel(mass):
    total_fuel = 0.0
    more_fuel = fuel(mass)
    while more_fuel > 0:
        total_fuel += more_fuel
        more_fuel = fuel(more_fuel)
    return total_fuel


with open("day1.input", "r") as in_file:
    for line in in_file:
        mass = float(line.strip())
        total += integrated_fuel(mass)

print(int(total))
