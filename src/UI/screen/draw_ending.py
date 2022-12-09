from Repositories.stats import Stats
import UI.tools.draw_higlight as dr_hl
import UI.tools.draw_normal as dr_no
import UI.screen.draw_screen as dr_sc
import pygame
pygame.init()
Stat = Stats()


def draw_highscorelist(database, screen):
    height = 50
    for i in range(len(database.scorelist)):
        dr_hl.draw_nonhighlight(
            screen, Stat.screen_width/2+100, height, 300, 50)
        dr_no.draw_txt(
            Stat.infofont, database.scorelist[i][0], Stat.txt_color, screen, Stat.screen_width/2+150, height+5)
        dr_no.draw_txt(Stat.infofont, str(
            database.scorelist[i][1]), Stat.txt_color, screen, Stat.screen_width/2+250, height+5)
        height += 60


def draw_name_need(database, screen):
    dr_sc.wholeblank(screen)
    draw_highscorelist(database, screen)
    pygame.draw.rect(screen, Stat.default_color, [
                     Stat.screen_width/2-450, 400, 300, 200])
    dr_no.draw_txt(Stat.startfont, "Congrats", Stat.txt_color,
                   screen, Stat.screen_width/2-450, 100)
    dr_no.draw_txt(
        Stat.startfont, f"You survived {database.scorelist[database.ind][1]} days", Stat.txt_color, screen, Stat.screen_width/2-450, 200)
    dr_no.draw_txt(Stat.infofont, "Enter your name:", Stat.txt_color,
                   screen, Stat.screen_width/2-450, 300)
    dr_no.draw_txt(Stat.startfont, str(
        database.scorelist[database.ind][0]), Stat.txt_color, screen, Stat.screen_width/2-450, 400)
    dr_no.draw_txt(Stat.infofont, "press enter to submit name",
                   Stat.txt_color, screen, Stat.screen_width/2-450, 500)


def draw_hs(database, screen):
    dr_sc.wholeblank(screen)
    draw_highscorelist(database, screen)
    dr_hl.draw_highlight(screen, Stat.screen_width/2-400,
                         Stat.screen_height/2-300, 300, 200)
    dr_hl.draw_highlight(screen, Stat.screen_width/2-400,
                         Stat.screen_height/2, 300, 200)
    dr_no.draw_txt(Stat.startfont, "play again", Stat.txt_color, screen,
                   Stat.screen_width/2-380, Stat.screen_height/2-250)
    dr_no.draw_txt(Stat.startfont, "quit", Stat.txt_color, screen,
                   Stat.screen_width/2-300, Stat.screen_height/2+50)
