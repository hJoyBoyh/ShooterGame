import pygame
def get_font(size):
        return pygame.font.Font("assets/font.ttf", size)
# detection click bouton
def click_dectection(rect, pos):
    return True if rect.collidepoint(pos[0], pos[1]) else False