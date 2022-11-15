import tools.draw_higlight as draw_hl
import tools.draw_normal as draw_no
import pygame

import sys
pygame.init()
screen_width = 64*15
screen_height= 64*12
startfont=pygame.font.SysFont("comicsans",60)
smallfont=pygame.font.SysFont("comicsans",25)
infofont=pygame.font.SysFont("comicsans",30)
default_color="#172226"
lighter_default_color="#2d424a"
darker_default_color="#131b1f"
midlight_default_color="#203036"


def draw_summary(screen, summary, finance):
    pygame.draw.rect(screen,midlight_default_color,[screen_width/2-250,screen_height/2-250,500,500])
    draw_hl.draw_highlight(screen, midlight_default_color, darker_default_color, lighter_default_color, screen_width/2-100, screen_height/2+30, 190, 100)
    draw_no.draw_txt(infofont, "Net  Worth:", "white", screen, screen_width/2-200, screen_height/2-200)
    draw_no.draw_txt(startfont, "okey", "white", screen, screen_width/2-70, screen_height/2+30)
    draw_no.draw_txt(infofont, str(summary), "white", screen, screen_width/2, screen_height/2-200)
    draw_no.draw_txt(infofont, "Money:", "white", screen, screen_width/2-200, screen_height/2-150)
    draw_no.draw_txt(infofont, str(finance.money), "white", screen, screen_width/2, screen_height/2-150)
    draw_no.draw_txt(infofont, "New Expenses:", "white", screen, screen_width/2-200, screen_height/2-100)
    draw_no.draw_txt(infofont, str(finance.exp), "white", screen, screen_width/2+20, screen_height/2-100)
    
def drawinfo(m, timedifference, timer, screen):
    pygame.draw.rect(screen,midlight_default_color,[20,20,300,200])
    pygame.draw.rect(screen,darker_default_color,[20,20,300,200], 5, 3)
    moneysentence=infofont.render("Money: ", True, "white")
    if m.money>=m.exp:
        money=infofont.render(str(m.money), True, "white")
    else:
        money=infofont.render(str(m.money), True, "red")
    expsentence=infofont.render("expenses", True, "white")
    expense=infofont.render(str(m.exp), True, "red")
    incsentence=infofont.render("income", True, "white")
    income=infofont.render(str(m.inc), True, "green")
    screen.blit(moneysentence, (60,40))
    screen.blit(money, (230,40))
    screen.blit(expsentence, (60,90))
    screen.blit(expense, (230, 90))
    screen.blit(incsentence, (60, 140))
    screen.blit(income, (230, 140))
    timedifference=30-timedifference/1000
    draw_hl.draw_highlight(screen, midlight_default_color, darker_default_color, lighter_default_color, screen_width/2-155, 160, 100, 50)
    draw_no.draw_txt(infofont, "END", "white", screen, screen_width/2-140, 165)
    pygame.draw.rect(screen,midlight_default_color,[screen_width/2-130,100,50,40])
    draw_no.draw_txt(infofont, str(round(timedifference)), "white", screen, screen_width/2-123, 100)
    draw_no.draw_txt(infofont, "D a y", "white", screen, screen_width/2-140, 10)
    draw_no.draw_txt(infofont, str(timer.day), "white", screen, screen_width/2-115, 50)
    
    
def blank(screen):
    pygame.draw.rect(screen,default_color,[screen_width/2-50,0,800,800])
    
def wholeblank(screen):
    pygame.draw.rect(screen,default_color,[0,0,1600,1600]) 
    
    
def drawowned(o, screen):
    startheight=10
    mouse=pygame.mouse.get_pos()
    for i in range(10):
        amount=smallfont.render(str(o.owned[i]), True, "white")
        pygame.draw.rect(screen,midlight_default_color,[screen_width/2-50,startheight+8,45,45])
        pygame.draw.rect(screen,darker_default_color,[screen_width/2-50,startheight+8,45,45], 5, 3)
        if o.owned[i]>=10:
            screen.blit(amount, (screen_width/2-40,startheight+15))
        else:
            screen.blit(amount, (screen_width/2-35,startheight+15))
        startheight+=65
    draw_hl.draw_highlight(screen, midlight_default_color, darker_default_color, lighter_default_color, screen_width/2+50, startheight+8, 400, 88)
    shoptxt=startfont.render("market", True, "white")
    screen.blit(shoptxt, (screen_width/2+140,startheight+10))
    
    
def drawshop(itemlist, screen):
    mouse=pygame.mouse.get_pos()
    draw_hl.draw_highlight(screen, midlight_default_color, darker_default_color, lighter_default_color, screen_width/2+50, 668, 400, 88)
    shoptxt=startfont.render("stocks", True, "white")
    screen.blit(shoptxt, (screen_width/2+140,660+10))
    draw_hl.draw_highlight(screen, midlight_default_color, darker_default_color, lighter_default_color, screen_width/2+10, 50, 450, 175)
    draw_hl.draw_highlight(screen, midlight_default_color, darker_default_color, lighter_default_color, screen_width/2+10, 250, 450, 175)
    draw_hl.draw_highlight(screen, midlight_default_color, darker_default_color, lighter_default_color, screen_width/2+10, 450, 450, 175)
    if itemlist[0].sold==False:
        draw_no.draw_thing(smallfont, infofont, smallfont, itemlist[0], screen, screen_width/2+10, 50)
    else:
        draw_no.draw_sold(startfont, screen, screen_width/2+10, 50)
    if itemlist[1].sold==False:
        draw_no.draw_thing(smallfont, infofont, smallfont, itemlist[1], screen, screen_width/2+10, 250)
    else:
        draw_no.draw_sold(startfont, screen, screen_width/2+10, 250)
    if itemlist[2].sold==False:
        draw_no.draw_thing(smallfont, infofont, smallfont, itemlist[2], screen, screen_width/2+10, 450)
    else:
        draw_no.draw_sold(startfont, screen, screen_width/2+10, 450)
        
        
def drawstocks(stocks, screen):
    mouse = pygame.mouse.get_pos()
    day_stocks=stocks[len(stocks)-1]
    startheight=10
    for stock in day_stocks:
        draw_hl.draw_highlight(screen, midlight_default_color, darker_default_color, lighter_default_color, screen_width/2+10, startheight+8, 450, 45)
        if stock[3]>0:
            risecolor="green"
        else:
            risecolor="red"
        draw_no.draw_txt(smallfont, str(stock[0]), "white", screen, screen_width/2+30, startheight+13)
        draw_no.draw_txt(smallfont, str(stock[1]), "white", screen, screen_width/2+300, startheight+13)
        draw_no.draw_txt(smallfont, str(stock[3]), risecolor, screen, screen_width/2+400, startheight+13)
        startheight+=65