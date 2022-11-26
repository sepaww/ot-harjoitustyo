import tools.draw_higlight as dr_hl
import tools.draw_normal as dr_no
import screen.draw_screen as dr_sc
import pygame
pygame.init()
screen_width = 64*15
screen_height = 64*12
startfont = pygame.font.SysFont("comicsans", 60)
smallfont = pygame.font.SysFont("comicsans", 25)
infofont = pygame.font.SysFont("comicsans", 30)
default_color = "#172226"
lighter_default_color = "#2d424a"
darker_default_color = "#131b1f"
midlight_default_color = "#203036"


def draw_highscorelist(database, screen):
    height = 50
    for i in range(len(database.scorelist)):
        dr_hl.draw_nonhighlight(screen, midlight_default_color, darker_default_color,
                                lighter_default_color, screen_width/2+100, height, 300, 50)
        dr_no.draw_txt(
            infofont, database.scorelist[i][0], "white", screen, screen_width/2+150, height+5)
        dr_no.draw_txt(infofont, str(
            database.scorelist[i][1]), "white", screen, screen_width/2+250, height+5)
        height += 60


def draw_name_need(database, screen):
    dr_sc.wholeblank(screen)
    draw_highscorelist(database, screen)
    pygame.draw.rect(screen, default_color, [
                     screen_width/2-450, 400, 300, 200])
    dr_no.draw_txt(startfont, "Congrats", "white",
                   screen, screen_width/2-450, 100)
    dr_no.draw_txt(
        startfont, f"You survived {database.scorelist[database.ind][1]} days", "white", screen, screen_width/2-450, 200)
    dr_no.draw_txt(infofont, "Enter your name:", "white",
                   screen, screen_width/2-450, 300)
    dr_no.draw_txt(startfont, str(
        database.scorelist[database.ind][0]), "white", screen, screen_width/2-450, 400)
    dr_no.draw_txt(infofont, "press enter to submit name",
                   "white", screen, screen_width/2-450, 500)


def draw_hs(database, screen):
    dr_sc.wholeblank(screen)
    draw_highscorelist(database, screen)
    dr_hl.draw_highlight(screen, midlight_default_color, darker_default_color,
                         lighter_default_color, screen_width/2-400, screen_height/2-300, 300, 200)
    dr_hl.draw_highlight(screen, midlight_default_color, darker_default_color,
                         lighter_default_color, screen_width/2-400, screen_height/2, 300, 200)
    dr_no.draw_txt(startfont, "play again", "white", screen,
                   screen_width/2-380, screen_height/2-250)
    dr_no.draw_txt(startfont, "quit", "white", screen,
                   screen_width/2-300, screen_height/2+50)
