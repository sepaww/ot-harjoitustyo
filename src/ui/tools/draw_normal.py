import pygame
from repositories.stats import Stats
from ui.tools.draw_higlight import draw_highlight
Stat = Stats()


def draw_txt(font, text, color, screen, pos_x, pos_y):
    txt = font.render(text, True, color)
    screen.blit(txt, (pos_x, pos_y))


def draw_thing(item, screen, pos_x, pos_y):

    head_txt = Stat.info_font.render(item.name, True, Stat.txt_color)
    effect_txt = Stat.small_font.render(item.effect_str, True, Stat.txt_color)
    description = Stat.small_font.render(
        item.description, True, Stat.txt_color)
    price_sentence = Stat.info_font.render("Price:", True, Stat.txt_color)
    price = Stat.info_font.render(str(item.price), True, Stat.txt_color)
    screen.blit(head_txt, (pos_x+10, pos_y+10))
    screen.blit(description, (pos_x+10, pos_y+90))
    screen.blit(effect_txt, (pos_x+10, pos_y+130))
    screen.blit(price_sentence, (pos_x+10, pos_y+50))
    screen.blit(price, (pos_x+200, pos_y+50))


def draw_sold(font, screen, pos_x, pos_y):
    sold_txt = font.render("sold", True, Stat.txt_color)
    screen.blit(sold_txt, (pos_x+10, pos_y
                           + 90))


def draw_chr(screen, chr_info, width, height):
    draw_highlight(screen, width,
                   height, 400, 300)
    draw_txt(Stat.info_font, str(
        chr_info[0]), Stat.txt_color, screen, width+40, height+10)
    draw_txt(Stat.small_font, str(
        chr_info[1]), Stat.txt_color, screen, width+10, height+60)
    draw_txt(Stat.info_font, str(
        f"Money: {chr_info[3]}"), Stat.txt_color, screen, width+160, height+10)
    draw_txt(Stat.info_font, str(
        f"income: {chr_info[4]}"), Stat.txt_color, screen, width+10, height+120)
    draw_txt(Stat.info_font, str(
        f"expenses: {chr_info[5]}"), Stat.txt_color, screen, width+190, height+120)
    draw_txt(Stat.info_font, str(
        f"reroll price: {chr_info[6]}"), Stat.txt_color, screen, width+10, height+170)
    draw_txt(Stat.info_font, str(
        f"expense scaling: {chr_info[2]}"), Stat.txt_color, screen, width+10, height+220)
