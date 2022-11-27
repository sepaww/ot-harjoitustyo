import pygame
from tools.stats import Stats
Stat=Stats()

def draw_highlight(screen, width, height, xsize, ysize):
    mouse = pygame.mouse.get_pos()
    pygame.draw.rect(screen, Stat.midlight_default_color, [width, height, xsize, ysize])
    if width-1 <= mouse[0] <= width+xsize+1 and height <= mouse[1] <= height+ysize+1:
        pygame.draw.rect(screen, Stat.lighter_default_color, [
                         width-1, height-1, xsize+2, ysize+2], 5, 3)
    else:
        pygame.draw.rect(screen, Stat.darker_default_color, [
                         width-1, height-1, xsize+2, ysize+2], 5, 3)


def draw_nonhighlight(screen, width, height, xsize, ysize):
    pygame.draw.rect(screen, Stat.midlight_default_color, [width, height, xsize, ysize])
    pygame.draw.rect(screen, Stat.darker_default_color, [
                     width-1, height-1, xsize+2, ysize+2], 5, 3)
