import pygame
pygame.init()
import finance.effects as effects
import sys
screen_width = 64*15
screen_height= 64*12
def summaryinput(summaryloop):
    mouse=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if screen_width/2-100 <= mouse[0] <= screen_width/2+90 and screen_height/2+30 <= mouse[1] <= screen_height/2+130:
                summaryloop=False
    return summaryloop
      


def inputters(ol, stocks, money, switch, dayswitch):
    mouse=pygame.mouse.get_pos()
    left=1
    right=3
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                startheight=10
                id=None
                for i in range(10):
                    if screen_width/2 <= mouse[0] <= screen_width/2+600 and startheight <= mouse[1] <= startheight+60:
                        id=i
                        
                    startheight+=65
                if id!=None:
                    curstock=stocks[-1][id]
                    if event.button==left:
                        price=curstock[1]
                        if money.money>=price:
                            money.money-=price
                            ol.owned[id]+=1
                            
                    elif event.button==right:
                        if ol.owned[id]>0:
                            price=curstock[1]
                            money.money+=price
                            ol.owned[id]-=1
                if screen_width/2+50 <= mouse[0] <= screen_width/2+450 and startheight+8 <= mouse[1] <= startheight+88:
                    #print(startheight)
                    switch.take=True
                elif screen_width/2-155 <= mouse[0] <= screen_width/2-55 and 160 <= mouse[1] <= 210:
                    dayswitch.take=True
                #else: switch.take=False
                            
def inputterm(switch, itemlist, wholefinance, dayswitch):
    mouse=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
        if event.type == pygame.MOUSEBUTTONDOWN:
            if screen_width/2+50 <= mouse[0] <= screen_width/2+450 and 660+8 <= mouse[1] <= 660+88:
                print("stonk")
                switch.take=False
            elif screen_width/2+10 <= mouse[0] <= screen_width/2+450 and 50 <= mouse[1] <= 225 and itemlist[0].sold==False:
                if wholefinance.money>=itemlist[0].price:
                    wholefinance.money-=itemlist[0].price
                    effects.apply_effect(itemlist[0].effect, wholefinance)
                    itemlist[0].sold=True
            elif screen_width/2+10 <= mouse[0] <= screen_width/2+450 and 250 <= mouse[1] <= 425 and itemlist[1].sold==False:
                if wholefinance.money>=itemlist[1].price:
                    wholefinance.money-=itemlist[1].price
                    effects.apply_effect(itemlist[1].effect, wholefinance)           
                    itemlist[1].sold=True
            elif screen_width/2+10 <= mouse[0] <= screen_width/2+450 and 450 <= mouse[1] <= 625 and itemlist[2].sold==False:
                if wholefinance.money>=itemlist[2].price:
                    wholefinance.money-=itemlist[2].price
                    effects.apply_effect(itemlist[2].effect, wholefinance) 
                    itemlist[2].sold=True
            elif screen_width/2-155 <= mouse[0] <= screen_width/2-55 and 160 <= mouse[1] <= 210:
                dayswitch.take=True