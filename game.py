import pygame
import game_setting as gs

from pygame import display, event, image

# Intialize the pygame
pygame.init()

# create the screen
screen = display.set_mode((800, 800))

# Background
background = pygame.image.load('background.png')

# Caption and Icon
pygame.display.set_caption("Memory Game")
icon = pygame.image.load('ikon.png')
pygame.display.set_icon(icon)

def find_index(x,y):
    row = x // gs.IMAGE_SIZE
    col = y // gs.IMAGE_SIZE
    return row*gs.NUM_TILES_SIDE + col

#Describing the characteristics of the message
def display_message(msg,color,x,y,size):
    font = pygame.font.SysFont(None,size)
    screen_text = font.render(msg,True,color)
    screen.blit(background, (0, 0))
    screen.blit(screen_text,(x,y))
    return screen_text.get_rect()

running_starting_window = True

screen.fill((255,255,255))


print ("Good Bye")

###############################################################################

