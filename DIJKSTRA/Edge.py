"""
An edge is a vertex pair (v,w)
Value is any property that uniquely defines a vertex in a Graph.
In this particular case it is a tuple of coordinates (x,y).
"""

class Edge():

    # the length of the edge is the distance between the neighbour-nodes
    def __init__(self, value1, value2, value):
        self.value1 = value1
        self.value2 = value2
        self.length = value

    # Defines tailored objects comparing. Assumes that the other
    # argument is an Edge.
    def __gt__(self, other):
        if self.value1 == other.value1:
            return self.value2 > other.value2
        else:
            return self.value1 > other.value1

    # Defines tailored objects comparing. Assumes that the other
    # argument is an Edge.
    def __eq__(self, other):
        if isinstance(other, Edge):
            return self.value1 == other.value1 and self.value2 == other.value2
        else:
            return False

    def __hash__(self):
        return hash( (self.value1, self.value2) )

    def __repr__(self):
        return "'" + str(self.value1) + ': ' + str(self.value2) + ': ' +  str(self.length) + "'"
