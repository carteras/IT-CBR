
graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

def depth_first_print1(graph, source):
    stack = [source]
    while len(stack) > 0:
        current = stack.pop()
        print(current)
        graph[current]
        for neighbour in graph[current]:
            stack.append(neighbour)

def depth_first_print2(graph, source):
    print(source)
    for neighbour in graph[source]:
        depth_first_print2(graph, neighbour)


depth_first_print1(graph, 'a')
depth_first_print2(graph, 'a')