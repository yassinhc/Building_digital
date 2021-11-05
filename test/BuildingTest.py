import unittest

import sys
sys.path.append('..')

from src import Building


class Test_Building(unittest.TestCase):
    
    def test_Building_empty(self):
        building = Building.Building([])
        nb = building.getLenFloor()
        self.assertEqual(nb,0)

 

if __name__ == '__main__':
    unittest.main()