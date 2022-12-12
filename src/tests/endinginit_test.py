import unittest
import services.ending_screen_op.ending_init as endinit


class fake_data_base():
    def __init__(self):
        self.scorelist = [["ses", 10], ["ses", 9], ["ses", 9], ["ses", 8], [
            "ses", 8], ["ses", 8], ["ses", 7], ["ses", 6], ["ses", 5], ["ses", 4]]


class Test_Finance(unittest.TestCase):
    def setUp(self):
        self.days = 3
        self.fake_data_base = fake_data_base()

    def test_too_low(self):
        ret = endinit.need_new_name(self.days, self.fake_data_base)
        self.assertEqual(ret, False)

    def test_place_nine(self):
        self.days = 5
        ret = endinit.need_new_name(self.days, self.fake_data_base)
        self.assertEqual(self.fake_data_base.scorelist[9][0], "____")
        self.assertEqual(ret, True)
