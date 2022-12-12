import pygame
import sys
pygame.init()


def name_inputs(data_base, name_bool, cursor_position):
    """inputs for name giving screen
    Args:
        data_base (data_base object): 
        name_bool (bool): bool to break out of callers loop
        cursor_position (int): index of players writing cursor
    Returns:
        tuple: [0] to break out of callers loop and [1] to retrun updated cursor position
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                data_base.namechange()
                name_bool = False
            elif event.key == pygame.K_BACKSPACE:
                if cursor_position > 0:
                    if cursor_position == 1:
                        data_base.score_list[data_base.ind][0] = "____"
                    else:
                        data_base.score_list[data_base.ind][0] = data_base.score_list[data_base.ind][0][:cursor_position -
                                                                                                  1] + "_" + data_base.score_list[data_base.ind][0][cursor_position:]

                    cursor_position -= 1
            else:

                if cursor_position < 4:
                    data_base.score_list[data_base.ind][0] = data_base.score_list[data_base.ind][0][:cursor_position] + \
                        event.unicode + \
                        data_base.score_list[data_base.ind][0][cursor_position+1:]
                    cursor_position += 1
    return (name_bool, cursor_position)


def next_inputs():
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
