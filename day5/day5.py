import sys
sys.path.append("/home/ejvlf/personal/adventofcode2021")
print(sys.path)

from common.text_manipulations import TextParser

def source_file_line_parser (row: str):

    start_end = row.split(" -> ")
    start_coord = (int(start_end[0].rsplit(",")[0]),int(start_end[0].rsplit(",")[1]))
    end_coord = (int(start_end[1].rsplit(",")[0]),int(start_end[1].rsplit(",")[1]))

    return start_coord, end_coord

def generate_line (start_coords : tuple, end_coords: tuple) -> list:

    if start_coords[0] == end_coords[0] and start_coords[1] == end_coords[1]:

        return [(start_coords[0], start_coords[1])]

    elif start_coords[0] == end_coords[0]:

        if start_coords[1] < end_coords[1]:
            y_extension = [(start_coords[0],y) for y in range(start_coords[1],end_coords[1] +1)]
        else:
             y_extension = [(start_coords[0],y) for y in range(end_coords[1], start_coords[1] +1)]
        return y_extension

    
    elif start_coords[1] == end_coords[1]:
        if start_coords[0] < end_coords[0]:
            x_extension = [(x,start_coords[1]) for x in range(start_coords[0],end_coords[0] +1)]
        else:
             x_extension = [(x,start_coords[1]) for x in range(end_coords[0], start_coords[0] +1)]
        return x_extension

    else:

        diagonal = [start_coords]
        last_point = start_coords

        while last_point != end_coords:
            x = last_point[0]
            y = last_point[1]

            if x > end_coords[0]:
                x -= 1

            elif x < end_coords[0]:
                x += 1

            if y > end_coords[1]:
                y -= 1

            elif y < end_coords[1]:
                y += 1

            last_point = (x,y)
            diagonal.append(last_point)

        return diagonal

def dict_counter(unit_to_count, callback) -> int:

    list_to_count = []
        
    for (key, value) in unit_to_count.items():
            
        if callback(value):

            list_to_count.append(key)
        
    return len(list_to_count)

def run():

    #source file loading
    source_list = TextParser("day5.txt", parse_to_ints=False).load_file_as_list()
            
    # Part 1
    lines_in_source = {}

    for i in source_list:

        start_coords, end_coords = source_file_line_parser(i)

        if start_coords[0] == end_coords[0] or start_coords[1] == end_coords[1]:

            full_lines = generate_line(start_coords, end_coords)
            
            for point in full_lines:

                if point in lines_in_source:

                    lines_in_source[point] += 1
                
                else:

                    lines_in_source[point] = 1

    result = dict_counter(lines_in_source, lambda val : val >= 2)

    print(f"Part 1 result: {result}")

    # Part 2
    lines_in_source = {}

    for i in source_list:

        start_coords, end_coords = source_file_line_parser(i)

        full_lines = generate_line(start_coords, end_coords)
            
        for point in full_lines:

            if point in lines_in_source:

                lines_in_source[point] += 1
                
            else:

                lines_in_source[point] = 1

    result = dict_counter(lines_in_source, lambda val : val >= 2)

    print(f"Part 2 result: {result}")


        
if __name__ == "__main__":

    run()

