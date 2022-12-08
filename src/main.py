import sys
import pygame

from finance import stockcreator as stcr
from finance import Finance
from finance import items
from finance.Finance import character_list

from day_change_op import daychange

from tools.stats import Stats

from screen import draw_screen
from screen import draw_ending as draw_en
from screen import draw_start_screen as dr_strt

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
    original_reroll = wholefinance.rerollprice
    
    # MAIN LOOP
    while loop:
        timedifference = pygame.time.get_ticks()-timer.start_time
        # Whether we are in shop or stock view
        if shopswitch.take:
            rerolled = inputs.inputter_market(
                shopswitch, itemlist, wholefinance, dayswitch)
            if rerolled:
                itemlist = items.itemgiver()
            draw_screen.drawshop(itemlist, screen, wholefinance)
            if not shopswitch.take:
                draw_screen.blank(screen)

        else:
            inputs.inputter_stock(owned, stocks, wholefinance,
                                  shopswitch, dayswitch, screen)
            draw_screen.drawstocks(stocks, screen)
            draw_screen.drawowned(owned, screen)
            if shopswitch.take:
                draw_screen.blank(screen)
        # Draws finance info
        draw_screen.drawinfo(wholefinance, timedifference, timer, screen)
        # Checking if player has clicked end or timer has run out.
        # If so, engages day_change_operations or ends game if not enough money
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
            wholefinance.rerollprice = original_reroll
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


def character_select():
    draw_screen.draw_character_select(screen, character_list)
    character = inputs.character_select_input(character_list)
    return character


def initialize():
    """A function for calling all the setup function for the
    game to start and settting up all objects used to run the game
    also lets the player choose their character

    Returns:
        days: the amount of days the player lasted.
    """
    draw_screen.wholeblank(screen)
    # Character select loop
    character = None
    while character is None:
        character = character_select()
        pygame.display.update()
    stocks = stcr.create_stocks()
    money = Finance.Finance(character)
    owned = stats.Ownedstocks()
    switch = stats.Switch()
    dayswitch = stats.Switch()
    time = stats.Timer()
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
        startmouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Stat.screen_width/2-100 <= startmouse[0] <= Stat.screen_width/2+90:
                    if Stat.screen_height/2-40 <= startmouse[1] <= Stat.screen_height/2+40:
                        days = initialize()
                        ending_screen(days)
        screen.fill((Stat.default_color))

        dr_strt.draw_startscreen(screen)
        pygame.display.update()


starting_screen()
