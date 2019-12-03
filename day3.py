import collections


def follow_trace(operands, matrix):
    x, y = 0, 0

    delta_map = {
        'U': (0, -1),
        'D': (0, 1),
        'L': (-1, 0),
        'R': (1, 0)
    }

    for operand in operands:
        visited = {(0, 0)}
        direction = operand[0]
        ct = int(operand[1:])

        dx, dy = delta_map[direction]

        for step in range(ct):
            x += dx
            y += dy
            if (x, y) not in visited:
                matrix[(x, y)] += (step,)  # 1
                # print("Add", x, y, step, matrix[(x, y)])
                visited.add((x, y))
                if len(matrix[(x, y)]) > 1:
                    print("CROSS", x, y, sum(abs(x)
                                             for x in matrix[(x, y)]), matrix[(x, y)])


def min_distance(matrix):
    min_distance = None

    for (x, y), crosses in matrix.items():
        if len(crosses) > 1:
            distance = sum(abs(x) for x in crosses)  # abs(x) + abs(y)
            if min_distance is None or min_distance >= distance:
                min_distance = distance
                print("CRO", crosses, x, y, distance)

    return min_distance


matrix = collections.defaultdict(tuple)

with open("day3.input", "r") as in_file:
    for line in in_file:
        operands = line.strip().split(",")
        follow_trace(operands, matrix)

print(min_distance(matrix))
