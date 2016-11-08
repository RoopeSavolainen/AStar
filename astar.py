from grid import Grid
import queue

class AStar:

    def __init__(self, grid):
        self.grid = grid
        self.frontier = []


    def reset(self):
        self.frontier = []
        if self.grid.start is not None and self.grid.target is not None:
            self.grid.uncheck()
            self.grid.start.cost_so_far = 0
            self.grid.start.prev_node = None
            self.frontier.append(self.grid.start)
            self.grid.start.in_frontier = True


    def step(self):
        if len(self.frontier) == 0:
            return
        current = min(self.frontier, key=lambda n: n.cost_so_far + n.heuristic(self.grid.target))

        if current == self.grid.target:
            route_node = current.prev_node
            while route_node != self.grid.start:
                route_node.route = True
                route_node = route_node.prev_node
            return

        self.frontier.remove(current)
        current.in_frontier = False

        for neighbour in current.neighbours():
            new_cost = current.cost_so_far + neighbour.length
            if neighbour.target.cost_so_far is None or new_cost < neighbour.target.cost_so_far:
                neighbour.target.cost_so_far = new_cost
                neighbour.target.prev_node = current

            if not neighbour.target.checked:
                neighbour.target.checked = True
                self.frontier.append(neighbour.target)
                neighbour.target.in_frontier = True


