import sys
import random
import dijkstra
import Edge
import Vertex

def main():
    r = 10
    m = 15
    n = 10

    edges = []
    random.seed()
    print "EDGES:"
    for i in xrange(m):
        s = ''
        for j in xrange(n):
            d = Edge.Edge( (i,j), (i+1,j), random.randint(1, r) )
            edges.append(d)
            s += ' ' + str(d)
            d = Edge.Edge( (i,j), (i,j+1), random.randint(1, r) )
            edges.append(d)
            s += ' ' + str(d)
        print s
    print

    s = Vertex.Vertex((0, 0))
    s.distance = 0
    dijkstra.dijkstra(edges, s)

if __name__ == "__main__":
    sys.exit(main())
