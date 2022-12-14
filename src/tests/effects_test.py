import unittest
import services.finance.effects as ef
import services.finance.finance as F
from random import seed


class Test_Stock_history(unittest.TestCase):
    def setUp(self):
        self.Finance = F.Finance(("Jami", "your average 'Jantteri'",
                                 "average", 300, 50, 50, 25, [20, 20, 30, 30, 40, 40], 50))
        self.effect_list = [("money", 10), ("income", 20), ("expenses", -30)]
        self.lottery_eff = [("lottery", 0)]

    def test_applying(self):
        temp = F.Finance(("Jami", "your average 'Jantteri'", "average",
                         300, 50, 50, 25, [20, 20, 30, 30, 40, 40], 50))
        ef.apply_effect(self.effect_list, temp)
        self.assertNotEqual(self.Finance.money, temp.money)
        self.assertNotEqual(self.Finance.exp, temp.exp)
        self.assertNotEqual(self.Finance.inc, temp.inc)

    def test_correct_apply(self):
        ef.apply_effect(self.effect_list, self.Finance)
        self.assertEqual(self.Finance.money, 310)
        self.assertEqual(self.Finance.exp, 20)
        self.assertEqual(self.Finance.inc, 70)

    def test_correct_apply(self):
        seed(1)
        ef.apply_effect(self.lottery_eff, self.Finance)
        self.assertEqual(self.Finance.money, 310)
        seed(100)
        ef.apply_effect(self.lottery_eff, self.Finance)
        self.assertEqual(self.Finance.money, 320)
        seed(30)
        ef.apply_effect(self.lottery_eff, self.Finance)
        self.assertEqual(self.Finance.money, 320)
