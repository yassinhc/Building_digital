#from Building import Building
from src import Building

import unittest


class Test_Building(unittest.TestCase):
    def test_Building_empty(self):
        building = Building()
        nb = building.getLenArea()
        self.assertEqual(nb,0)

 

if __name__ == '__main__':
    unittest.main()