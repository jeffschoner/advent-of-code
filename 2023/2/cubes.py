from collections import defaultdict
import re

def run(text):
    lines = [line for line in text.split('\n') if line]
    result_sum = 0

    for line in lines:
        m = re.match("Game (\d+):", line)
        if not m:
            raise ValueError("Line does not start with Game")

        game_id = int(m.group(1))
        add_game = True
        for draw in line[m.span()[1]:].split(';'):
            color_counts = defaultdict(int)
            for colors in draw.split(','):
                pair = colors.strip().split(' ')
                color_counts[pair[1]] += int(pair[0])

            if color_counts['red'] > 12 or color_counts['green'] > 13 or color_counts['blue'] > 14:
                add_game = False
                break

        if add_game:
            result_sum += game_id

    return result_sum