import pygame

from services.finance import stock_creator as stcr
from services.finance import finance
from services.finance import items
from services.finance.finance import character_list
from services.day_change_op import day_change
from services.ending_screen_op import ending_init as endinit

from repositories import data_base_op as data_op
from repositories import stats

from ui.screen import draw_screen
from ui.screen import draw_ending as draw_en
from ui.screen import draw_start_screen as dr_strt

from ui.inputs import inputs
from ui.inputs import end_inputs
from ui.inputs import start_inputs


pygame.init()
Stat = stats.Stats()
pygame.display.set_caption(Stat.name)


screen = pygame.display.set_mode((Stat.screen_width, Stat.screen_height))

clock = pygame.time.Clock()
clock.tick(10)
mouse = pygame.mouse.get_pos()


def game_loop(shop_switch, whole_finance, day_switch, owned, stocks, item_list):
    """driver function for game loop.

    Args:
        shop_switch (Switch()): global boolian
        whole_finance (Finance()): players financial info
        day_switch (Switch): global boolian
        owned (list): list of owned stocks indexes
        stocks (matrix): matrix of stocks
        item_list (list): list of items

    Returns:
        list: itemlist which might have been changed with reroll
    """
    # Whether we are in shop or stock view
    if shop_switch.take:
        rerolled = inputs.inputter_market(
            shop_switch, item_list, whole_finance, day_switch)
        if rerolled:
            item_list = items.item_giver()
        draw_screen.draw_shop(item_list, screen, whole_finance)
        if not shop_switch.take:
            draw_screen.blank(screen)
    else:
        inputs.inputter_stock(owned, stocks, whole_finance,
                              shop_switch, day_switch, screen)
        draw_screen.draw_stocks(stocks, screen)
        draw_screen.draw_owned(owned, screen)
        if shop_switch.take:
            draw_screen.blank(screen)
    return item_list


def run(list_of_things):
    """Main loop. takes value from initialize and calls for
    gamelogic functions and pygame inputs and draw_screens.
    Also operates day change operator. after done
    looping will return back to starting_screen function

    Args:
        list_of_things (list): includes all required objects from initialize to run the game

    Returns:
        days: the amount of days player survived
    """
    lot = list_of_things
    stocks = lot[0]
    whole_finance = lot[1]
    owned = lot[2]
    shop_switch = lot[3]
    item_list = lot[4]
    day_switch = lot[5]
    timer = lot[6]
    screen.fill((Stat.default_color))
    loop = True
    original_reroll = whole_finance.reroll_price
    # MAIN LOOP
    while loop:
        time_difference = pygame.time.get_ticks()-timer.start_time
        # game_loop
        item_list = game_loop(shop_switch, whole_finance,
                              day_switch, owned, stocks, item_list)
        # Draws finance info
        draw_screen.draw_info(whole_finance, time_difference, timer, screen)
        # Checking if player has clicked end or timer has run out.
        # If so, engages day_change_operations or ends game if not enough money
        if 30-time_difference/1000 <= 0 or day_switch.take:
            day_switch.take = False
            draw_screen.whole_blank(screen)
            if whole_finance.exp > whole_finance.money:
                break
            summary_list = day_change.day_change(
                stocks, whole_finance, owned, timer)
            summary = summary_list[0]
            item_list = summary_list[1]
            stocks = summary_list[2]
            whole_finance.reroll_price = original_reroll
            summary_loop = True

            while summary_loop:
                summary_loop = day_change.summary_driver(
                    screen, summary, whole_finance, summary_loop)
                pygame.display.update()

            draw_screen.whole_blank(screen)
            timer.start_time = pygame.time.get_ticks()

        pygame.display.update()
    return timer.day


def character_select():
    """driver code for character select screen operations

    Returns:
        list: list of selected character attributes
    """
    draw_screen.draw_character_select(screen, character_list)
    character = inputs.character_select_input(character_list)
    return character


def initialize():
    """A function for calling all the setup functions for the
    game to start and settting up all objects used to run the game
    also lets the player choose their character

    Returns:
        days: the amount of days the player lasted.
    """
    draw_screen.whole_blank(screen)
    # Character select loop
    character = None
    while character is None:
        character = character_select()
        pygame.display.update()

    stocks = stcr.create_stocks()
    money = finance.Finance(character)
    owned = stats.Owned_stocks()
    switch = stats.Switch()
    day_switch = stats.Switch()
    time = stats.Timer()
    item_list = items.item_giver()

    return run([stocks, money, owned, switch, item_list, day_switch, time])


def ending_screen(days):
    """The function that runs everything that happens
    after the player cant pay the daily expenses.
    Is responsible for calling data_base related functions
    and calling ending screen related pygame functions

    Args:
        days (int): the "highscore" of player
    """
    data_base = data_op.Data_base_op()
    need_name = endinit.need_new_name(days, data_base)
    cursor_position = 0
    breaker = False
    while True:
        if need_name:
            draw_en.draw_name_need(data_base, screen)
            ret_tuple = end_inputs.name_inputs(
                data_base, need_name, cursor_position)
            need_name, cursor_position = ret_tuple[0], ret_tuple[1]
        else:
            draw_en.draw_hs(data_base, screen)
            breaker = end_inputs.next_inputs()
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
        start_game = start_inputs.start_inputs()
        if start_game:
            days = initialize()
            ending_screen(days)
        screen.fill((Stat.default_color))

        dr_strt.draw_start_screen(screen)
        pygame.display.update()


starting_screen()
