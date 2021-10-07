import unittest

import sys
sys.path.append('..')


import src.Area as Area

class Test_Area(unittest.TestCase):
    def test_get_list_elements(self):
        area = Area.Area([])
        list_elem = area.getListElements()
        self.assertEqual([], list_elem)


    def test_nb_elements(self):
        area = Area.Area([])
        nb_elem = area.getNbElements()
        self.assertEqual(0, nb_elem)

        
        
        
        
if __name__ == '__main__':
    unittest.main()
