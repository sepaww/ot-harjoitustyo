import unittest
import finance.stockcreator as st_cr


class Test_Stock_creator(unittest.TestCase):
    def setUp(self):
        self.startstocks = st_cr.create_stocks()

    def test_exists(self):
        temp = st_cr.create_stocks()
        self.assertNotEqual(temp, None)

    def test_stock_parts(self):
        temp = self.startstocks[0][0]
        self.assertEqual(len(temp), 4)
        self.assertEqual(type(temp[0]), str)
        self.assertEqual(type(temp[1]), int)
        self.assertEqual(type(temp[2]), float)
        self.assertEqual(temp[3], 0)

    def test_startstock_len(self):
        self.assertEqual(len(self.startstocks), 10)
        self.assertEqual(len(self.startstocks[0]), 10)
        
    def test_stockviewer(self):
        pricelist=[]
        diff_list=[]
        
        index=1
        for dayslist in self.startstocks:
            pricelist.append(dayslist[index][1])
        maxprice=max(pricelist)
        minprice=min(pricelist)
        bigdiff=maxprice-minprice
        for arvo in pricelist:
            arvodiff=arvo-minprice
            arvodiff=arvodiff/bigdiff
            diff_list.append(arvodiff)
        ret=st_cr.create_historyview(self.startstocks, index)
        self.assertEqual(ret[1], maxprice)
        self.assertEqual(ret[2], minprice)
        for i in range(10):
            self.assertEqual(diff_list[i], ret[0][i])