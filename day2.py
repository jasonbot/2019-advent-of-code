def chunks(line_array):
    index = 0
    while index <= len(line_array):
        chunk = line_array[index:index+4]
        if chunk and chunk[0] == 99:
            return
        yield chunk
        index += 4


def interpret_line(text_line):
    line_parsed = [int(item) for item in text_line.strip().split(",")]
    # Once you have a working computer, the first step is to restore the gravity
    # assist program (your puzzle input) to the "1202 program alarm" state it had
    # just before the last computer caught fire. To do this, before running the
    # program, replace position 1 with the value 12 and replace position 2 with the
    # value 2. What value is left at position 0 after the program halts?]
    for x in range(100):
        for y in range(100):
            line_array = line_parsed[:]
            try:
                line_array[1] = x
                line_array[2] = y
                for chunk in chunks(line_array):
                    opcode, *others = chunk
                    if opcode == 99:
                        break
                    elif opcode in (1, 2):
                        addr1, addr2, dest = others
                        operand = {1: lambda x, y: x + y,
                                   2: lambda x, y: x*y}[opcode]
                        line_array[dest] = operand(
                            line_array[addr1], line_array[addr2])
                    else:
                        pass
                        # raise ValueError(opcode)
                if line_array[0] == 19690720:
                    yield x, y, line_array[0]
            except Exception:
                pass


with open("day2.input", "r") as in_lines:
    for line in in_lines:
        for item in interpret_line(line):
            print(100 * item[0] + item[1])
