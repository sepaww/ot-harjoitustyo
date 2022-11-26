import screen.draw_screen as draw_screen
import pygame
import finance.stockhistory as st_hs
import day_change_op.day_change_operator as dop
import inputs.inputs as inputs
import finance.items as items
pygame.init
def daychange(stocks, finance, owned, timer):
    itemlist=items.itemgiver()
    stocks=st_hs.stock_update(stocks)
    timer.day+=1
    dop.finance_update(finance, timer)
    summary=dop.summary(stocks, finance, owned)
    return summary, itemlist, stocks


def summary_driver(screen, summary, finance, summaryloop):
        draw_screen.draw_summary(screen, summary, finance)
        summaryloop=inputs.summaryinput(summaryloop)
        return summaryloop
