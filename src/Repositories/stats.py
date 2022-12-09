
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
        fake_screen=pygame.display.set_mode((960,768))
        dirname = os.path.dirname(__file__)
        configspot = os.path.join(dirname, "..", "config.txt")
        config = open(configspot, "r")

        configlist = []
        for line in config.read().splitlines():
            if line[0] != "!":
                configlist.append(line)

        if len(configlist) != 14:
            raise ValueError("Wrong amount of values in config")
        
        temp=configlist.pop(0)
        if int(temp)/960 != 1:
            raise ValueError("Set screen_width back to base value")
        self.screen_width = int(temp)
        
        temp=configlist.pop(0)
        if int(temp)!=768:
            raise ValueError("Set screen_height back to base value")
        self.screen_height = int(temp)
        
        temp1=configlist.pop(0)
        temp2=configlist.pop(0)
        try:
            pygame.font.SysFont(temp1, int(temp2))
        except:
            raise ValueError("startfont values faulty")
        self.startfont = pygame.font.SysFont(temp1, int(temp2))

        temp1=configlist.pop(0)
        temp2=configlist.pop(0)
        try:
            pygame.font.SysFont(temp1, int(temp2))
        except:
            raise ValueError("smallfont values faulty")
        self.smallfont = pygame.font.SysFont(temp1, int(temp2))
        
        temp1=configlist.pop(0)
        temp2=configlist.pop(0)
        try:
            pygame.font.SysFont(temp1, int(temp2))
        except:
            raise ValueError("infofont values faulty")
        self.infofont = pygame.font.SysFont(temp1, int(temp2))
        
        temp=configlist.pop(0)
        try:
            pygame.draw.rect(fake_screen,temp,[1,1,1,1])
        except:
            raise ValueError("default_color not a color")
        self.default_color = temp
        
        temp=configlist.pop(0)
        try:
            pygame.draw.rect(fake_screen,temp,[1,1,1,1])
        except:
            raise ValueError("lighter_default_color not a color")
        self.lighter_default_color = temp
        
        temp=configlist.pop(0)
        try:
            pygame.draw.rect(fake_screen,temp,[1,1,1,1])
        except:
            raise ValueError("darker_default_color not a color")
        self.darker_default_color = temp
        
        temp=configlist.pop(0)
        try:
            pygame.draw.rect(fake_screen,temp,[1,1,1,1])
        except:
            raise ValueError("midlight_default_color not a color")
        self.midlight_default_color = temp
        
        temp=configlist.pop(0)
        try:
            pygame.draw.rect(fake_screen,temp,[1,1,1,1])
        except:
            raise ValueError("txt_color not a color")
        self.txt_color = temp
        
        temp=configlist.pop(0)
        if type(temp)!=str:
            raise ValueError("games name is not a str")
        self.name = temp
        #pygame.quit()
class Ownedstocks():
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
