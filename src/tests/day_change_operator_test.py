import unittest

import services.finance.finance as F
import services.finance.stock_creator as st_cr
import services.day_change_op.day_change_operator as op
import repositories.stats as s




class Test_DOP(unittest.TestCase):

    def setUp(self):
        self.time = s.Timer()
        self.time.day = 4
        self.owned = s.Ownedstocks()
        self.finance = F.Finance(("Jami", "your average 'Jantteri'",
                                 "average", 300, 50, 50, 25, [20, 20, 30, 30, 40, 40], 50))
        self.stocks = st_cr.create_stocks()

    def test_finance_update(self):
        op.finance_update(self.finance, self.time)
        self.assertEqual(self.finance.money, 300)
        self.assertEqual(self.finance.exp, 90)

    def test_finance_update_highday(self):
        self.time.day = 10
        op.finance_update(self.finance, self.time)
        self.assertEqual(self.finance.exp, 120)

    def test_summary_zero(self):
        summ = op.summary(self.stocks, self.finance, self.owned)
        self.assertEqual(summ, 300)

    def test_summary_some_owned(self):
        self.owned.owned[1] += 1
        summ = op.summary(self.stocks, self.finance, self.owned)
        curstock = self.stocks[-1]

        sum_of_money = 0
        for i in range(len(curstock)):
            if self.owned.owned[i] > 0:
                sum_of_money += curstock[i][1]*self.owned.owned[i]
        sum_of_money += self.finance.money
        self.assertEqual(summ, sum_of_money)
