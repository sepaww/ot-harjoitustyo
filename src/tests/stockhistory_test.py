import unittest
import finance.stockhistory as st_hs
import finance.stockcreator as st_cr
import random as r


class Test_Stock_history(unittest.TestCase):
    def setUp(self):
        r.seed(1)
        self.startstocks = st_cr.create_stocks()
        self.startstock = ["test", 100, 50.1, 0]

    def test_stock_operator(self):
        r.seed(1)
        temp = st_hs.stock_operator(self.startstock)
        self.assertEqual(len(temp), 4)
        self.assertEqual(temp[0], self.startstock[0])
        self.assertEqual(type(temp[1]), int)
        self.assertEqual(type(temp[2]), int)
        self.assertEqual(type(temp[3]), int)
        if temp[1] > self.startstock[1]:
            self.assertGreater(temp[3], 0)
        else:
            self.assertGreater(0, temp[3])

    def test_create_history(self):
        # create_history is operated through stock creator

        self.assertEqual(len(self.startstocks), 10)

    def test_stock_update(self):
        temp = st_hs.stock_update(self.startstocks)
        self.assertEqual(len(temp), len(self.startstocks))
