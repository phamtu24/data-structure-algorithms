from collections import namedtuple
import time
import multiprocessing as mp

V = 8
E = 13
inf = float('inf')
Edge = namedtuple('Edge', ['u', 'v'])
Vertex = namedtuple('Vertex', ['title', 'visited'])



class Graph():
    def __init__(self, edges, weights):
        self.edges = [Edge(*edge) for edge in edges]
        self.weights = weights
        # v = {e.u for e in self.edges} | {e.v for e in self.edges}
        self.vertices = [Vertex(title, False) for title in range(V)]
        
        

    def printArray(self, arr):
        for i in range(V):
            print(f'Path to Vertex {i} is {arr[i]}')

    def dijkstra(self, edges, vertices, weights, root):
        root = root._replace(visited=True)
        dist = []
        dist.append(root.title)
        dist[root.title] = 0

        for i in range(V):
            if vertices[i].title != root.title:
                dist.append(vertices[i].title)
                dist[vertices[i].title] = self.findEgde(root, vertices[i], edges, weights)
            else:
                vertices[i] = vertices[i]._replace(visited = True)
        
        for j in range(V):
            h = self.minPath(vertices, dist)
            if h == None : 
                self.printArray(dist)
                return
            u = vertices[h]
        
            for i in range(V):
                if vertices[i].visited == False:
                    c = self.findEgde(u, vertices[i], edges, weights)
                    dist[vertices[i].title] = min(dist[vertices[i].title], dist[u.title] + c)
        self.printArray(dist)


    def findEgde(self, u, v, edges, weights):
        for i in range(E):
            if edges[i].u == u.title and edges[i].v == v.title:
                return weights[i]
        return inf

    def minWeight(self, dist, vertices):
        minimum = inf
        for i in range(len(vertices)):
            time.sleep(0.3)
            if vertices[i].visited == True:
                continue
            elif vertices[i].visited == False and dist[i] < minimum:
                minimum = dist[i]
        return minimum

    def minPath(self, vertices, dist):
        minW = self.minWeight(dist, vertices)
        for i in range(V):
            if vertices[i].visited == False and dist[vertices[i].title] == minW:
                vertices[i] = vertices[i]._replace(visited = True)
                return i 

g = Graph([(0, 1), (0, 2),
               (1, 2), (1, 6), (1, 7),
               (2, 3), (2, 4),
               (3, 4), (3, 5), (3, 6),
               (4, 5),
               (5, 6),
               (6, 7)],
               [1, 4, 2, 4, 2, 1, 3, 1, 3, 1, 1, 6, 14])
root = Vertex(0, False)
start = time.perf_counter()
print(g.dijkstra(g.edges, g.vertices, g.weights, root))
finish = time.perf_counter()
print(f'finish in {finish - start} second(s)')
