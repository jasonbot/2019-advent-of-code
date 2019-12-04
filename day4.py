PART_ONE, PART_TWO = 1, 2

with open("day4.input", "r") as in_handle:
    start, end = map(int, in_handle.read().strip().split("-"))


def is_valid(number, method=PART_ONE):
    num_string = str(number)
    groupings = tuple()

    if not all(num_string[index] <= num_string[index+1] for index in range(len(num_string)-1)):
        return False

    last_char = None
    for character in num_string:
        if character != last_char:
            last_char = character
            groupings += (1,)
        else:
            new_count = groupings[-1] + 1
            groupings = groupings[:-1] + (new_count,)

    if method == PART_ONE:
        return any(g >= 2 for g in groupings)
    elif method == PART_TWO:
        return any(g == 2 for g in groupings)

    return False


valid_ct = 0
valid_ct_2 = 0
for x in range(start, end + 1):
    if is_valid(x, PART_ONE):
        valid_ct += 1
    if is_valid(x, PART_TWO):
        valid_ct_2 += 1

print(valid_ct, valid_ct_2)
