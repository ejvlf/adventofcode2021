from common.text_manipulations import TextParser
import re
from statistics import median

ILLEGAL_CHAR_TO_POINTS = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

AUTOCOMPLETED_CHAR_TO_POINTS = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }

def run():

    #source file loading
    commands : list = TextParser("day10.txt", parse_to_ints=False).load_file_as_list()

    non_corrupt_lines = []

    # Part 1
    consec_complete_brackets_regex = "\(\)|\[\]|{}|<>"


    score = 0
    for line in commands:
        while re.search(consec_complete_brackets_regex, line):
            line = re.sub(consec_complete_brackets_regex, "", line)
        first_illegal_char = ""
        for char in line:
            if char in ")]}>":
                first_illegal_char = char
                break
        if first_illegal_char:
            score += ILLEGAL_CHAR_TO_POINTS[first_illegal_char]
        else:
            non_corrupt_lines.append(line)

    print(f"Part 1 score: {score}")

    # Part 2

    scores = []
    for line in non_corrupt_lines:
        while re.search(consec_complete_brackets_regex, line):
            line = re.sub(consec_complete_brackets_regex, "", line)
        mapping_table = line.maketrans("([{<", ")]}>")
        missing_characters = line.translate(mapping_table)[::-1]
        score = 0
        for char in missing_characters:
            score *= 5
            score += AUTOCOMPLETED_CHAR_TO_POINTS[char]
        scores.append(score)

    middle_score = median(scores)
    print(f"Part 2 score: {middle_score}")



if __name__ == "__main__":

    run()