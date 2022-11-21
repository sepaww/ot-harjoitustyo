import unittest
import stocks.stockcreator as st_cr

class Test_Stock_creator(unittest.TestCase):
    def setUp(self):
        self.startstocks=st_cr.create_stocks()

    def test_exists(self):
        temp=st_cr.create_stocks()
        self.assertNotEqual(temp, None)
    
    def test_stock_parts(self):
        temp=self.startstocks[0][0]
        self.assertEqual(len(temp), 4)
        self.assertEqual(type(temp[0]), str)
        self.assertEqual(type(temp[1]), int)
        self.assertEqual(type(temp[2]), float)
        self.assertEqual(type(temp[3]), 0)
        
    def test_startstock_len(self):
        self.assertEqual(len(self.startstocks), 100)
        self.assertEqual(len(self.startstocks[0]), 10)
        
        