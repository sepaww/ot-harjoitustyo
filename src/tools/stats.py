class Stats():
    """class for stats used in game's code.
    """

    def __init__(self):
        """initiator
        """
        import pygame
        pygame.init()
        self.screen_width = 64*15
        self.screen_height = 64*12

        self.startfont = pygame.font.SysFont("comicsans", 60)
        self.smallfont = pygame.font.SysFont("comicsans", 25)
        self.infofont = pygame.font.SysFont("comicsans", 30)

        self.default_color = "#172226"
        self.lighter_default_color = "#2d424a"
        self.darker_default_color = "#131b1f"
        self.midlight_default_color = "#203036"

        self.name = "pörssipeli"
