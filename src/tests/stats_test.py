from repositories import stats
import unittest
import pygame
pygame.init()


class Test_Stats(unittest.TestCase):
    def setUp(self):
        self.Stat = stats.Stats()
        self.Owned_stocks = stats.Owned_stocks()
        self.Switch = stats.Switch()
        self.Timer = stats.Timer()
        self.ticks = pygame.time.get_ticks()

    def test_stat_values(self):
        self.assertEqual(type(self.Stat.name), str)
        # vaikea näitä testata muulla kuin ovat olemassa ja toisaalta niiden validius on jo todettu stats.py:ssä
        # -----------------------------------------
        self.assertNotEqual(self.Stat.darker_default_color, None)
        self.assertNotEqual(self.Stat.midlight_default_color, None)
        self.assertNotEqual(self.Stat.lighter_default_color, None)
        self.assertNotEqual(self.Stat.default_color, None)
        self.assertNotEqual(self.Stat.txt_color, None)
        self.assertNotEqual(self.Stat.info_font, None)
        self.assertNotEqual(self.Stat.small_font, None)
        self.assertNotEqual(self.Stat.start_font, None)
        # -----------------------------------------
        self.assertEqual(self.Stat.screen_height, 768)
        self.assertEqual(self.Stat.screen_width, 960)
        pygame.quit()

    def test_Owned_stocks(self):
        self.assertEqual(len(self.Owned_stocks.owned), 10)
        for alk in self.Owned_stocks.owned:
            self.assertEqual(alk, 0)

    def test_Timer(self):
        self.assertAlmostEqual(self.Timer.start_time, self.ticks)
        self.assertEqual(self.Timer.day, 1)

    def test_Switch(self):
        self.assertEqual(self.Switch.take, False)
