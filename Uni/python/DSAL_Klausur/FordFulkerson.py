import random

class Vertex:

    def __init__(self, id, edges):
        self.visited = False
        self.id = id
        self.edges = edges

    def to_dot(self, vertices):
        s = ''
        for v in self.edges:
            s += '\n "{}" -> "{}" [label="{}"];'.format(self.id, vertices[v].id, self.edges[v])
        return s+'\n'

class Network:

    def __init__(self, size, vertices = None):
        if vertices == None: self.vertices = self.generate_vertices(size)
        else: self.vertices = vertices
        
    def do_fordfulkerson(self):
        flow_value = 0
        flow = self.find_flow()
        while(flow != None):
            self.augment_flow(flow)
            flow_value += flow[1]
            flow = self.find_flow()
        return flow_value

    def find_flow(self):
        flow = []
        value = float("Inf")
        current = 0
        grey_nodes = []
        while(True):
            if current == len(self.vertices)-1: return flow + [len(self.vertices)-1], value
            if current not in grey_nodes: grey_nodes.append(current)
            neighbors = [(v,self.vertices[current].edges[v]) for v in self.vertices[current].edges if v not in grey_nodes and self.vertices[current].edges[v]>0]
            if len(neighbors) > 0:
                flow.append(current)
                value = min(neighbors[0][1], value)
                current = neighbors[0][0]
            else:
                if len(flow) == 0: return None
                else: current = flow.pop()

    def augment_flow(self, flow):
        if flow == None: return None
        for i in range(len(flow[0])-1):
            frm = flow[0][i]
            to = flow[0][i+1]

            self.vertices[frm].edges[to] = self.vertices[frm].edges[to] - flow[1]
            self.vertices[to].edges[frm] = flow[1]

    def generate_vertices(self, size):
        vertices = {}
        for i in range(size):
            edges = {}
            if i != size-1:
                for j in range(size):
                    if i != j and random.random() < 0.3 and j != 0:
                        edges[j] = random.randint(0, 20)
                if len(edges) == 0:
                    j = random.randint(0, size-1)
                    while(j == i):
                        j = random.randint(0, size-1)
                    edges[j] = random.randint(0, 20)
            vertices[i] = Vertex(i, edges)
        return vertices

    def to_dot(self):
        s = 'digraph{ \n'
        for vertex in self.vertices:
            s += self.vertices[vertex].to_dot(self.vertices)
        return s + '\n }'

network = Network(5)

f = open('output.txt', 'w')
f.write(network.to_dot())
f.close()

print(network.do_fordfulkerson())

f = open('output1.txt', 'w')
f.write(network.to_dot())
f.close()