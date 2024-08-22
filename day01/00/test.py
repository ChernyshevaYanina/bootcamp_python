import unittest
from functional_purse import add_ingot, get_ingot, empty

class TestPurse(unittest.TestCase):
    def test_add_ingot_1(self):
        new_purse = {}
        new_purse = add_ingot(new_purse)
        self.assertEqual(new_purse, {"gold_ingots": 1})
        
    def test_add_ingot_2(self):
        purse = {"gold_ingots": 10, "stones": 5, "silver_ingots": 7}
        new_purse = add_ingot(purse)
        new_purse = add_ingot(new_purse)
        self.assertEqual(new_purse, {"gold_ingots": 12,  "stones": 5, "silver_ingots": 7})
    
    def test_add_ingot_3(self):
        purse = {"gold_ingots": -3}
        new_purse = add_ingot(purse)
        self.assertEqual(new_purse, {"gold_ingots": 1})
        
    def test_get_ingot_1(self):
        purse = {"gold_ingots": 10, "stones": 5, "silver_ingots": 7}
        purse = get_ingot(purse)
        self.assertEqual(purse, {"gold_ingots": 9,  "stones": 5, "silver_ingots": 7})
    
    def test_get_ingot_2(self):
        purse = {"gold_ingots": 0}
        purse = get_ingot(purse)
        self.assertEqual(purse, {})
        
    def test_get_ingot_2(self):
        purse = {"gold_ingots": -3}
        purse = get_ingot(purse)
        self.assertEqual(purse, {})
    
    def test_empty(self):
        purse = {"gold_ingots": 20, "stones" : 10}
        purse = empty(purse)
        self.assertEqual(purse, {})
    
    def test_all(self):
        purse = {"gold_ingots": 20, "stones" : 10}
        purse = add_ingot(get_ingot(add_ingot(empty(purse))))
        self.assertEqual(purse, {"gold_ingots": 1})

    
if __name__ == '__main__':
    unittest.main()
