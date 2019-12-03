import math

total = 0.0


def fuel(mass):
    # Take its mass, divide by three, round down, and subtract 2.
    return int(math.floor(float(mass) / 3.0) - 2.0)


with open("day1.input", "r") as in_file:
    for line in in_file:
        mass = float(line.strip())
        total += fuel(mass)

print(int(total))
