from common.text_manipulations import TextParser

def decode_unknown_numbers(segment: str, rosetta : dict) -> int:

    solution =  {[0,2,3,5,6] : 5, [0,1,3,4,6]: 2, [0,1,2,3,6]: 3,[0,1,2,3,5,6] : 9, [0,2,3,4,5,6]: 6, [0,1,2,3,4,5]: 0}
    values_to_decode = sorted([rosetta[s] for s in segment])

    return solution[values_to_decode]

def decode_known_numbers(segment : str, rosetta={}) -> int:

    if len(segment) == 2:

        if len(rosetta) > 0:
        
            rosetta[segment[0]] = 2
            rosetta[segment[1]] = 5

        return 1, rosetta

    elif len(segment) == 4:

        if len(rosetta) > 0:
        
            rosetta[segment[0]] = 1
            rosetta[segment[1]] = 2
            rosetta[segment[2]] = 3
            rosetta[segment[3]] = 5

        return 4, rosetta

    elif len(segment) == 7:

        if len(rosetta) > 0:

            for key, value in rosetta.items():

                if value == -1:

                    rosetta[key] = segment[key]

        return 8, rosetta

    elif len(segment) == 3:

        if len(rosetta) > 0:
        
            rosetta[segment[0]] = 0
            rosetta[segment[1]] = 2
            rosetta[segment[2]] = 5

        return 7, rosetta

    else:

        return None


def run():

    numbers = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
    map_char_to_segment = {"a":-1,"b":-1,"c":-1,"d":-1,"e":-1,"f":-1,"g":-1,"h":-1}

    #source file loading
    segments : list = [block.split("|") for block in TextParser("day8.txt", parse_to_ints=False).load_file_as_list()]

    #Part 1
    for segment in segments:

        segment_list : list = segment[1].lstrip().split(" ")

        final_list = list(map(decode_known_numbers,segment_list))

        for number in final_list:

            if number == None:
                continue

            numbers[number[0]] += 1            
        
    
    part1_score = sum(numbers.values()) 

    print(f"Part 1 score is: {part1_score}")

    # Part 2

    for segment in segments:
        
        key_strings = segment[0].rstrip().split(" ")
        display_strings = segment[1].lstrip().split(" ")

        known_values = list(filter(lambda x : len(x) in (2,4,7,3), key_strings))
        unknown_values = list(filter(lambda x : len(x) not in (2,4,7,3), key_strings))

        for value in known_values:

            _, map_char_to_segment = decode_known_numbers(value, map_char_to_segment)

if __name__ == "__main__":

    run()