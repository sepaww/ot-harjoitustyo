import sys
from services.finance import effects as effects
from services.finance.stockcreator import create_historyview
from repositories.stats import Stats
from ui.screen.draw_screen import draw_historyview
import pygame
pygame.init()
Stat = Stats()


def quitevent(event):
    """a function to remove copypaste from other funtions. handles pygame.quit() call

    Args:
        event (pygame.event)
    """
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()


def summaryinput(summaryloop):
    """input for summary screen

    Args:
        summaryloop (bool): a boolian to know when to break out of callers loop

    Returns:
        bool: same bool
    """
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        quitevent(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Stat.screen_width/2-100 <= mouse[0] <= Stat.screen_width/2+90 and Stat.screen_height/2+30 <= mouse[1] <= Stat.screen_height/2+130:
                summaryloop = False
    return summaryloop


def inputter_stock(ol, stocks, money, switch, dayswitch, screen):
    """imputs for stock screen. handles buying stocks and related operations, such as money deduction.

    Args:
        ol (list): list of owned stocks
        stocks (matrix): list of stocks
        money (Finance object): players money info
        switch (Global boolian): a boolian to switch to shop view
        dayswitch (Global boolian): a boolian for breaking out of callers loop
    """
    mouse = pygame.mouse.get_pos()
    left = 1
    right = 3

    for event in pygame.event.get():
        quitevent(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            startheight = 10
            id = None
            for i in range(10):
                if Stat.screen_width/2+250 <= mouse[0] <= Stat.screen_width/2+280 and startheight+15 <= mouse[1] <= startheight+45:
                    price_list = create_historyview(stocks, i)
                    draw_historyview(price_list, screen)
                    break
                elif Stat.screen_width/2 <= mouse[0] <= Stat.screen_width/2+600 and startheight <= mouse[1] <= startheight+60:
                    id = i
                    break

                startheight += 65
            startheight = 660
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
            if Stat.screen_width/2+50 <= mouse[0] <= Stat.screen_width/2+450 and startheight+8 <= mouse[1] <= startheight+88:

                switch.take = True
            elif Stat.screen_width/2-155 <= mouse[0] <= Stat.screen_width/2-55 and 160 <= mouse[1] <= 210:
                dayswitch.take = True


def inputter_market(switch, itemlist, wholefinance, dayswitch):
    """handles inputs for shop screen and related actions

    Args:
        switch (bool): a tool to switch back to stock view
        itemlist (list): includes all the items for the day
        wholefinance (Finance object): players money situation
        dayswitch (bool): a bool to know when to break out of callers loop
    """
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        quitevent(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Stat.screen_width/2+50 <= mouse[0] <= Stat.screen_width/2+450 and 660+8 <= mouse[1] <= 660+88:

                switch.take = False
            elif Stat.screen_width/2+10 <= mouse[0] <= Stat.screen_width/2+450 and 50 <= mouse[1] <= 225 and itemlist[0].sold == False:
                if wholefinance.money >= itemlist[0].price:
                    wholefinance.change_amount(itemlist[0].price)
                    effects.apply_effect(itemlist[0].effect, wholefinance)
                    itemlist[0].sold = True
            elif Stat.screen_width/2+10 <= mouse[0] <= Stat.screen_width/2+450 and 250 <= mouse[1] <= 425 and itemlist[1].sold == False:
                if wholefinance.money >= itemlist[1].price:
                    wholefinance.change_amount(itemlist[1].price)
                    effects.apply_effect(itemlist[1].effect, wholefinance)
                    itemlist[1].sold = True
            elif Stat.screen_width/2+10 <= mouse[0] <= Stat.screen_width/2+450 and 450 <= mouse[1] <= 625 and itemlist[2].sold == False:
                if wholefinance.money >= itemlist[2].price:
                    wholefinance.change_amount(itemlist[2].price)
                    effects.apply_effect(itemlist[2].effect, wholefinance)
                    itemlist[2].sold = True
            elif Stat.screen_width/2-155 <= mouse[0] <= Stat.screen_width/2-55 and 160 <= mouse[1] <= 210:
                dayswitch.take = True
            elif Stat.screen_width/2-150 <= mouse[0] <= Stat.screen_width/2 and Stat.screen_height/2+250 <= mouse[1] <= Stat.screen_height/2+350:
                if wholefinance.money >= wholefinance.rerollprice:
                    wholefinance.change_amount(wholefinance.rerollprice)
                    wholefinance.reroll_doubler()
                    return True
            return False


def character_select_input(character_list):
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        quitevent(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Stat.screen_width/2-450 <= mouse[0] <= Stat.screen_width/2+50 and Stat.screen_height/2-350 <= mouse[1] <= Stat.screen_height/2-50:
                return character_list[0]
            if Stat.screen_width/2+50 <= mouse[0] <= Stat.screen_width/2+450 and Stat.screen_height/2-350 <= mouse[1] <= Stat.screen_height/2-50:
                return character_list[1]
            if Stat.screen_width/2-450 <= mouse[0] <= Stat.screen_width/2+50 and Stat.screen_height/2+50 <= mouse[1] <= Stat.screen_height/2+350:
                return character_list[2]
            if Stat.screen_width/2+50 <= mouse[0] <= Stat.screen_width/2+450 and Stat.screen_height/2+50 <= mouse[1] <= Stat.screen_height/2+350:
                return character_list[3]
