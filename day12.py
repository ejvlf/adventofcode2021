from common.text_manipulations import TextParser
from collections import defaultdict


class Graph:
    def __init__(self):
        self._nodes: defaultdict[str, list] = defaultdict(list)

    def add_edge(self, node: str, neighbor: str):

        self._nodes[node].append(neighbor)
        self._nodes[neighbor].append(node)


    def __dfs_count(self, current_node: str, start_node: str, end_node: str, visited_node: set) -> int:

        # path found
        if current_node == end_node:
            return 1

        # return total of paths found from each neighbor
        return sum(
            self.__dfs_count(neighbor, start_node, end_node, visited_node | {neighbor})
            for neighbor in self._nodes[current_node]
            if not neighbor.lower() or neighbor not in visited_node
        )

    def find_path_count(self, start: str, end: str) -> int:

        return self.__dfs_count(current=start, start=start, end=end, visited={start})

    def __str__(self):
        return str(self._nodes)

    @classmethod
    def from_list(cls, map: list):

        graph = cls()

        for line in map:
            node, neighbor = line.split(",")
            graph.add_edge(node, neighbor)
        return graph


def run():

    source = TextParser("day12_test.txt").load_file_as_list()
    graph = Graph.from_list(source)

    #Part 1
    print(graph.find_path_count("start", "end"))


if __name__ == "__main__":

    run()