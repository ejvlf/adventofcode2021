from common.text_manipulations import TextParser
       
RISK_LEVEL : int = 1

def map_low_points(list_of_points : list) -> list:

    points_to_check = ((-1, 0), (1, 0), (0, -1), (0, 1))
    max_y = len(list_of_points)
    max_x = len(list_of_points[0])
    
    low_points = []
    
    for y in range(max_y):
        for x in range(max_x):

            total_number_of_neighbours = 0
            neighbors_with_high_value = 0
            current_value = int(list_of_points[y][x])

            if x-1 >= 0 and int(list_of_points[y][x -1]) > current_value:

                neighbors_with_high_value += 1

            total_number_of_neighbours += 1 if x-1 >= 0 else 0
            
            if x+1 < max_x and int(list_of_points[y][x +1]) > current_value:

                neighbors_with_high_value += 1

            total_number_of_neighbours += 1 if x+1 < max_x else 0

            if y-1 >= 0 and  int(list_of_points[y-1][x]) > current_value:

                neighbors_with_high_value += 1

            total_number_of_neighbours += 1 if y-1 >= 0 else 0

            if y+1 < max_y and int(list_of_points[y+1][x]) > current_value:

                neighbors_with_high_value += 1

            total_number_of_neighbours += 1 if y+1 < max_y else 0

            if total_number_of_neighbours == neighbors_with_high_value:

                low_points.append(int(list_of_points[y][x]))
           
              
    return low_points


def run():

    #source file loading
    points : list = TextParser("day9.txt", parse_to_ints=False).load_file_as_list()
    part_1_list = list(map(lambda x : x + RISK_LEVEL, map_low_points(points)))

    print(f"Part 1 score: {sum(part_1_list)}")


if __name__ == "__main__":

    run()