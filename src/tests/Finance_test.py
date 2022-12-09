import unittest
import Services.finance.effects as ef
import Services.finance.finance as F


class Test_Finance(unittest.TestCase):
    def setUp(self):
        self.finance = F.Finance(("Jami", "your average 'Jantteri'",
                                 "average", 300, 50, 50, 25, [20, 20, 30, 30, 40, 40], 50))

    def test_Existance(self):
        finance = F.Finance(("Jami", "your average 'Jantteri'",
                            "average", 300, 50, 50, 25, [20, 20, 30, 30, 40, 40], 50))
        self.assertEqual(finance.money, 300)
        self.assertEqual(finance.inc, 50)
        self.assertEqual(finance.explist, [20, 20, 30, 30, 40, 40])
        self.assertEqual(finance.rerollprice, 25)
        self.assertEqual(finance.standard_exp_increase, 50)

    def test_reduction(self):
        self.finance.change_amount(10)
        self.assertEqual(self.finance.money, 290)

    def test_addition(self):
        self.finance.change_amount_up(10)
        self.assertEqual(self.finance.money, 310)

    def test_reroll_doubler(self):
        self.finance.reroll_doubler()
        self.assertEqual(self.finance.rerollprice, 50)
