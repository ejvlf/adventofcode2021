import sys
sys.path.append("/home/ejvlf/personal/adventofcode2021")
print(sys.path)
from copy import deepcopy

from common.text_manipulations import TextParser

LANTERNFISH_RESET_TIMER : int = 6
LANTERNFISH_STARTING_TIMER : int = 8

# First
def run_day (school_of_fish : list, number_of_day : int) -> list:

    work_list = deepcopy(school_of_fish)

    print(f"Start of day: {number_of_day}")

    for i, fish in enumerate(school_of_fish):

        fish -= 1

        if fish < 0:

            work_list[i] = LANTERNFISH_RESET_TIMER

            work_list.append(LANTERNFISH_STARTING_TIMER)

        else:

            work_list[i] = fish        

    print(f"Finished day {number_of_day}")
    
    return work_list

#Second

def run_day_dicts(original_school_of_fish : dict, day : int):
    
    print(f"Start of day: {day}")

    final_condition = original_school_of_fish[0]
    
    original_school_of_fish[0] = original_school_of_fish[1]
    original_school_of_fish[1] = original_school_of_fish[2]
    original_school_of_fish[2] = original_school_of_fish[3]
    original_school_of_fish[3] = original_school_of_fish[4]
    original_school_of_fish[4] = original_school_of_fish[5]
    original_school_of_fish[5] = original_school_of_fish[6]
    original_school_of_fish[6] = final_condition + original_school_of_fish[7]
    original_school_of_fish[7] = original_school_of_fish[8]
    original_school_of_fish[8] = final_condition

    print(f"Finished day {day}")

    return original_school_of_fish

def run():

    #source file loading
    original_school_of_fish : list = TextParser("day6.txt").load_file_as_ints()

    for day in range(80):

        original_school_of_fish = run_day(original_school_of_fish, day)

    # Part 1
    print(f"Part 1 result: {len(original_school_of_fish)}")    
    


    # Part 2
    original_school_of_fish : list = TextParser("day6.txt").load_file_as_ints()
    fish_dict : dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    
    for fish in original_school_of_fish:
        fish_dict[fish] += 1

    for day in range(256):

        fish_dict = run_day_dicts(fish_dict, day)

    print(f"Part 2 result: {sum(fish_dict.values())}")

        
if __name__ == "__main__":

    run()

