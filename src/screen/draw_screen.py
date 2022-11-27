import sys
import tools.draw_higlight as draw_hl
import tools.draw_normal as draw_no
import pygame
from tools.stats import Stats
Stat = Stats()
pygame.init()


def draw_summary(screen, summary, finance):
    pygame.draw.rect(screen, Stat.midlight_default_color, [
                     Stat.screen_width/2-250, Stat.screen_height/2-250, 500, 500])
    draw_hl.draw_highlight(screen, Stat.screen_width /
                           2-100, Stat.screen_height/2+30, 190, 100)
    draw_no.draw_txt(Stat.infofont, "Net  Worth:", "white", screen,
                     Stat.screen_width/2-200, Stat.screen_height/2-200)
    draw_no.draw_txt(Stat.startfont, "okey", "white", screen,
                     Stat.screen_width/2-70, Stat.screen_height/2+30)
    draw_no.draw_txt(Stat.infofont, str(summary), "white", screen,
                     Stat.screen_width/2, Stat.screen_height/2-200)
    draw_no.draw_txt(Stat.infofont, "Money:", "white", screen,
                     Stat.screen_width/2-200, Stat.screen_height/2-150)
    draw_no.draw_txt(Stat.infofont, str(finance.money), "white",
                     screen, Stat.screen_width/2, Stat.screen_height/2-150)
    draw_no.draw_txt(Stat.infofont, "New Expenses:", "white", screen,
                     Stat.screen_width/2-200, Stat.screen_height/2-100)
    draw_no.draw_txt(Stat.infofont, str(finance.exp), "white",
                     screen, Stat.screen_width/2+20, Stat.screen_height/2-100)


def drawinfo(m, timedifference, timer, screen):
    pygame.draw.rect(screen, Stat.midlight_default_color, [20, 20, 300, 200])
    pygame.draw.rect(screen, Stat.darker_default_color,
                     [20, 20, 300, 200], 5, 3)
    moneysentence = Stat.infofont.render("Money: ", True, "white")
    if m.money >= m.exp:
        money = Stat.infofont.render(str(m.money), True, "white")
    else:
        money = Stat.infofont.render(str(m.money), True, "red")
    expsentence = Stat.infofont.render("expenses", True, "white")
    expense = Stat.infofont.render(str(m.exp), True, "red")
    incsentence = Stat.infofont.render("income", True, "white")
    income = Stat.infofont.render(str(m.inc), True, "green")
    screen.blit(moneysentence, (60, 40))
    screen.blit(money, (230, 40))
    screen.blit(expsentence, (60, 90))
    screen.blit(expense, (230, 90))
    screen.blit(incsentence, (60, 140))
    screen.blit(income, (230, 140))
    timedifference = 30-timedifference/1000
    draw_hl.draw_highlight(screen, Stat.screen_width/2-155, 160, 100, 50)
    draw_no.draw_txt(Stat.infofont, "END", "white",
                     screen, Stat.screen_width/2-140, 165)
    pygame.draw.rect(screen, Stat.midlight_default_color, [
                     Stat.screen_width/2-130, 100, 50, 40])
    draw_no.draw_txt(Stat.infofont, str(round(timedifference)),
                     "white", screen, Stat.screen_width/2-123, 100)
    draw_no.draw_txt(Stat.infofont, "D a y", "white",
                     screen, Stat.screen_width/2-140, 10)
    draw_no.draw_txt(Stat.infofont, str(timer.day), "white",
                     screen, Stat.screen_width/2-115, 50)


def blank(screen):
    pygame.draw.rect(screen, Stat.default_color, [
                     Stat.screen_width/2-50, 0, 800, 800])


def wholeblank(screen):
    pygame.draw.rect(screen, Stat.default_color, [0, 0, 1600, 1600])


def drawowned(o, screen):
    startheight = 10
    mouse = pygame.mouse.get_pos()
    for i in range(10):
        amount = Stat.smallfont.render(str(o.owned[i]), True, "white")
        pygame.draw.rect(screen, Stat.midlight_default_color, [
                         Stat.screen_width/2-50, startheight+8, 45, 45])
        pygame.draw.rect(screen, Stat.darker_default_color, [
                         Stat.screen_width/2-50, startheight+8, 45, 45], 5, 3)
        if o.owned[i] >= 10:
            screen.blit(amount, (Stat.screen_width/2-40, startheight+15))
        else:
            screen.blit(amount, (Stat.screen_width/2-35, startheight+15))
        startheight += 65
    draw_hl.draw_highlight(screen, Stat.screen_width /
                           2+50, startheight+8, 400, 88)
    shoptxt = Stat.startfont.render("market", True, "white")
    screen.blit(shoptxt, (Stat.screen_width/2+140, startheight+10))


def drawshop(itemlist, screen):
    mouse = pygame.mouse.get_pos()
    draw_hl.draw_highlight(screen, Stat.screen_width/2+50, 668, 400, 88)
    shoptxt = Stat.startfont.render("stocks", True, "white")
    screen.blit(shoptxt, (Stat.screen_width/2+140, 660+10))
    draw_hl.draw_highlight(screen, Stat.screen_width/2+10, 50, 450, 175)
    draw_hl.draw_highlight(screen, Stat.screen_width/2+10, 250, 450, 175)
    draw_hl.draw_highlight(screen, Stat.screen_width/2+10, 450, 450, 175)
    if itemlist[0].sold == False:
        draw_no.draw_thing(itemlist[0], screen, Stat.screen_width/2+10, 50)
    else:
        draw_no.draw_sold(Stat.startfont, screen, Stat.screen_width/2+10, 50)
    if itemlist[1].sold == False:
        draw_no.draw_thing(itemlist[1], screen, Stat.screen_width/2+10, 250)
    else:
        draw_no.draw_sold(Stat.startfont, screen, Stat.screen_width/2+10, 250)
    if itemlist[2].sold == False:
        draw_no.draw_thing(itemlist[2], screen, Stat.screen_width/2+10, 450)
    else:
        draw_no.draw_sold(Stat.startfont, screen, Stat.screen_width/2+10, 450)


def drawstocks(stocks, screen):
    mouse = pygame.mouse.get_pos()
    day_stocks = stocks[len(stocks)-1]
    startheight = 10
    for stock in day_stocks:
        draw_hl.draw_highlight(screen, Stat.screen_width /
                               2+10, startheight+8, 450, 45)
        if stock[3] > 0:
            risecolor = "green"
        else:
            risecolor = "red"
        draw_no.draw_txt(Stat.smallfont, str(
            stock[0]), "white", screen, Stat.screen_width/2+30, startheight+13)
        draw_no.draw_txt(Stat.smallfont, str(
            stock[1]), "white", screen, Stat.screen_width/2+300, startheight+13)
        draw_no.draw_txt(Stat.smallfont, str(
            stock[3]), risecolor, screen, Stat.screen_width/2+400, startheight+13)
        startheight += 65
