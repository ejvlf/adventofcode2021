import sys
sys.path.append("/home/ejvlf/personal/adventofcode2021")
print(sys.path)

from statistics import median, mean
from common.text_manipulations import TextParser

def fuel_spent (reference_value : float, distance_list : list) -> float:

    fuel_spent = sum(map(lambda distance : abs(distance - reference_value), distance_list))

    return fuel_spent
    
def fuel_spent_part_2(start: int, end: int):

    return sum(range(abs(end - start)+1))

def run():

    #source file loading
    crab_fuel : list = TextParser("day7.txt").load_file_as_ints()
        

    #Part 1
    distance_median = median(crab_fuel)
    part1 = fuel_spent(distance_median, crab_fuel)
    print(f"Part 1 score is {part1}")

    #Part 2
    range_start = min(crab_fuel)
    range_end   = max(crab_fuel)
    best_point = 0
    best_fuel  = 100000000000000000

    for distance in range(range_start,range_end):

        def cost(start : int, end : int):
            return sum(range(abs(end - start)+1))

        current = sum([cost(distance, x) for x in crab_fuel])
        if current < best_fuel:
            best_fuel = current
            best_point = distance

    print(f"Part 2 score is {best_fuel}")
if __name__ == "__main__":

    run()

