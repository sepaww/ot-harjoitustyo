import pygame
from tools.stats import Stats
from tools.draw_higlight import draw_highlight
Stat = Stats()


def draw_txt(font, text, color, screen, posx, posy):
    txt = font.render(text, True, color)
    screen.blit(txt, (posx, posy))


def draw_thing(item, screen, posx, posy):

    headtxt = Stat.infofont.render(item.name, True, Stat.txt_color)
    effecttxt = Stat.smallfont.render(item.effectstr, True, Stat.txt_color)
    description = Stat.smallfont.render(item.description, True, Stat.txt_color)
    pricesentence = Stat.infofont.render("Price:", True, Stat.txt_color)
    price = Stat.infofont.render(str(item.price), True, Stat.txt_color)
    screen.blit(headtxt, (posx+10, posy+10))
    screen.blit(description, (posx+10, posy+90))
    screen.blit(effecttxt, (posx+10, posy+130))
    screen.blit(pricesentence, (posx+10, posy+50))
    screen.blit(price, (posx+200, posy+50))


def draw_sold(font, screen, posx, posy):
    soldtxt = font.render("sold", True, Stat.txt_color)
    screen.blit(soldtxt, (posx+10, posy+90))


def draw_chr(screen, chrinfo, width, height):
    draw_highlight(screen, width,
                   height, 400, 300)
    draw_txt(Stat.infofont, str(
        chrinfo[0]), Stat.txt_color, screen, width+40, height+10)
    draw_txt(Stat.smallfont, str(
        chrinfo[1]), Stat.txt_color, screen, width+10, height+60)
    draw_txt(Stat.infofont, str(
        f"Money: {chrinfo[3]}"), Stat.txt_color, screen, width+160, height+10)
    draw_txt(Stat.infofont, str(
        f"income: {chrinfo[4]}"), Stat.txt_color, screen, width+10, height+120)
    draw_txt(Stat.infofont, str(
        f"expenses: {chrinfo[5]}"), Stat.txt_color, screen, width+190, height+120)
    draw_txt(Stat.infofont, str(
        f"reroll price: {chrinfo[6]}"), Stat.txt_color, screen, width+10, height+170)
    draw_txt(Stat.infofont, str(
        f"expense scaling: {chrinfo[2]}"), Stat.txt_color, screen, width+10, height+220)
