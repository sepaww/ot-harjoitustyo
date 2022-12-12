import sys
import pygame
from repositories.stats import Stats
Stat = Stats()


def start_inputs():
    start_mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Stat.screen_width/2-100 <= start_mouse[0] <= Stat.screen_width/2+90:
                if Stat.screen_height/2-40 <= start_mouse[1] <= Stat.screen_height/2+40:
                    return True
    return False
