from common.text_manipulations import TextParser

def decode_numbers(segment : str) -> int:

    if len(segment) == 2:

        return 1

    elif len(segment) == 4:

        return 4

    elif len(segment) == 7:

        return 8

    elif len(segment) == 3:

        return 7

    else:

        return None


def run():

    numbers = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}

    #source file loading
    segments : list = [block.split("|") for block in TextParser("day8.txt", parse_to_ints=False).load_file_as_list()]

    #Part 1
    for segment in segments:

        segment_list : list = segment[1].lstrip().split(" ")

        final_list = list(map(decode_numbers,segment_list))

        for number in final_list:

            if number == None:
                continue

            numbers[number] += 1            
        
    
    part1_score = sum(numbers.values()) 

    print(f"Part 1 score is: {part1_score}")








if __name__ == "__main__":

    run()

