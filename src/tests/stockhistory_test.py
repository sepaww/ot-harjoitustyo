import unittest
import services.finance.stock_history as st_hs
import services.finance.stock_creator as st_cr
import random as r


class Test_Stock_history(unittest.TestCase):
    def setUp(self):
        r.seed(1)
        self.start_stocks = st_cr.create_stocks()
        self.start_stock = ["test", 100, 50.1, 0]

    def test_stock_operator(self):
        r.seed(1)
        temp = st_hs.stock_operator(self.start_stock)
        self.assertEqual(len(temp), 4)
        self.assertEqual(temp[0], self.start_stock[0])
        self.assertEqual(type(temp[1]), int)
        self.assertEqual(type(temp[2]), int)
        self.assertEqual(type(temp[3]), int)
        if temp[1] > self.start_stock[1]:
            self.assertGreater(temp[3], 0)
        else:
            self.assertGreater(0, temp[3])

    def test_create_history(self):
        # create_history is operated through stock creator

        self.assertEqual(len(self.start_stocks), 10)

    def test_stock_update(self):
        temp = st_hs.stock_update(self.start_stocks)
        self.assertEqual(len(temp), len(self.start_stocks))
