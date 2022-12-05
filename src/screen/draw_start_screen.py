
import tools.draw_higlight as draw_hl
import tools.draw_normal as draw_no
import pygame
from tools.stats import Stats
Stat = Stats()
pygame.init()

def draw_startscreen(screen):
    draw_hl.draw_highlight(screen, Stat.screen_width /
                               2-100, Stat.screen_height/2-40, 190, 80)
    draw_no.draw_txt(Stat.startfont, "start", Stat.txt_color, screen,
                        Stat.screen_width/2-75, Stat.screen_height/2-50)