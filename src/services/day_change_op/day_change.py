

from ui.screen import draw_screen
from ui.inputs import inputs
from services.finance import stock_history as st_hs
from services.finance import items
from services.day_change_op import day_change_operator as dop



def day_change(stocks, finance, owned, timer):
    """handles the actions related to changing the ingame day
        also initializes updates to required ingame objects
    Args:
        stocks (matrix): matrix that includes the stocks and their history
        finance (Finance object): Player financial situation
        owned (list): the indexes of owned stocks and the amount of owned
        timer (Timer object): includes the amount of days, which will be rosen by 1

    Returns:
        int: networth
        list: the new item_list
        matrix: updated stocks
    """
    item_list = items.item_giver()
    stocks = st_hs.stock_update(stocks)
    timer.day += 1
    dop.finance_update(finance, timer)
    summary = dop.summary(stocks, finance, owned)
    return summary, item_list, stocks


def summary_driver(screen, summary, finance, summary_loop):
    """handles the actions required to running the summary screen

    Args:
        screen (pygame object): the screen
        summary (int): networth
        finance (Finance object): players financial status
        summary_loop (bool): a bool to break out of callers loop
    Returns:
        bool: a bool to break out of callers loop
    """
    draw_screen.draw_summary(screen, summary, finance)
    summary_loop = inputs.summary_input(summary_loop)
    return summary_loop
