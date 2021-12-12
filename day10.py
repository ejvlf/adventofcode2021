from common.text_manipulations import TextParser
       
def run():

    #source file loading
    commands_sample : list = TextParser("day10_test.txt", parse_to_ints=False).load_file_as_list()
    commands : list = TextParser("day9.txt", parse_to_ints=False).load_file_as_list()

if __name__ == "__main__":

    run()