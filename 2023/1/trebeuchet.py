def find_digit(line, r):
    for i in r:
        o = ord(line[i])
        if o >= 48 and o <= 57:
            return o - 48
    raise ValueError("No digits in {line}".format(line = line))

def trebeuchet(text):
    lines = [line for line in text.split('\n') if line]
    sum = 0
    for line in lines:
        first_digit = find_digit(line, range(0, len(line)))
        last_digit = find_digit(line, range(len(line)-1, -1, -1))
        number = first_digit * 10 + last_digit
        sum += number

    return sum
