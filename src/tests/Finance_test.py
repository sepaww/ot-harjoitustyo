import unittest
from finance.effects import apply_effect
from finance.Finance import Finance

class Test_Finance(unittest.TestCase):
    def setUp(self):
        None
    def test_Existance(self):
        finance=Finance(100, 50, 50)
        self.assertEqual(finance.money, 100)
        self.assertEqual(finance.inc, 50)
        self.assertEqual(finance.exp, 50)
