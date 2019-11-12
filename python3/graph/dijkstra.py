from collections import namedtuple, deque
import time
import multiprocessing as mp
import itertools

start = time.perf_counter()
 
inf = float('inf')
Edge = namedtuple('Edge', ['start', 'end', 'cost'])

class Graph():
    def __init__(self, edges):
        self.edges = [Edge(*edge) for edge in edges]
        self.vertices = {e.start for e in self.edges} | {e.end for e in self.edges}

    def dijkstra(self, source, dest):
        assert source in self.vertices
        dist = {vertex: inf for vertex in self.vertices}
        previous = {vertex: None for vertex in self.vertices}
        dist[source] = 0
        q = self.vertices.copy()
        neighbours = {vertex: set() for vertex in self.vertices}
        for start, end, cost in self.edges:
            neighbours[start].add((end, cost))
        while q:
            dist1 = splitDict(dist)[0]
            dist2 = splitDict(dist)[1]
            processes = []
            for _ in range(2):
                p = mp.Process(target=parallelFunc, args=(q, dist, dest, neighbours, previous))
                p.start()
                processes.append(p)
            for process in processes:
                process.join()

            # parallelFunc(q, dist, dest, neighbours, previous)
            # u = min(q, key=lambda vertex: dist[vertex])
            # q.remove(u)
            # if dist[u] == inf or u == dest:
            #     break
            # for v, cost in neighbours[u]:
            #     alt = dist[u] + cost
            #     if alt < dist[v]: 
            #         dist[v] = alt
            #         previous[v] = u
        s, u = deque(), dest
        while previous[u]:
            s.appendleft(u)
            u = previous[u]
        s.appendleft(u)
        return s

def parallelFunc(q, dist, dest, neighbours, previous):
    u = min(q, key=lambda vertex: dist[vertex])
    q.remove(u)
    if dist[u] == inf or u == dest:
        return
    for v, cost in neighbours[u]:
        alt = dist[u] + cost
        if alt < dist[v]: 
            dist[v] = alt
            previous[v] = u

def splitDict(d):
    n = len(d) // 2          
    i = iter(d.items())      

    d1 = dict(itertools.islice(i, n))
    d2 = dict(i)                       

    return d1, d2

graph = Graph([("a", "b", 1), ("a", "c", 4),
               ("b", "c", 2), ("b", "g", 4), ("b", "h", 2),
               ("c", "d", 1), ("c", "e", 3),
               ("d", "e", 1), ("d", "f", 3), ("d", "g", 1),
               ("e", "f", 1),
               ("f", "g", 6),
               ("g", "h", 14)])
print(graph.dijkstra("a", "g"))
finish = time.perf_counter()
print(f'finish in {round(finish-start, 2)} seconds')