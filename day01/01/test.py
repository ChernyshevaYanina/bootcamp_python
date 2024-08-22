import unittest
from splitwise import split_booty

class TestSplitwise(unittest.TestCase):
    def test_split_booty(self):
        purse1 = {"gold_ingots": 3}
        purse2 = {"silver_ingots": 5, "gold_ingots": 10}
        purse3 = {"stones": 15}
        purse4 = {"gold_ingots": 1}
        purse5 = {"gold_ingots": 1, "aplles" : 7}
        
        ans1, ans2, ans3 = split_booty(purse1, purse2, \
            purse3,  purse4,  purse5)
        
        self.assertEqual(ans1, {'gold_ingots': 5})
        self.assertEqual(ans2, {'gold_ingots': 5})
        self.assertEqual(ans3, {'gold_ingots': 5})
    
    def test_split_booty_2(self):
        purse1 = {"gold_ingots" : 1}
        purse2 = {"gold_ingots" : 1}
        
        self.assertEqual(split_booty(purse1, purse2),\
            "You need more gold ingots")
        
if __name__ == '__main__':
    unittest.main()