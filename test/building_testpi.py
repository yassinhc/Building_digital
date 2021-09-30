
import sys
sys.path.append('..')

from src import Building
#from Building import Building

import unittest


class Test_Building(unittest.TestCase):
    def test_Building_empty(self):
        building = Building.Building([])
        nb = building.getLenArea()
        self.assertEqual(nb,0)

 

if __name__ == '__main__':
    unittest.main()