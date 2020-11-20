from functools import reduce

class Grid():
    def __init__(self):
        self.size = (1000, 1000)
        self.grid = []
        self.create_grid()

    def get_size(self):
        return (len(self.grid), len(self.grid[0]))

    def create_grid(self) -> None:
        (a, b) = self.size
        self.grid = [[False for j in range(a)] for i in range(b)]

    def _update(self, coordinate1, coordinate2, operation) -> None:
        (x1, y1) = coordinate1
        (x2, y2) = coordinate2
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self._perform_cell_operation(x, y, operation)


    def _perform_cell_operation(self,x,y,operation):
        if operation == 1:
            self.grid[x][y] = True
        elif operation == 0:
            self.grid[x][y] = False
        else:
            self.grid[x][y] = not self.grid[x][y]

    def count_lights_on(self):
        lights_on = 0
        for i in range(1000):
            lights_on += reduce(lambda x, y: x + y, self.grid[i])
        return lights_on