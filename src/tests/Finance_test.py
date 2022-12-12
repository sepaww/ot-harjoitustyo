import unittest
import services.finance.effects as ef
import services.finance.finance as F


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
        self.assertEqual(finance.reroll_price, 25)
        self.assertEqual(finance.standard_exp_increase, 50)

    def test_reduction(self):
        self.finance.change_amount(10)
        self.assertEqual(self.finance.money, 290)

    def test_addition(self):
        self.finance.change_amount_up(10)
        self.assertEqual(self.finance.money, 310)

    def test_reroll_doubler(self):
        self.finance.reroll_doubler()
        self.assertEqual(self.finance.reroll_price, 50)
