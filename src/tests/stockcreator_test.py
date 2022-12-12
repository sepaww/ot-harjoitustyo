import unittest
import services.finance.stock_creator as st_cr


class Test_Stock_creator(unittest.TestCase):
    def setUp(self):
        self.start_stocks = st_cr.create_stocks()

    def test_exists(self):
        temp = st_cr.create_stocks()
        self.assertNotEqual(temp, None)

    def test_stock_parts(self):
        temp = self.start_stocks[0][0]
        self.assertEqual(len(temp), 4)
        self.assertEqual(type(temp[0]), str)
        self.assertEqual(type(temp[1]), int)
        self.assertEqual(type(temp[2]), float)
        self.assertEqual(temp[3], 0)

    def test_start_stock_len(self):
        self.assertEqual(len(self.start_stocks), 10)
        self.assertEqual(len(self.start_stocks[0]), 10)

    def test_stock_viewer(self):
        price_list = []
        diff_list = []

        index = 1
        for days_list in self.start_stocks:
            price_list.append(days_list[index][1])
        max_price = max(price_list)
        min_price = min(price_list)
        big_diff = max_price-min_price
        for arvo in price_list:
            arvo_diff = arvo-min_price
            arvo_diff = arvo_diff/big_diff
            diff_list.append(arvo_diff)
        ret = st_cr.create_history_view(self.start_stocks, index)
        self.assertEqual(ret[1], max_price)
        self.assertEqual(ret[2], min_price)
        for i in range(10):
            self.assertEqual(diff_list[i], ret[0][i])
