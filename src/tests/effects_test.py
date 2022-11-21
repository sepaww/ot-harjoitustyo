import unittest
import finance.effects as ef
import finance.Finance as F
class Test_Stock_history(unittest.TestCase):
    def setUp(self):
        self.Finance=F.Finance(100, 50, 50)
        self.effectlist=[("money", 10), ("income", 20), ("expenses", -30)]
        self.lotteryeff=[("lottery", 0)]
        
    def test_applying(self):
        temp=F.Finance(100, 50, 50)
        ef.apply_effect(self.effectlist, temp)
        self.assertNotEqual(self.Finance.money,temp.money ) 
        self.assertNotEqual(self.Finance.exp,temp.exp )
        self.assertNotEqual(self.Finance.inc,temp.inc )
        
    def test_correct_apply(self):
        ef.apply_effect(self.effectlist, self.Finance)
        self.assertEqual(self.Finance.money,110)    
        self.assertEqual(self.Finance.exp,20)    
        self.assertEqual(self.Finance.inc,70)       
    