import collections


def follow_trace(operands, matrix):
    x, y = 0.0, 0.0

    delta_map = {
        'U': (0, -1),
        'D': (0, 1),
        'L': (-1, 0),
        'R': (1, 0)
    }

    visited = {(0, 0)}
    distance = 0

    for operand in operands:
        direction = operand[0]
        ct = int(operand[1:])

        dx, dy = delta_map[direction]

        for _ in range(ct):
            x += dx
            y += dy

            distance += 1
            if (x, y) not in visited:
                matrix[(x, y)] += (distance,)  # 1
                visited.add((x, y))


def min_distance(matrix):
    min_distance = None

    for (x, y), crosses in matrix.items():
        if len(crosses) > 1:
            distance = sum(abs(x) for x in crosses)  # abs(x) + abs(y)
            if min_distance is None or min_distance >= distance:
                min_distance = distance

    return min_distance


matrix = collections.defaultdict(tuple)

with open("day3.input", "r") as in_file:
    for line in in_file:
        operands = line.strip().split(",")
        follow_trace(operands, matrix)

print(min_distance(matrix))
