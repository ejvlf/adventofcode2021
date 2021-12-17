from common.text_manipulations import TextParser

def create_visited_map (source : list) -> dict:

    visited = {}

    for y in range(len(source)):

        for x in range(len(source[0])):

            if x == 0 and y == 0:
                visited[(x,y)] = (True, 0)
                continue

            visited[(x,y)] = (False, int(source[y][x]))
    

    return visited

def run_algorithm(graph : dict, final_node : tuple, max_x : int, max_y : int):

    current_node = (0,0)
    neighbours = [(0,1), (0,-1), (1,0), (-1,0)]
    total_score = graph[current_node][1]
    
    while current_node != final_node:

        scores = []

        for neighbour in neighbours:

            if (current_node[0] + neighbour[0] >= 0 and current_node[0] + neighbour[0] <= max_x) \
                    and (current_node[1] + neighbour[1] >= 0 and current_node[1] + neighbour[1] <= max_y):
                    
                    tentative_coords = (current_node[0] + neighbour[0], current_node[1] + neighbour[1])
                    tentative_node = graph[tentative_coords]

                    if tentative_node[0] == False:
                        tentative_node = (True, tentative_node[1])
                        scores.append((tentative_coords, tentative_node[1] + total_score))
                        graph[tentative_coords] = tentative_node
                    else:
                        continue
        best_score = 99999999999999
        for visited_nodes in scores:

            if visited_nodes[1] < best_score:

                best_score = visited_nodes[1]
                current_node = visited_nodes[0]

        total_score += best_score

    return total_score      

def run():
    

    source = TextParser("day15_test.txt", parse_to_ints=False).load_file_as_list()
    start_coord = (0,0)
    end_coord = (len(source[0]),len(source))

    visited = create_visited_map(source)
    score = run_algorithm(visited, end_coord, end_coord[0], end_coord[1])    


if __name__ == "__main__":

    run()