WORD_DIGITS = [
    ("one", 1),
    ("two", 2),
    ("three", 3),
    ("four", 4),
    ("five", 5),
    ("six", 6),
    ("seven", 7),
    ("eight", 8),
    ("nine", 9)
]

def find_digit(line, r):
    for i in r:
        o = ord(line[i])
        # "1" => 49, "9" => 57
        if o >= 49 and o <= 57:
            return o - 48
        else:
            for word, digit in WORD_DIGITS:
                if line[i:].startswith(word):
                    return digit
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
