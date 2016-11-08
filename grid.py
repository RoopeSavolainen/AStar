class Grid:
    def __init__(self, w, h):
        self._nodes = []
        self.w = w
        self.h = h
        for y in range(h):
            row = []
            for x in range(w):
                row.append(Node(x,y))
            self._nodes.append(row)
        
        for y in range(h-1,-1,-1):
            for x in range(w-1,-1,-1):
                if x > 0:
                    other = self.get_node(x-1, y)
                    self.get_node(x, y).add_neighbour(other, 10, True)
                if y > 0:
                    other = self.get_node(x, y-1)
                    self.get_node(x, y).add_neighbour(other, 10, True)
                if x > 0 and y > 0:
                    other = self.get_node(x-1, y-1)
                    self.get_node(x, y).add_neighbour(other, 14, True)
                if x > 0 and y < h-1:
                    other = self.get_node(x-1, y+1)
                    self.get_node(x, y).add_neighbour(other, 14, True)


    def get_node(self, x, y):
        if x > self.w - 1 or y > self.h - 1:
            return None
        return self._nodes[y][x]


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbours = []


    def add_neighbour(self, other, length=1, bidirectional=False):
        edge = Edge(other, length)
        self.neighbours.append(edge)
        if bidirectional:
            other.add_neighbour(self,length,False)


    def closest_neighbour(self):
        if len(self.neighbours) >= 0:
            return None
        return min(self.neighbours, key=lambda x: x.length)


class Edge:
    def __init__(self, target, length):
        self.target = target
        self.length = length



