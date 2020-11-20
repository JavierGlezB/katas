from grid import Grid
from read_instructions import get_instructions

def run():
    instructions = get_instructions()
    grid = Grid()
    for operation, coordinate1, coordinate2 in instructions:
        grid._update(coordinate1, coordinate2, operation)

    print("Lights on: {}".format(grid.count_lights_on()))

if __name__ == '__main__':
    run()

















