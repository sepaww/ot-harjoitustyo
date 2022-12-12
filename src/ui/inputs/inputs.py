import sys
from services.finance import effects as effects
from services.finance.stock_creator import create_history_view
from repositories.stats import Stats
from ui.screen.draw_screen import draw_history_view
import pygame
pygame.init()
Stat = Stats()


def quit_event(event):
    """a function to remove copypaste from other funtions. handles pygame.quit() call

    Args:
        event (pygame.event)
    """
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()


def summary_input(summary_loop):
    """input for summary screen

    Args:
        summary_loop (bool): a boolian to know when to break out of callers loop

    Returns:
        bool: same bool
    """
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        quit_event(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Stat.screen_width/2-100 <= mouse[0] <= Stat.screen_width/2+90 and Stat.screen_height/2+30 <= mouse[1] <= Stat.screen_height/2+130:
                summary_loop = False
    return summary_loop


def inputter_stock(ol, stocks, money, switch, day_switch, screen):
    """imputs for stock screen. handles buying stocks and related operations, such as money deduction.

    Args:
        ol (list): list of owned stocks
        stocks (matrix): list of stocks
        money (Finance object): players money info
        switch (Global boolian): a boolian to switch to shop view
        day_switch (Global boolian): a boolian for breaking out of callers loop
    """
    mouse = pygame.mouse.get_pos()
    left = 1
    right = 3

    for event in pygame.event.get():
        quit_event(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_height = 10
            id = None
            for i in range(10):
                if Stat.screen_width/2+250 <= mouse[0] <= Stat.screen_width/2+280 and start_height+15 <= mouse[1] <= start_height+45:
                    price_list = create_history_view(stocks, i)
                    draw_history_view(price_list, screen)
                    break
                elif Stat.screen_width/2 <= mouse[0] <= Stat.screen_width/2+600 and start_height <= mouse[1] <= start_height+60:
                    id = i
                    break

                start_height += 65
            start_height = 660
            if id != None:
                curstock = stocks[-1][id]
                if event.button == left:
                    price = curstock[1]
                    if money.money >= price:
                        money.change_amount(price)
                        ol.owned[id] += 1

                elif event.button == right:
                    if ol.owned[id] > 0:
                        price = curstock[1]
                        money.change_amount_up(price)
                        ol.owned[id] -= 1
            if Stat.screen_width/2+50 <= mouse[0] <= Stat.screen_width/2+450 and start_height+8 <= mouse[1] <= start_height+88:

                switch.take = True
            elif Stat.screen_width/2-155 <= mouse[0] <= Stat.screen_width/2-55 and 160 <= mouse[1] <= 210:
                day_switch.take = True


def inputter_market(switch, item_list, whole_finance, day_switch):
    """handles inputs for shop screen and related actions

    Args:
        switch (bool): a tool to switch back to stock view
        item_list (list): includes all the items for the day
        whole_finance (Finance object): players money situation
        day_switch (bool): a bool to know when to break out of callers loop
    """
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        quit_event(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Stat.screen_width/2+50 <= mouse[0] <= Stat.screen_width/2+450 and 660+8 <= mouse[1] <= 660+88:

                switch.take = False
            elif Stat.screen_width/2+10 <= mouse[0] <= Stat.screen_width/2+450 and 50 <= mouse[1] <= 225 and item_list[0].sold == False:
                if whole_finance.money >= item_list[0].price:
                    whole_finance.change_amount(item_list[0].price)
                    effects.apply_effect(item_list[0].effect, whole_finance)
                    item_list[0].sold = True
            elif Stat.screen_width/2+10 <= mouse[0] <= Stat.screen_width/2+450 and 250 <= mouse[1] <= 425 and item_list[1].sold == False:
                if whole_finance.money >= item_list[1].price:
                    whole_finance.change_amount(item_list[1].price)
                    effects.apply_effect(item_list[1].effect, whole_finance)
                    item_list[1].sold = True
            elif Stat.screen_width/2+10 <= mouse[0] <= Stat.screen_width/2+450 and 450 <= mouse[1] <= 625 and item_list[2].sold == False:
                if whole_finance.money >= item_list[2].price:
                    whole_finance.change_amount(item_list[2].price)
                    effects.apply_effect(item_list[2].effect, whole_finance)
                    item_list[2].sold = True
            elif Stat.screen_width/2-155 <= mouse[0] <= Stat.screen_width/2-55 and 160 <= mouse[1] <= 210:
                day_switch.take = True
            elif Stat.screen_width/2-150 <= mouse[0] <= Stat.screen_width/2 and Stat.screen_height/2+250 <= mouse[1] <= Stat.screen_height/2+350:
                if whole_finance.money >= whole_finance.reroll_price:
                    whole_finance.change_amount(whole_finance.reroll_price)
                    whole_finance.reroll_doubler()
                    return True
            return False


def character_select_input(character_list):
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        quit_event(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Stat.screen_width/2-450 <= mouse[0] <= Stat.screen_width/2+50 and Stat.screen_height/2-350 <= mouse[1] <= Stat.screen_height/2-50:
                return character_list[0]
            if Stat.screen_width/2+50 <= mouse[0] <= Stat.screen_width/2+450 and Stat.screen_height/2-350 <= mouse[1] <= Stat.screen_height/2-50:
                return character_list[1]
            if Stat.screen_width/2-450 <= mouse[0] <= Stat.screen_width/2+50 and Stat.screen_height/2+50 <= mouse[1] <= Stat.screen_height/2+350:
                return character_list[2]
            if Stat.screen_width/2+50 <= mouse[0] <= Stat.screen_width/2+450 and Stat.screen_height/2+50 <= mouse[1] <= Stat.screen_height/2+350:
                return character_list[3]
