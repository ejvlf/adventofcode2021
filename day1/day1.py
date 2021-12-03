import sys
sys.path.append("/home/ejvlf/personal/adventofcode2021")
print(sys.path)

#Nice. Python is not a functional language.
sys.setrecursionlimit(5000)

import logging
from common.text_manipulations import TextParser
import common.fancy_math_operations



NO_PREVIOUS_MEASUREMENT : str = "N/A"
INCREASED : str = "increased"
DECREASED : str = "decreased"
NO_CHANGE: str = "no change"
MEASUREMENT_WINDOW : int = 3
MEASUREMENT_STEP: int = 1

def map_depths (source : list) -> list:

    depth_category = []

    for idx, depth in enumerate(source):

        if idx == 0:

            depth_category.append((idx, NO_PREVIOUS_MEASUREMENT))
            continue

        """
        if depth is not the first one keep going through the happy path
        with each depth compare a previous one and classify it
        """

        depth_comparison = ""

        if source[idx-1] < depth:

            depth_comparison = INCREASED

        elif source[idx-1] > depth:

            depth_comparison = DECREASED
        
        else:
             depth_comparison = NO_CHANGE

        depth_category.append((idx, depth_comparison))

    return depth_category


def add_depth_window(list_of_depths: list, list_of_windowed_depths = [], start_idx = 0):

    depths_to_group = []
    idx_counter = 0

    while len(depths_to_group) < MEASUREMENT_WINDOW:

        depths_to_group.append(list_of_depths[start_idx + idx_counter])

        idx_counter += 1

    list_of_windowed_depths.append(sum(depths_to_group))

    if len(list_of_depths) - (start_idx) > 3:
        
        add_depth_window(list_of_depths, list_of_windowed_depths, start_idx + MEASUREMENT_STEP)

    return list_of_windowed_depths

      

def run():

    #source file loading
    source_list = TextParser("day1.txt").load_file_as_list()

    #map depths
    list_of_depths = map_depths(source_list)

    #First part
    total_for_first_part : int = common.fancy_math_operations.count_matching(INCREASED, list_of_depths)

    print(f"Part 1 result: {str(total_for_first_part)}")

    #Second part
    windowed_depths = map_depths(add_depth_window(source_list))
    total_for_second_part = common.fancy_math_operations.count_matching(INCREASED, windowed_depths)

    print(f"Part 2 result: {str(total_for_second_part)}")


if __name__ == "__main__":

    run()