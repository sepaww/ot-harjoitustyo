import sys
import ui.tools.draw_higlight as draw_hl
import ui.tools.draw_normal as draw_no
import pygame
from repositories.stats import Stats
Stat = Stats()
pygame.init()


def draw_summary(screen, summary, finance):
    pygame.draw.rect(screen, Stat.midlight_default_color, [
                     Stat.screen_width/2-250, Stat.screen_height/2-250, 500, 500])
    draw_hl.draw_highlight(screen, Stat.screen_width /
                           2-100, Stat.screen_height/2+30, 190, 100)
    draw_no.draw_txt(Stat.info_font, "Net  Worth:", Stat.txt_color, screen,
                     Stat.screen_width/2-200, Stat.screen_height/2-200)
    draw_no.draw_txt(Stat.start_font, "okey", Stat.txt_color, screen,
                     Stat.screen_width/2-70, Stat.screen_height/2+30)
    draw_no.draw_txt(Stat.info_font, str(summary), Stat.txt_color, screen,
                     Stat.screen_width/2, Stat.screen_height/2-200)
    draw_no.draw_txt(Stat.info_font, "Money:", Stat.txt_color, screen,
                     Stat.screen_width/2-200, Stat.screen_height/2-150)
    draw_no.draw_txt(Stat.info_font, str(finance.money), Stat.txt_color,
                     screen, Stat.screen_width/2, Stat.screen_height/2-150)
    draw_no.draw_txt(Stat.info_font, "New Expenses:", Stat.txt_color, screen,
                     Stat.screen_width/2-200, Stat.screen_height/2-100)
    draw_no.draw_txt(Stat.info_font, str(finance.exp), Stat.txt_color,
                     screen, Stat.screen_width/2+20, Stat.screen_height/2-100)


def draw_info(m, time_difference, timer, screen):
    pygame.draw.rect(screen, Stat.midlight_default_color, [20, 20, 300, 200])
    pygame.draw.rect(screen, Stat.darker_default_color,
                     [20, 20, 300, 200], 5, 3)
    moneysentence = Stat.info_font.render("Money: ", True, Stat.txt_color)
    if m.money >= m.exp:
        money = Stat.info_font.render(str(m.money), True, Stat.txt_color)
    else:
        money = Stat.info_font.render(str(m.money), True, "red")
    exp_sentence = Stat.info_font.render("expenses", True, Stat.txt_color)
    expense = Stat.info_font.render(str(m.exp), True, "red")
    inc_sentence = Stat.info_font.render("income", True, Stat.txt_color)
    income = Stat.info_font.render(str(m.inc), True, "green")
    screen.blit(moneysentence, (60, 40))
    screen.blit(money, (230, 40))
    screen.blit(exp_sentence, (60, 90))
    screen.blit(expense, (230, 90))
    screen.blit(inc_sentence, (60, 140))
    screen.blit(income, (230, 140))
    time_difference = 30-time_difference/1000

    draw_hl.draw_highlight(screen, Stat.screen_width/2-155, 160, 100, 50)
    draw_no.draw_txt(Stat.info_font, "END", Stat.txt_color,
                     screen, Stat.screen_width/2-140, 165)
    pygame.draw.rect(screen, Stat.midlight_default_color, [
                     Stat.screen_width/2-130, 100, 50, 40])
    draw_no.draw_txt(Stat.info_font, str(round(time_difference)),
                     Stat.txt_color, screen, Stat.screen_width/2-123, 100)
    draw_no.draw_txt(Stat.info_font, "D a y", Stat.txt_color,
                     screen, Stat.screen_width/2-140, 10)
    draw_no.draw_txt(Stat.info_font, str(timer.day), Stat.txt_color,
                     screen, Stat.screen_width/2-115, 50)


def blank(screen):
    pygame.draw.rect(screen, Stat.default_color, [
                     Stat.screen_width/2-50, 0, 800, 800])
    pygame.draw.rect(screen, Stat.default_color, [
                     Stat.screen_width/2-300, 600, 800, 800])


def whole_blank(screen):
    pygame.draw.rect(screen, Stat.default_color, [0, 0, 1600, 1600])


def draw_owned(o, screen):
    start_height = 10
    mouse = pygame.mouse.get_pos()
    for i in range(10):
        amount = Stat.small_font.render(str(o.owned[i]), True, Stat.txt_color)
        pygame.draw.rect(screen, Stat.midlight_default_color, [
                         Stat.screen_width/2-50, start_height+8, 45, 45])
        pygame.draw.rect(screen, Stat.darker_default_color, [
                         Stat.screen_width/2-50, start_height+8, 45, 45], 5, 3)
        if o.owned[i] >= 10:
            screen.blit(amount, (Stat.screen_width/2-40, start_height+15))
        else:
            screen.blit(amount, (Stat.screen_width/2-35, start_height+15))
        start_height += 65
    draw_hl.draw_highlight(screen, Stat.screen_width /
                           2+50, start_height+8, 400, 88)
    shop_txt = Stat.start_font.render("market", True, Stat.txt_color)
    screen.blit(shop_txt, (Stat.screen_width/2+140, start_height+10))


