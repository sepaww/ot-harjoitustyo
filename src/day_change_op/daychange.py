from screen import draw_screen as draw_screen
import pygame
from finance import stockhistory as st_hs
from day_change_op import day_change_operator as dop
from inputs import inputs as inputs
from finance import items as items
pygame.init


def daychange(stocks, finance, owned, timer):
    """handles the actions related to changing the ingame day
        also initializes updates to required ingame objects
    Args:
        stocks (matrix): matrix that includes the stocks and their history
        finance (Finance object): Player financial situation
        owned (list): the indexes of owned stocks and the amount of owned
        timer (Timer object): includes the amount of days, which will be rosen by 1

    Returns:
        int: networth
        list: the new itemlist
        matrix: updated stocks
    """
    itemlist = items.itemgiver()
    stocks = st_hs.stock_update(stocks)
    timer.day += 1
    dop.finance_update(finance, timer)
    summary = dop.summary(stocks, finance, owned)
    return summary, itemlist, stocks


def summary_driver(screen, summary, finance, summaryloop):
    """handles the actions required to running the summary screen

    Args:
        screen (pygame object): the screen
        summary (int): networth
        finance (Finance object): players financial status
        summaryloop (bool): a bool to break out of callers loop
    Returns:
        bool: a bool to break out of callers loop
    """
    draw_screen.draw_summary(screen, summary, finance)
    summaryloop = inputs.summaryinput(summaryloop)
    return summaryloop
