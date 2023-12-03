import re

def find_all(lines):
    symbols = set()
    numbers = set()
    for row in range(len(lines)):
        line = lines[row]
        for m in re.finditer("\d+", line):
            start, end = m.span()
            numbers.add((row, start, end, int(m.group(0))))

        for col in range(len(line)):
            o = ord(line[col])
            if o != 46 and (o < 48 or o > 57):
                symbols.add((row, col))

    return symbols, numbers

def has_adjacent_symbol(symbols, row, start_col, end_col):
    for r in [row-1, row+1]:
        for c in range(start_col-1, end_col+1):
            if (r, c) in symbols: return True

    return (row, start_col-1) in symbols or (row, end_col) in symbols

def run(text):
    lines = [line for line in text.split('\n') if line]
    symbols, numbers = find_all(lines)

    sum = 0
    for row, start_col, end_col, number in numbers:
        if has_adjacent_symbol(symbols, row, start_col, end_col):
            sum += number

    return sum
