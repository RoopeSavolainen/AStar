from grid import Grid
import queue

class AStar:

    def __init__(self, grid):
        self.grid = grid
        self.frontier = []


    def reset(self):
        if self.grid.start is not None and self.grid.target is not None:
            self.grid.uncheck()
            self.grid.start.cost_so_far = 0
            self.frontier.append(self.grid.start)


    def step(self):
        if len(self.frontier) == 0:
            return
        current = min(self.frontier, key=lambda n: n.cost_so_far + n.heuristic(self.grid.target))
        self.frontier.remove(current)
        for neighbour in current.neighbours():
            neighbour.target.checked = True
            neighbour.target.cost_so_far = current.cost_so_far + neighbour.length
            self.frontier.append(neighbour.target)


