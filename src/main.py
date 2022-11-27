import sys
import pygame

from finance import stockcreator as stcr
from finance import Finance
from finance import items


from day_change_op import daychange

from tools import draw_higlight as draw_hl
from tools import draw_normal as draw_no
from tools.stats import Stats

from screen import draw_screen
from screen import draw_ending as draw_en


from inputs import inputs
from inputs import endinputs


from ending_screen_op import endinginit as endinit
from ending_screen_op import database_op as data_op

pygame.init()
Stat = Stats()
pygame.display.set_caption(Stat.name)


screen = pygame.display.set_mode((Stat.screen_width, Stat.screen_height))

clock = pygame.time.Clock()
clock.tick(10)

mouse = pygame.mouse.get_pos()


class Ownedstocks():
    """a list with the purpose of tracking the indexes of
    owned stocks in the stocklist and their amount
    """

    def __init__(self):
        self.owned = [0]*10


class Switch():
    """Gereral purpose global boolian
    """

    def __init__(self):
        self.take = False


class Timer():
    """Timer object for time limit tracking and day highscore tracking
    """

    def __init__(self):
        self.start_time = pygame.time.get_ticks()
        self.day = 1


def run(listofthings):
    """Main loop. takes value from initialize and calls for
    gamelogic functions and pygame inputs and draw_screens.
    Also operates day change operator. after done
    looping will return back to starting_screen function

    Args:
        listofthings (list): includes all required objects from initialize to run the game

    Returns:
        days: the amount of days player survived
    """
    lot = listofthings
    stocks = lot[0]
    wholefinance = lot[1]

    owned = lot[2]
    shopswitch = lot[3]
    itemlist = lot[4]
    dayswitch = lot[5]
    timer = lot[6]
    screen.fill((Stat.default_color))
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
    """A function for calling all the setup function for the
    game to start and settting up all objects used to run the game

    Returns:
        days: the amount of days the player lasted.
    """
    stocks = stcr.create_stocks()
    money = Finance.Finance(300, 50, 50)
    owned = Ownedstocks()
    switch = Switch()
    dayswitch = Switch()
    time = Timer()
    itemlist = items.itemgiver()

    return run([stocks, money, owned, switch, itemlist, dayswitch, time])


def ending_screen(days):
    """The function that runs everything that happens
    after the player cant pay the daily expenses.
    Is responsible for calling database related functions
    and calling ending screen related pygame functions

    Args:
        days (int): the "highscore" of player
    """
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
    """The function that is reponsible of running the
    starting screen and calling for initialize()
    when player starts the game.
    Also responsible of calling
    for ending_screen after player cant pay for expenses
    """
    loop = True
    while loop:
        Startmouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Stat.screen_width/2-100 <= Startmouse[0] <= Stat.screen_width/2+90 and
                Stat.screen_height/2-40 <= Startmouse[1] <= Stat.screen_height/2+40:
                    days = initialize()
                    ending_screen(days)
        screen.fill((Stat.default_color))
        
        draw_hl.draw_highlight(screen, Stat.screen_width /
                               2-100, Stat.screen_height/2-40, 190, 80)
        draw_no.draw_txt(Stat.startfont, "start", "white", screen,
                         Stat.screen_width/2-75, Stat.screen_height/2-50)
        pygame.display.update()


starting_screen()
