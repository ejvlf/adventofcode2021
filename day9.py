from common.text_manipulations import TextParser
       
RISK_LEVEL : int = 1

def map_low_points(list_of_points : list, max_y : int, max_x : int) -> list:

    points_to_check = ((-1, 0), (1, 0), (0, -1), (0, 1))
    
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

                low_points.append((int(list_of_points[y][x]), (x,y)))
           
              
    return low_points

def get_adj_points(x : int, y: int, max_y: int, max_x: int) -> list:
    adj_points = []
    
    if x > 0:
    
        adj_points.append((x - 1, y))
    
    if x < max_x - 1:
    
        adj_points.append((x + 1, y))
    
    if y > 0:
    
        adj_points.append((x, y - 1))
    
    if y < max_y - 1:
    
        adj_points.append((x, y + 1))
    
    return adj_points

def get_adj_basin_points(x : int, y: int, points: list, max_y: int, max_x: int) -> list:
    adj_basin_points = []

    adj_points = get_adj_points(x, y, max_y, max_x)
    
    for adj_point in adj_points:
        adj_x, adj_y = adj_point
        height = int(points[adj_y][adj_x])
        if height < 9:
            adj_basin_points.append(adj_point)
    
    return adj_basin_points

def get_basin_points(point : tuple, points : list, max_y: int, max_x: int, basin_points=[]):
    basin_points = basin_points.copy()
    basin_points.append(point)
    x, y = point

    adj_basin_points = get_adj_basin_points(x, y, points, max_y, max_x)

    for adj_bp in adj_basin_points:

        if adj_bp not in basin_points:
            basin_points = get_basin_points(adj_bp, points, max_y, max_x, basin_points=basin_points)

    return basin_points

def run():

    #source file loading
    points : list = TextParser("day9.txt", parse_to_ints=False).load_file_as_list()
    max_y = len(points)
    max_x = len(points[0])

    # Part 1
    low_points = map_low_points(points, max_y, max_x)
    part_1_score = sum(list(map(lambda x : x[0] + RISK_LEVEL, low_points)))

    print(f"Part 1 score: {part_1_score}")

    # Part 2
    basin_sizes = []
    for low_point in low_points:

        basin_points = get_basin_points(low_point[1], points, max_y, max_x)
        basin_sizes.append(len(basin_points))

    basin_sizes.sort(reverse=True)
    three_largest_basins = basin_sizes[:3]
    part2_score = 1
    
    for size in three_largest_basins:
    
        part2_score *= size
    
    print("Part 2 score:", part2_score)

if __name__ == "__main__":

    run()