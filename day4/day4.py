import sys
sys.path.append("/home/ejvlf/personal/adventofcode2021")
print(sys.path)

from common.text_manipulations import TextParser


def run():

    #source file loading
    source_list = TextParser("day3.txt", parse_to_ints=False).load_file_as_list()

    # Part 1 

        
if __name__ == "__main__":

    run()