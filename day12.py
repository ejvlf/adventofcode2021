from common.text_manipulations import TextParser
from collections import defaultdict


def passage_pathing(cave_map):
    
    # Recursive depth-first search
    def dfs(cave_map : , visited, loc, visited_small):
        
        new_visited = visited.copy()
        if loc == "end":
            return 1
        if loc in new_visited:
            new_visited[loc] += 1
        else:
            new_visited[loc] = 1

        # For every node that the current location points to...
        # If going to an upper case node, just go, no worries
        # If going to a lower case node, make sure it's not visited already
        paths = 0
        for to in cave_map[loc]:
            if to.isupper():
                paths += dfs(cave_map, new_visited, to, visited_small)
            elif to not in new_visited:
                paths += dfs(cave_map, new_visited, to, visited_small)
            # For part 2 you can also go to a lower case node if you haven't been
            # twice already or to another node twice
            elif to in new_visited and new_visited[to] < 2 and not visited_small:
                paths += dfs(cave_map, new_visited, to, True)
        
        return paths

    visited = {}
    return dfs(cave_map, visited, "start", False)



def run():

    source = TextParser("day12_test.txt").load_file_as_list()
    graph = Graph.from_list(source)
    cave_map = defaultdict(list)
    with open('Advent of Code/test.txt', 'r') as input:
        for line in input:
            connection = line.rstrip().split("-")

            # Create a map of every left node to every right node an vise versa
            # If one of the nodes is start, only keep track of what start goes to
            # Similarly if one node is end, only keep track of what goes to end
            if connection[1] != "start" and connection[0] != "end":
                cave_map[connection[0]].append(connection[1])
            if connection[0] != "start" and connection[1] != "end":
                cave_map[connection[1]].append(connection[0])
    
    print(passage_pathing(cave_map))


if __name__ == "__main__":

    run()