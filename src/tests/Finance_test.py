import unittest
import finance.effects as ef
import finance.Finance as F

class Test_Finance(unittest.TestCase):
    def setUp(self):
        None
    def test_Existance(self):
        finance=F.Finance(100, 50, 50)
        self.assertEqual(finance.money, 100)
        self.assertEqual(finance.inc, 50)
        self.assertEqual(finance.exp, 50)