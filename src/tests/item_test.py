import unittest
import shop.items as it
class Test_Stock_history(unittest.TestCase):
    def setUp(self):
        self.imaginary_item=["Head", "Desc", "stat_Desc", [("money", 0)], 1]
    
    def test_item(self):
        item=it.Item(self.imaginary_item[0], self.imaginary_item[1], self.imaginary_item[2], self.imaginary_item[3] ,self.imaginary_item[4])
        self.assertEqual(item.name, self.imaginary_item[0])
        self.assertEqual(item.description, self.imaginary_item[1])
        self.assertEqual(item.effectstr, self.imaginary_item[2])
        self.assertEqual(item.effect, self.imaginary_item[3])
        self.assertEqual(item.price, self.imaginary_item[4])
        self.assertEqual(item.sold, False)