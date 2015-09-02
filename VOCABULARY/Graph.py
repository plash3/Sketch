"""
An abstract base class (ABC)

Graph G = (V,E)
 - V = set of vertices
 - E = set of edges i.e. vertex pairs (v,w)

Adjacency lists:
Array Adj of |V| linked lists
 - for each vertex u E V, Adj[u] stores u's neighbours,
   i.e., {v E V | (u,v) E E}
"""

from abc import ABCMeta, abstractmethod

class Graph(object):
    __metaclass__ = ABCMeta

    def __init__(self, name):
        self.name = name
        self.vertices = None

    def __repr__(self):
        return str(self.vertices)

    # Adds a vertex to the Graph.
    @abstractmethod
    def add_vertex(self, vertex):
        pass

    # Gets an adjacency list for a given vertex - its neighbours.
    @abstractmethod
    def adj(self, vertex):
        pass

    # Breadth-first search (BFS) - Graph traversal algorithm;
    # Explore graph level by level from s.
    # Input: A starting vertex s of the Graph.
    # Output: All vertices reachable from s labeled as explored.
    def bfs(self, s):
        level = 0
        s.distance = level
        # a list of explored vertices initially empty;
        # a vertex becomes explored when it leaves a frontier queue
        vstd_vertices = [s]
        # the frontier is implemented as a FIFO queue; it contains
        # a list of nodes discovered (or visited) but not explored
        # (children nodes have not been visited);
        frontier = [s]
        while frontier:
            # a queue of discovered nodes on a current level
            level += 1
            next_level = []
            for u in frontier:
                adjl = self.adj(u)
                for v in adjl:
                    if v not in vstd_vertices:
                        v.distance = level
                        v.parent = u
                        vstd_vertices.append(v)
                        next_level.append(v)
            frontier = next_level
        return vstd_vertices
