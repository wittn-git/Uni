import random

class Vertex:

    def __init__(self, id):
        self.visited = False
        self.distance = float('inf')
        self.id = id
    
    def set_edges(self, edges):
        self.edges = edges

    def to_dot(self):
        s = ''
        for edge in self.edges:
            s += '\n "Node{} | {}" -> "Node{} | {}" [label="{}"];'.format(self.id, self.distance, edge.id, edge.distance, self.edges[edge])
        return s+'\n'

class Graph:

    def __init__(self, size):
        self.vertices = self.generate_vertices(size)
    
    def do_dijkstra(self):
        current = self.vertices[0]
        current.distance = 0
        while(True):
            current.visited = True
            for neighbor in current.edges:
                if current.distance + current.edges[neighbor] < neighbor.distance:
                    neighbor.distance = current.distance + current.edges[neighbor]

            unvisited = [vertex for vertex in self.vertices.values() if vertex.visited == False]
            if len(unvisited) == 0: break
            current = min(unvisited, key=lambda vertex: vertex.distance)

    def generate_vertices(self, size):
        vertices = {}
        for i in range(size):
            vertices[i] = Vertex(i)
        for i in range(size):
            edges = {}
            for j in range(size):
                if i != j and random.random() < 0.3:
                    edges[vertices[j]] = random.randint(0, 100)
            vertices[i].set_edges(edges)
        return vertices


    def to_dot(self):
        s = 'digraph{ \n'
        for vertex in self.vertices:
            s += self.vertices[vertex].to_dot()
        return s + '\n }'


graph = Graph(8)
graph.do_dijkstra()
f = open('output.txt', 'w')
f.write(graph.to_dot())
f.close()