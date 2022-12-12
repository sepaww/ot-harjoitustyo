from repositories.stats import Stats
import ui.tools.draw_higlight as dr_hl
import ui.tools.draw_normal as dr_no
import ui.screen.draw_screen as dr_sc
import pygame
pygame.init()
Stat = Stats()


def draw_highscore_list(data_base, screen):
    height = 50
    for i in range(len(data_base.score_list)):
        dr_hl.draw_non_highlight(
            screen, Stat.screen_width/2+100, height, 300, 50)
        dr_no.draw_txt(
            Stat.info_font, data_base.score_list[i][0], Stat.txt_color, screen, Stat.screen_width/2+150, height+5)
        dr_no.draw_txt(Stat.info_font, str(
            data_base.score_list[i][1]), Stat.txt_color, screen, Stat.screen_width/2+250, height+5)
        height += 60


def draw_name_need(data_base, screen):
    dr_sc.whole_blank(screen)
    draw_highscore_list(data_base, screen)
    pygame.draw.rect(screen, Stat.default_color, [
                     Stat.screen_width/2-450, 400, 300, 200])
    dr_no.draw_txt(Stat.start_font, "Congrats", Stat.txt_color,
                   screen, Stat.screen_width/2-450, 100)
    dr_no.draw_txt(
        Stat.start_font, f"You survived {data_base.score_list[data_base.ind][1]} days", Stat.txt_color, screen, Stat.screen_width/2-450, 200)
    dr_no.draw_txt(Stat.info_font, "Enter your name:", Stat.txt_color,
                   screen, Stat.screen_width/2-450, 300)
    dr_no.draw_txt(Stat.start_font, str(
        data_base.score_list[data_base.ind][0]), Stat.txt_color, screen, Stat.screen_width/2-450, 400)
    dr_no.draw_txt(Stat.info_font, "press enter to submit name",
                   Stat.txt_color, screen, Stat.screen_width/2-450, 500)


def draw_hs(data_base, screen):
    dr_sc.whole_blank(screen)
    draw_highscore_list(data_base, screen)
    dr_hl.draw_highlight(screen, Stat.screen_width/2-400,
                         Stat.screen_height/2-300, 300, 200)
    dr_hl.draw_highlight(screen, Stat.screen_width/2-400,
                         Stat.screen_height/2, 300, 200)
    dr_no.draw_txt(Stat.start_font, "play again", Stat.txt_color, screen,
                   Stat.screen_width/2-380, Stat.screen_height/2-250)
    dr_no.draw_txt(Stat.start_font, "quit", Stat.txt_color, screen,
                   Stat.screen_width/2-300, Stat.screen_height/2+50)
