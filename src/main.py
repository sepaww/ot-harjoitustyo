import pygame
import sys
import finance.stockcreator as stcr

import day_change_op.daychange as daychange

import tools.draw_higlight as draw_hl
import tools.draw_normal as draw_no

import finance.items as items
import finance.effects as effects

import screen.draw_screen as draw_screen
import screen.draw_ending as draw_en


import inputs.inputs as inputs
import inputs.endimputs as endinputs

import finance.Finance as Finance
import ending_screen_op.endinginit as endinit
import ending_screen_op.database_op as data_op
pygame.init()
pygame.display.set_caption("porssipeli")

screen_width = 64*15
screen_height = 64*12
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()
clock.tick(10)

mouse = pygame.mouse.get_pos()

startfont = pygame.font.SysFont("comicsans", 60)
smallfont = pygame.font.SysFont("comicsans", 25)
infofont = pygame.font.SysFont("comicsans", 30)

default_color = "#172226"
lighter_default_color = "#2d424a"
darker_default_color = "#131b1f"
midlight_default_color = "#203036"


class Ownedstocks():
    def __init__(self):
        self.owned = [0]*10


class Switch():
    def __init__(self):
        self.take = False


class Timer():
    def __init__(self):
        self.start_time = pygame.time.get_ticks()
        self.day = 1

# drawshopspot

# drawownedspot

# inputspot
# drawinfospot


################################################
def run(listofthings):

    l = listofthings
    stocks = l[0]
    wholefinance = l[1]

    owned = l[2]
    shopswitch = l[3]
    itemlist = l[4]
    dayswitch = l[5]
    timer = l[6]
    screen.fill((default_color))
    loop = True
    # MAIN LOOP
    while loop:
        timedifference = pygame.time.get_ticks()-timer.start_time
        draw_screen.drawinfo(wholefinance, timedifference, timer, screen)

        if shopswitch.take:
            inputs.inputterm(shopswitch, itemlist, wholefinance, dayswitch)
            draw_screen.drawshop(itemlist, screen)
            if not shopswitch.take:
                draw_screen.blank(screen)

        else:
            inputs.inputters(owned, stocks, wholefinance,
                             shopswitch, dayswitch)
            draw_screen.drawstocks(stocks, screen)
            draw_screen.drawowned(owned, screen)
            if shopswitch.take:
                draw_screen.blank(screen)

        if 30-timedifference/1000 <= 0 or dayswitch.take:
            dayswitch.take = False
            draw_screen.wholeblank(screen)
            if wholefinance.exp > wholefinance.money:
                break
            summarylist = daychange.daychange(
                stocks, wholefinance, owned, timer)
            summary = summarylist[0]
            itemlist = summarylist[1]
            stocks = summarylist[2]
            summaryloop = True

            while summaryloop:
                summaryloop = daychange.summary_driver(
                    screen, summary, wholefinance, summaryloop)
                pygame.display.update()

            draw_screen.wholeblank(screen)
            timer.start_time = pygame.time.get_ticks()

        pygame.display.update()
    return timer.day
################################################


def initialize():

    stocks = stcr.create_stocks()
    money = Finance.Finance(300, 50, 50)
    owned = Ownedstocks()
    switch = Switch()
    dayswitch = Switch()
    time = Timer()
    itemlist = items.itemgiver()

    return run([stocks, money, owned, switch, itemlist, dayswitch, time])


def ending_screen(days):
    database = data_op.Databaseop()
    needname = endinit.need_new_name(days, database)
    cursorposition = 0
    breaker = False
    while True:
        if needname:
            draw_en.draw_name_need(database, screen)
            rettuple = endinputs.nameinputs(database, needname, cursorposition)
            needname, cursorposition = rettuple[0], rettuple[1]
        else:
            draw_en.draw_hs(database, screen)
            breaker = endinputs.nextinputs()
        if breaker:
            break
        pygame.display.update()


def starting_screen():
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if screen_width/2-100 <= mouse[0] <= screen_width/2+90 and screen_height/2-40 <= mouse[1] <= screen_height/2+40:
                    days = initialize()
                    ending_screen(days)
        screen.fill((default_color))
        mouse = pygame.mouse.get_pos()
        draw_hl.draw_highlight(screen, midlight_default_color, darker_default_color,
                               lighter_default_color, screen_width/2-100, screen_height/2-40, 190, 80)
        draw_no.draw_txt(startfont, "start", "white", screen,
                         screen_width/2-75, screen_height/2-50)
        pygame.display.update()


starting_screen()
