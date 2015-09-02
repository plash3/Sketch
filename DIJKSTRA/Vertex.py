"""
class Vertex has -
- value - it can be a String, a number or any other type
  depending on the task at hand
- level - the distance to the initial node
- parent - the parent of the vertex
"""

class Vertex():

    def __init__(self, value):
        # Since the exploration has not started, set
        # the distance to the initial node as INFINITY;
        # the parent of the vertex has not been discovered.
        self.value = value
        self.distance = -1
        self.parent = None

    # Defines tailored objects comparing. Assumes
    # that the other argument is a Vertex.
    def __eq__(self, other):
        if isinstance(other, Vertex):
            return self.value == other.value
        else:
            # try to compare itself with an instance
            # of any other class to avoid an error
            return self.value == other

    def __ne__(self, other):
        if isinstance(other, Vertex):
            return self.value != other.value
        else:
            return self.value != other

    # A min heap is used using dist-values as keys;
    # hence the LESS/GREATER THAN methods depend on distance.
    def __lt__(self, other):
        if isinstance(other, Vertex):
            return self.distance < other.distance
        else:
            return self.distance < other

    def __gt__(self, other):
        if isinstance(other, Vertex):
            return self.distance > other.distance
        else:
            return self.distance > other

    def __le__(self, other):
        if isinstance(other, Vertex):
            return self.distance <= other.distance
        else:
            return self.distance <= other

    def __ge__(self, other):
        if isinstance(other, Vertex):
            return self.distance >= other.distance
        else:
            return self.distance >= other

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return "'" + str(self.value) + ': ' +  str(self.distance) + (': ' + str(self.parent.value) if self.parent else '') + "'"
