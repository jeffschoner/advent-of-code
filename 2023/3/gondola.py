import re

def find_all_symbols(lines):
    symbols = set()
    for row in range(len(lines)):
        line = lines[row]
        for col in range(len(line)):
            o = ord(line[col])
            if o != 46 and (o < 48 or o > 57):
                symbols.add((row, col))

    return symbols

def has_adjacent_symbol(symbols, row, start_col, end_col):
    for r in [row-1, row+1]:
        for c in range(start_col-1, end_col+1):
            if (r, c) in symbols: return True

    return (row, start_col-1) in symbols or (row, end_col) in symbols

def run(text):
    lines = [line for line in text.split('\n') if line]
    symbols = find_all_symbols(lines)

    sum = 0
    for row in range(len(lines)):
        line = lines[row]
        for m in re.finditer("\d+", line):
            start, end = m.span()
            if has_adjacent_symbol(symbols, row, start, end):
                sum += int(m.group(0))

    return sum
