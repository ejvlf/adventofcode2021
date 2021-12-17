from copy import deepcopy
from common.text_manipulations import TextParser

def parse_instructions(instruction : str) -> tuple:

    pair, command = instruction.split("->")

    return (pair.rstrip(), command.lstrip())

def create_pairs (polymer : str) -> dict:

    pairs = {}

    for idx in range(len(polymer) -1):

        pair = polymer[idx: idx+2]

        pairs[pair] = 1

    return pairs

        

def run_steps(pairs : dict, steps_list: list, number_of_steps : int = 0) -> dict:

    for _ in range(number_of_steps):

        starting_pairs = pairs.copy()

        for instruction in steps_list:

            valid_instruction = parse_instructions(instruction)
            pair = valid_instruction[0]
            new_char = valid_instruction[1]

            if pair in starting_pairs:

                if pair[0] + new_char in pairs:

                    pairs[pair[0] + new_char] += 1

                else:
                    pairs[pair[0] + new_char] = 1

                
                if new_char + pair[1] in pairs:

                    pairs[new_char + pair[1]] += 1
                
                else:
                    pairs[new_char + pair[1]] = 1

        
    return pairs

            
def count_total_elements(pairs : dict) -> dict:

    counter = {}

    for key, value in pairs.items():

        for char in key:

            if char in counter:

                counter[char] += value
            
            else:

                counter[char] = value

    return counter



def run():
    

    source = TextParser("day14_test.txt").load_file_as_list()
    polymer = source[0]
    chains = [row for row in source if row.find("->") > -1]

    #Part 1
    number_of_steps = 10
    pairs = create_pairs(polymer)
    pairs_after_steps = run_steps(pairs, chains, number_of_steps)

    counted_chars = count_total_elements(pairs_after_steps)

    part1_score = max(counted_chars.values()) - min(counted_chars.values())
    
    print(f"Part 1 score is: {part1_score}")


if __name__ == "__main__":

    run()