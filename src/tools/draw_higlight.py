import pygame

def draw_highlight(screen, fill_color, non_hover_color, hover_color, width, height, xsize, ysize):
    mouse=pygame.mouse.get_pos()
    pygame.draw.rect(screen,fill_color,[width,height,xsize,ysize])
    if width-1 <= mouse[0] <= width+xsize+1 and height <= mouse[1] <= height+ysize+1:
        pygame.draw.rect(screen,hover_color,[width-1,height-1,xsize+2,ysize+2], 5, 3)  
    else:
        pygame.draw.rect(screen,non_hover_color,[width-1,height-1,xsize+2,ysize+2], 5, 3)