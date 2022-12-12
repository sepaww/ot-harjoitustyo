import pygame
from repositories.stats import Stats
Stat = Stats()


def draw_highlight(screen, width, height, x_size, y_size):
    mouse = pygame.mouse.get_pos()
    pygame.draw.rect(screen, Stat.midlight_default_color,
                     [width, height, x_size, y_size])
    if width-1 <= mouse[0] <= width+x_size+1 and height <= mouse[1] <= height+y_size+1:
        pygame.draw.rect(screen, Stat.lighter_default_color, [
                         width-1, height-1, x_size+2, y_size+2], 5, 3)
    else:
        pygame.draw.rect(screen, Stat.darker_default_color, [
                         width-1, height-1, x_size+2, y_size+2], 5, 3)


def draw_non_highlight(screen, width, height, x_size, y_size):
    pygame.draw.rect(screen, Stat.midlight_default_color,
                     [width, height, x_size, y_size])
    pygame.draw.rect(screen, Stat.darker_default_color, [
                     width-1, height-1, x_size+2, y_size+2], 5, 3)
