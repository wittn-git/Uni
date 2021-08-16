import random

# input: graph g, starting vertex s, goal vertex t
def do_broadsearch(g, s, t):
    stack, discovered = [], []
    current = s
    while(True):
        print(current, stack, discovered)
        if current == t: return True
        for v in g[current]:
            if v not in discovered and v not in stack:
                stack.append(v)
        if len(stack) == 0 or len(discovered) == len(g): return False
        discovered.append(current)
        current = stack.pop(0)

def create_graph(size):
    graph = {}
    for i in range(size):
        graph[i] = []
    for i in range(size):
        for j in range(size):
            if(random.random() < 0.2) and j != i:
                if i not in graph[j]: graph[j].append(i)
                graph[i].append(j)
    return graph, 0, random.randint(0, size-1)

input = create_graph(6)
print(input)
print(do_broadsearch(input[0], input[1], input[2]))