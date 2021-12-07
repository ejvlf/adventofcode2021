import sys
sys.path.append("/home/ejvlf/personal/adventofcode2021")
print(sys.path)

from statistics import median
from common.text_manipulations import TextParser

def run():

    #source file loading
    crab_fuel : list = TextParser("day7.txt").load_file_as_ints()
    
    distance_median = median(crab_fuel)
    fuel_spent = sum(map(lambda distance : abs(distance - distance_median), crab_fuel))

    #Part 1
    print(f"Part 1 score is {fuel_spent}")

if __name__ == "__main__":

    run()

