class Stats():
    """class for stats used in game's code.
    """

    def __init__(self):
        """initiator
        """
        import pygame
        pygame.init()
        config=open("config.txt", "r")
        configlist=[]
        for line in config.read().splitlines():
            if line[0]!="!":
                configlist.append(line)
        
        if len(configlist)!=13:
            raise ValueError("Problems in config")
        
        self.screen_width = int(configlist.pop(0))
        
        self.screen_height = int(configlist.pop(0))
        
        self.startfont = pygame.font.SysFont(configlist.pop(0), int(configlist.pop(0)))
        
        self.smallfont = pygame.font.SysFont(configlist.pop(0), int(configlist.pop(0)))
        self.infofont = pygame.font.SysFont(configlist.pop(0), int(configlist.pop(0)))

        self.default_color = configlist.pop(0)
        self.lighter_default_color = configlist.pop(0)
        self.darker_default_color = configlist.pop(0)
        self.midlight_default_color = configlist.pop(0)

        self.name = configlist.pop(0)
