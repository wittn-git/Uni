from hashlib import new
import random

class Vertex:

    def __init__(self, id, neighbors):
        self.id = id
        self.neighbors = neighbors
        self.discovery_time, self.finish_time = None, None
    
    def to_dot(self):
        s = ''
        for neighbor in self.neighbors:
            s += '\n "{}" -> "{}";'.format(self.to_string(), neighbor.to_string())
        return s+'\n'

    def to_string(self):
        return "{}-{}/{}".format(self.id, self.discovery_time, self.finish_time)

class Graph:

    def __init__(self, size, vertices=None):
        if vertices == None:
            self.vertices = self.generate_vertices(size)
        else: self.vertices = vertices
    
    def get_reversegraph(self):
        rev_vertices = {}
        for i in range(len(self.vertices)):
            rev_vertices[i] = Vertex(i, [])
        for id, vertex in enumerate(self.vertices):
            for neighbor in vertex.neighbors:
                rev_vertices[neighbor].append(rev_vertices[i])
        return Graph(rev_vertices)
    
    def do_depthsearch(self):
        white_nodes, grey_nodes = [v for v in self.vertices], []
        current = 0
        time = 0
        stack = []
        while(True):
            self.vertices[current].discovery_time = time
            time += 1
            grey_nodes.append(current)
            white_nodes.remove(current)
            neighbors = [v for v in self.vertices[current].neighbors if v in white_nodes]
            if len(neighbors) > 0:
                stack.append(current)
                current = neighbors[0]
            else:
                self.vertices[current].finish_time = time
                time += 1
                flag = False
                if len(stack) > 0:
                    while([v for v in self.vertices[current].neighbors if v in white_nodes] == 0 and len(stack) > 0):
                        current = stack.pop()
                else:
                    if len(white_nodes) > 0:
                        current = white_nodes[0]
                    else: break
        pass
            
    def do_kosaraju(self):
        rev_graph = self.get_reversegraph()
        rev_graph.do_depthsearch()

    def generate_vertices(self, size):
        vertices = {}
        for i in range(size):
            neighbors = []
            for j in range(size):
                if i != j and random.random() < 0.3:
                    neighbors.append(j)
            vertices[i] = Vertex(i, neighbors)
        return vertices

    def to_dot(self):
        s = 'digraph{ \n'
        for vertex in self.vertices:
            s += self.vertices[vertex].to_dot()
        return s + '\n }'


graph = Graph(8)
graph.do_depthsearch()
f = open('output.txt', 'w')
f.write(graph.to_dot())
f.close()