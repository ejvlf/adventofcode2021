from common.text_manipulations import TextParser

# print all found paths
def print_paths(paths):
    for i in sorted(paths):
        print(",".join(i))


def dfs(graph, start, end, path, part2):
    path.append(start)

    if start == end: # found a path to end
        return [path]
    if start not in graph or end not in graph: # stop if start or end don't exist
        return []

    paths = []
    for node in graph[start]:
        # part 1: large caves can be visited indefinitely, small caves only once
        # part2=True activates the condition for part 2
        if node.isupper(): # visit big caves indefinitely
            paths.extend(dfs(graph, node, end, path.copy(), part2))
        elif node not in path: # visit small caves only once
            paths.extend(dfs(graph, node, end, path.copy(), part2))
        # at this point the small cave (node) was visited once
        # create subpaths like in part 1
        elif part2 and node != "start": 
            paths.extend(dfs(graph, node, end, path.copy(), part2=False))
            
    return paths

def run():

    caves = {}

    source = TextParser("day12.txt").load_file_as_list()
    for line in source:
        v = line.strip().split('-')
        if v[0] not in caves:
            caves[v[0]] = [v[1]]
        else:
            caves[v[0]].append(v[1])
        if v[1] not in caves:
            caves[v[1]] = [v[0]]
        else:
            caves[v[1]].append(v[0])


    paths1 = dfs(caves, 'start', 'end', path=[], part2=False)
    paths2 = dfs(caves, 'start', 'end', path=[], part2=True)

    print(f"Part 1: number of distinct paths: {len(paths1)}")
    print(f"Part 2: number of distinct paths: {len(paths2)}")    


if __name__ == "__main__":

    run()