import pygame
def draw_txt(font, text, color, screen, posx, posy):
    txt=font.render(text, True, color)
    screen.blit(txt, (posx,posy))
    
def draw_thing(smallfont, largefont, font, item, screen, posx, posy):
    
    headtxt=largefont.render(item.name, True, "white")
    effecttxt=smallfont.render(item.effectstr, True, "white")
    description=smallfont.render(item.description, True, "white")
    pricesentence=largefont.render("Price:", True, "white")
    price=largefont.render(str(item.price), True, "white")
    screen.blit(headtxt, (posx+10,posy+10))
    screen.blit(description, (posx+10,posy+90))
    screen.blit(effecttxt, (posx+10,posy+130))
    screen.blit(pricesentence, (posx+10, posy+50))
    screen.blit(price, (posx+200, posy+50))
    
def draw_sold(font, screen, posx, posy):
    soldtxt=font.render("sold", True, "white")
    screen.blit(soldtxt, (posx+10,posy+90))
    