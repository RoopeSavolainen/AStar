from math import sqrt

class Grid:
    def __init__(self, w, h):
        self._nodes = []
        self.w = w
        self.h = h

        self.start = None
        self.target = None

        # Builds the nodes for the grid
        for y in range(h):
            row = []
            for x in range(w):
                row.append(Node(x,y))
            self._nodes.append(row)

        # Creates edges between nodes
        for y in range(h-1,-1,-1):
            for x in range(w-1,-1,-1):
                if x > 0:
                    other = self.get_node(x-1, y)
                    self.get_node(x, y).add_neighbour(other, 1, True)
                if y > 0:
                    other = self.get_node(x, y-1)
                    self.get_node(x, y).add_neighbour(other, 1, True)
                if x > 0 and y > 0:
                    other = self.get_node(x-1, y-1)
                    self.get_node(x, y).add_neighbour(other, 1.4, True)
                if x > 0 and y < h-1:
                    other = self.get_node(x-1, y+1)
                    self.get_node(x, y).add_neighbour(other, 1.4, True)


    # Gets the node with coordinates x, y
    def get_node(self, x, y):
        if x > self.w - 1 or y > self.h - 1:
            return None
        return self._nodes[y][x]


    def uncheck(self):
        for x in range(self.w):
            for y in range(self.h):
                n = self.get_node(x,y)
                n.checked = False
                n.in_frontier = False
                n.route = False
                n.prev = None
                n.cost_so_far = None


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._neighbours = []
        self.enabled = True

        self.in_frontier = False
        self.checked = False
        self.route = False
        self.cost_so_far = 0

        prev_node = None


    # Adds a new edge
    # Takes another node and the length of the edge as a parameter
    # If you want to automatically create a mirrored edge back (e.g create a bidirectional edge), use bidirectional=True
    def add_neighbour(self, other, length=1, bidirectional=False):
        edge = Edge(other, length)
        self._neighbours.append(edge)
        if bidirectional:
            other.add_neighbour(self,length,False)


    # Returns an edge to the closest non-disabled neighbour
    # Don't know if this is needed, but it's provided for convenience
    def closest_neighbour(self):
        if len(self._neighbours) >= 0:
            return None
        return min(self.neighbours(), key=lambda x: x.length)


    # Returns a list of edges leading to non-disabled nodes
    def neighbours(self):
        l = []
        for n in self._neighbours:
            if n.target.enabled and not n.target.checked:
                l.append(n)
        return l


    # Heuristics function used in A* (just a distance between the two nodes
    # Takes another node as a parameter
    def heuristic(self, other):
        dist = sqrt((self.x-other.x)**2 + (self.y-other.y)**2)
        return round(dist,1)


# Edge is a simple unidirectional connection between two nodes
# Has the target and the length of the edge as members
# You can create a bidirectional edge by passing True to the 'bidirectional' parameter in add_neighbour()
class Edge:
    def __init__(self, target, length):
        self.target = target
        self.length = length


