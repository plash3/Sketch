import minheap_utility
import Vertex

# Dijkstra's algorithm

# for a given set of Edges - E get an adjacency list of a vertex u
def adj(E, u):
    adjl = {}
    for d in E:
        if d.value1 == u.value:
            adjl[d.value2] = d.length
        elif d.value2 == u.value:
            adjl[d.value1] = d.length
    return adjl

# check if the vertex - value is in unvisited vertices
def check_path(unvstd_list, value, dist, u):
    res = False
    for i in xrange(len(unvstd_list)):
        v = unvstd_list[i]
        if v.value == value:
            res = True
            if v.distance > dist:
                # a shorter path to v has been found
                v.distance = dist
                v.parent = u
                minheap_utility.sift_up(unvstd_list, i)
            break
    return res

# Input: Graph G(V, E) with vertices V and edges E
# for a given source node - s finds the shortest paths
# between that node and other vertices reachable from s
def dijkstra(E, s):
    # a list of visited vertices initially empty
    visited_list = []
    # make heap out of unvisited vertices using dist-values as values
    unvstd_list = [s]
    print 'UNVISITED LIST:'
    while unvstd_list:
        u = minheap_utility.delete_min(unvstd_list)
        visited_list.append(u)
        adjl = adj(E, u)
        for value, lngth in adjl.iteritems():
            if value in visited_list:
                continue
            dist = u.distance + lngth
            if not check_path(unvstd_list, value, dist, u):
                v = Vertex.Vertex(value)
                v.distance = dist
                v.parent = u
                minheap_utility.insert(unvstd_list, v)
        print unvstd_list
    print 'VISITED:'
    print visited_list
