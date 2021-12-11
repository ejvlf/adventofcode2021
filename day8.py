from os import sendfile
from common.text_manipulations import TextParser


def part_1_decoder(segment : str) -> int:

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



def map_strings_to_numbers (segments : list) -> dict:
    
    map_char_to_segment = {}

    segments = sorted(segments, key=lambda seg: len(seg))
    map_char_to_segment[8] = segments[9] 

    for segment in segments:

        if len(segment) == 2:

            map_char_to_segment[1] = segment

        elif len(segment) == 4:

            map_char_to_segment[4] = segment

        elif len(segment) == 3:

            map_char_to_segment[7] = segment

        else:

            set_segment = set(segment)

            if len(segment) == 5:
                
                if set_segment.issuperset(set(map_char_to_segment[7])):

                    map_char_to_segment[3] = segment

                elif len(set(map_char_to_segment[4]).difference(set_segment)) == 1:

                    map_char_to_segment[5] = segment

                elif len(set(map_char_to_segment[4]).difference(set_segment)) == 2:

                    map_char_to_segment[2] = segment

            elif len(segment) == 6:

                if len(set(map_char_to_segment[7]).difference(set_segment)) == 1 and len(set(map_char_to_segment[4]).difference(set_segment)) == 1:

                    map_char_to_segment[6] = segment

                elif set_segment.issuperset(set(map_char_to_segment[4])):

                    map_char_to_segment[9] = segment

                elif len(set(map_char_to_segment[4]).difference(set_segment)) == 1:

                    map_char_to_segment[0] = segment
                
    return { "".join(sorted(value)):key for key,value in map_char_to_segment.items() }

def decode_switches(segments_to_decode: list, mapper : dict) -> int:

    numbers_decoded = [ str(mapper["".join(sorted(segment))]) for segment in segments_to_decode]

    return int("".join(numbers_decoded))


def run():

    numbers = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}


    #source file loading
    segments : list = [block.split("|") for block in TextParser("day8.txt", parse_to_ints=False).load_file_as_list()]

    #Part 1
    for segment in segments:

        segment_list : list = segment[1].lstrip().split(" ")

        final_list = list(map(part_1_decoder,segment_list))

        for number in final_list:

            if number == None:
                continue

            numbers[number] += 1            
        
    
    part1_score = sum(numbers.values()) 

    print(f"Part 1 score is: {part1_score}")

    # Part 2
    part2_result = []

    for segment in segments:        
        key_strings = segment[0].rstrip().split(" ")
        display_strings = segment[1].lstrip().split(" ")

        part2_result.append(decode_switches(display_strings, map_strings_to_numbers(key_strings)))

    print(f"Part 2 result is: {sum(part2_result)}")

if __name__ == "__main__":

    run()