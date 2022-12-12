
import os
import pygame


class Stats():
    """class for stats used in game's code.
        reads the information from config.txt
        has raise and try-except commands to make sure no wrong values slip in to the game
    """

    def __init__(self):
        """initiator
        """
        pygame.init()
        fake_screen = pygame.display.set_mode((960, 768))
        dir_name = os.path.dirname(__file__)
        config_spot = os.path.join(dir_name, "..", "config.txt")
        config = open(config_spot, "r")

        config_list = []
        for line in config.read().splitlines():
            if line[0] != "!":
                config_list.append(line)

        if len(config_list) != 14:
            raise ValueError("Wrong amount of values in config")

        temp = config_list.pop(0)
        if int(temp)/960 != 1:
            raise ValueError("Set screen_width back to base value")
        self.screen_width = int(temp)

        temp = config_list.pop(0)
        if int(temp) != 768:
            raise ValueError("Set screen_height back to base value")
        self.screen_height = int(temp)

        temp_1 = config_list.pop(0)
        temp_2 = config_list.pop(0)
        try:
            pygame.font.SysFont(temp_1, int(temp_2))
        except:
            raise ValueError("start_font values faulty")
        self.start_font = pygame.font.SysFont(temp_1, int(temp_2))

        temp_1 = config_list.pop(0)
        temp_2 = config_list.pop(0)
        try:
            pygame.font.SysFont(temp_1, int(temp_2))
        except:
            raise ValueError("smallfont values faulty")
        self.small_font = pygame.font.SysFont(temp_1, int(temp_2))

        temp_1 = config_list.pop(0)
        temp_2 = config_list.pop(0)
        try:
            pygame.font.SysFont(temp_1, int(temp_2))
        except:
            raise ValueError("info_font values faulty")
        self.info_font = pygame.font.SysFont(temp_1, int(temp_2))

        temp = config_list.pop(0)
        try:
            pygame.draw.rect(fake_screen, temp, [1, 1, 1, 1])
        except:
            raise ValueError("default_color not a color")
        self.default_color = temp

        temp = config_list.pop(0)
        try:
            pygame.draw.rect(fake_screen, temp, [1, 1, 1, 1])
        except:
            raise ValueError("lighter_default_color not a color")
        self.lighter_default_color = temp

        temp = config_list.pop(0)
        try:
            pygame.draw.rect(fake_screen, temp, [1, 1, 1, 1])
        except:
            raise ValueError("darker_default_color not a color")
        self.darker_default_color = temp

        temp = config_list.pop(0)
        try:
            pygame.draw.rect(fake_screen, temp, [1, 1, 1, 1])
        except:
            raise ValueError("midlight_default_color not a color")
        self.midlight_default_color = temp

        temp = config_list.pop(0)
        try:
            pygame.draw.rect(fake_screen, temp, [1, 1, 1, 1])
        except:
            raise ValueError("txt_color not a color")
        self.txt_color = temp

        temp = config_list.pop(0)
        if type(temp) != str:
            raise ValueError("games name is not a str")
        self.name = temp
        # pygame.quit()


class Owned_stocks():
    """a list with the purpose of tracking the indexes of
    owned stocks in the stocklist and their amount
    """

    def __init__(self):
        self.owned = [0]*10


class Switch():
    """Gereral purpose global boolian
    """

    def __init__(self):
        self.take = False


class Timer():
    """Timer object for time limit tracking and day highscore tracking
    """

    def __init__(self):
        self.start_time = pygame.time.get_ticks()
        self.day = 1
