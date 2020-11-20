import unittest
from grid import Grid

class SatansGAMETest(unittest.TestCase):

    def setUp(self) -> None:
        self.grid = Grid()

    def test_validate_size(self):
        self.assertEqual(self.grid.get_size(), (1000,1000))

    def test_all_lights_down(self):
        lights_on = self.grid.count_lights_on()
        self.assertEqual(lights_on, 0)

    def test_turn_on_one_light(self):
        self.grid._update((0, 0), (1, 1), 1)
        self.assertEqual(self.grid.grid[0][0], True)

    def test_turn_off_one_light(self):
        self.grid._update((0, 0), (1, 1), 1)
        self.assertEqual(self.grid.grid[0][0], True)

        self.grid._update((0, 0), (1, 1), 0)
        self.assertEqual(self.grid.grid[0][0], False)

    def test_togle_one_light(self):
        self.grid._update((0, 0), (1, 1), 2)
        self.assertEqual(self.grid.grid[0][0], True)

        self.grid._update((0, 0), (1, 1), 2)
        self.assertEqual(self.grid.grid[0][0], False)

    def test_all_on(self):
        self.grid._update((0, 0), (999, 999), 1)
        lights_on = self.grid.count_lights_on()
        self.assertEqual(lights_on, 1000000)

    def test_all_off(self):
        lights_on = self.grid.count_lights_on()
        self.assertEqual(lights_on, 0)

    def test_toggle_all(self):
        args = ((0, 0), (999, 999), 2)
        self.grid._update(*args)
        lights_on = self.grid.count_lights_on()
        self.assertEqual(lights_on, 1000000)

        self.grid._update(*args)
        lights_on = self.grid.count_lights_on()
        self.assertEqual(lights_on, 0)

    def test_enum_lights_on(self):
        args = ((0, 0), (999, 999), 2)
        self.grid._update(*args)

        lights_on = self.grid.count_lights_on()
        self.assertEqual(lights_on, 1000000)