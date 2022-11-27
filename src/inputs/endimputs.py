import pygame
import sys
pygame.init()


def nameinputs(database, namebool, cursorposition):
    """inputs for name giving screen

    Args:
        database (database object): 
        namebool (bool): bool to break out of callers loop
        cursorposition (int): index of players writing cursor

    Returns:
        tuple: [0] to break out of callers loop and [1] to retrun updated cursor position
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                database.namechange()
                namebool = False
            elif event.key == pygame.K_BACKSPACE:
                if cursorposition > 0:
                    if cursorposition == 1:
                        database.scorelist[database.ind][0] = "____"
                    else:
                        database.scorelist[database.ind][0] = database.scorelist[database.ind][0][:cursorposition -
                                                                                                  1] + "_" + database.scorelist[database.ind][0][cursorposition:]

                    cursorposition -= 1
            else:

                if cursorposition < 4:
                    database.scorelist[database.ind][0] = database.scorelist[database.ind][0][:cursorposition] + \
                        event.unicode + \
                        database.scorelist[database.ind][0][cursorposition+1:]
                    cursorposition += 1
    return (namebool, cursorposition)


def nextinputs():
    """inputs for play again or quit buttons

    Returns:
        bool: a bool to break out of callers loop
    """
    screen_width = 64*15
    screen_height = 64*12
    breaker = False
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if screen_width/2-400 <= mouse[0] <= screen_width/2-100 and screen_height/2-300 <= mouse[1] <= screen_height/2-100:
                breaker = True
            if screen_width/2-400 <= mouse[0] <= screen_width/2-100 and screen_height/2 <= mouse[1] <= screen_height/2+200:
                pygame.quit()
                sys.exit()
    return breaker
