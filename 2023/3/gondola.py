import re

def find_all(lines):
    symbols = set()
    numbers = set()
    gears = set()

    for row in range(len(lines)):
        line = lines[row]
        for m in re.finditer("\d+", line):
            start, end = m.span()
            numbers.add((row, start, end, int(m.group(0))))

        for col in range(len(line)):
            o = ord(line[col])
            if o == 42:
                gears.add((row, col))
                symbols.add((row, col))
            elif o != 46 and (o < 48 or o > 57):
                symbols.add((row, col))

    return symbols, numbers, gears

def adjacents(symbols, gears, row, start_col, end_col):
    has_symbols = False
    adj_gears = set()

    for r in [row-1, row+1]:
        for c in range(start_col-1, end_col+1):
            if (r, c) in symbols:
                has_symbols = True
            if (r, c) in gears:
                adj_gears.add((r, c))

    if not has_symbols:
        has_symbols = (row, start_col-1) in symbols or (row, end_col) in symbols

    if (row, start_col-1) in gears:
        adj_gears.add((row, start_col-1))

    if (row, end_col) in gears:
        adj_gears.add((row, end_col))

    return has_symbols, adj_gears

def run(text):
    lines = [line for line in text.split('\n') if line]
    symbols, numbers, gears = find_all(lines)

    symbol_sum = 0
    all_adj_gears = {gear: [] for gear in gears}
    for row, start_col, end_col, number in numbers:
        has_symbols, adj_gears = adjacents(symbols, gears, row, start_col, end_col)
        if has_symbols:
            symbol_sum += number
        for adj_gear in adj_gears:
            all_adj_gears[adj_gear].append(number)


    return symbol_sum, sum([(nums[0]*nums[1] if len(nums) == 2 else 0) for nums in all_adj_gears.values()])
