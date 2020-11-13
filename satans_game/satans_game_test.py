import unittest

from functools import reduce


class Grid():

    def __init__(self):
        self.size = (1000,1000)
        self.create_grid()

    def get_size(self):
        return (len(self.grid), len(self.grid[0]))

    def create_grid(self):
        grid_fake = []
        (a, b) = self.size
        
        self.grid = [[False for j in range(a)] for i in range(b)]
	

class Satans_GAME_Test(unittest.TestCase):
    
    def test_validate_size(self):
        grid = Grid()
        self.assertEqual(grid.get_size(), (1000,1000))

    def test_all_lights_down(self):
        grid = Grid()
        
        a = False
        for i in range(1000):
            tmp = reduce(lambda x,y : x or y , grid.grid[i])
            a = a or tmp
        self.assertFalse(a)
#        for i in range(1000):
#            for j in range(1000):
#                with self.subTest(i=i*(j + 1)):
#                    self.assertFalse(grid.grid[i][j])

        
        