def draw_character_select(screen, chr_list):
    draw_no.draw_chr(
        screen, chr_list[0], Stat.screen_width/2-450, Stat.screen_height/2-350)
    draw_no.draw_chr(
        screen, chr_list[1], Stat.screen_width/2+50, Stat.screen_height/2-350)
    draw_no.draw_chr(
        screen, chr_list[2], Stat.screen_width/2-450, Stat.screen_height/2+50)
    draw_no.draw_chr(
        screen, chr_list[3], Stat.screen_width/2+50, Stat.screen_height/2+50)
    draw_no.draw_txt(Stat.info_font, str(
        "Select your character"), Stat.txt_color, screen, Stat.screen_width/2-150, Stat.screen_height/2-20)


def draw_shop(item_list, screen, finance):
    
    draw_hl.draw_highlight(screen, Stat.screen_width/2+50, 668, 400, 88)
    shop_txt = Stat.start_font.render("stocks", True, Stat.txt_color)
    screen.blit(shop_txt, (Stat.screen_width/2+140, 660+10))
    draw_hl.draw_highlight(screen, Stat.screen_width/2+10, 50, 450, 175)
    draw_hl.draw_highlight(screen, Stat.screen_width/2+10, 250, 450, 175)
    draw_hl.draw_highlight(screen, Stat.screen_width/2+10, 450, 450, 175)
    if item_list[0].sold == False:
        draw_no.draw_thing(item_list[0], screen, Stat.screen_width/2+10, 50)
    else:
        draw_no.draw_sold(Stat.start_font, screen, Stat.screen_width/2+10, 50)
    if item_list[1].sold == False:
        draw_no.draw_thing(item_list[1], screen, Stat.screen_width/2+10, 250)
    else:
        draw_no.draw_sold(Stat.start_font, screen, Stat.screen_width/2+10, 250)
    if item_list[2].sold == False:
        draw_no.draw_thing(item_list[2], screen, Stat.screen_width/2+10, 450)
    else:
        draw_no.draw_sold(Stat.start_font, screen, Stat.screen_width/2+10, 450)
    # Reroll
    draw_hl.draw_highlight(screen, Stat.screen_width /
                           2-150, Stat.screen_height/2+250, 150, 100)
    draw_no.draw_txt(Stat.small_font, str(
        "Reroll"), Stat.txt_color, screen, Stat.screen_width/2-110, Stat.screen_height/2+260)
    draw_no.draw_txt(Stat.small_font, str(
        finance.reroll_price), Stat.txt_color, screen, Stat.screen_width/2-110, Stat.screen_height/2+300)


def draw_stocks(stocks, screen):
    
    day_stocks = stocks[len(stocks)-1]
    start_height = 10
    for stock in day_stocks:
        draw_hl.draw_highlight(screen, Stat.screen_width /
                               2+10, start_height+8, 450, 45)
        draw_hl.draw_highlight(screen, Stat.screen_width /
                               2+250, start_height+15, 30, 30)
        if stock[3] > 0:
            rise_color = "green"
        else:
            rise_color = "red"
        draw_no.draw_txt(Stat.small_font, str(
            stock[0]), Stat.txt_color, screen, Stat.screen_width/2+30, start_height+13)
        draw_no.draw_txt(Stat.small_font, str(
            stock[1]), Stat.txt_color, screen, Stat.screen_width/2+300, start_height+13)
        draw_no.draw_txt(Stat.small_font, str(
            stock[3]), rise_color, screen, Stat.screen_width/2+400, start_height+13)
        draw_no.draw_txt(Stat.small_font, str(
            "H"), Stat.txt_color, screen, Stat.screen_width/2+255, start_height+12)
        start_height += 65


def blank_history_view(screen):
    pygame.draw.rect(screen, Stat.default_color, [
        20, 400, 420, 700])


def draw_history_view(price_list, screen):
    blank_history_view(screen)
    draw_hl.draw_non_highlight(screen, 20, 250, 400, 300)
    prices = price_list[0]
    for i in range(9):
        pygame.draw.circle(screen, Stat.txt_color,
                           (i*40+40, 530-int(260*prices[i])), 4)
        pygame.draw.line(screen, Stat.txt_color, (i*40+45, 530 -
                         int(260*prices[i])), ((i+1)*40+45, 530-int(260*prices[i+1])), 2)
    pygame.draw.circle(screen, Stat.txt_color,
                       (9*40+40, 530-int(260*prices[9])), 4)
    draw_no.draw_txt(Stat.small_font, str(
        price_list[1]), Stat.txt_color, screen, 30, 260)
    draw_no.draw_txt(Stat.small_font, str(
        price_list[2]), Stat.txt_color, screen, 30, 510)
