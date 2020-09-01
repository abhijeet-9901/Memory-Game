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

while running_starting_window: # ALL THESE PROCESSES TAKES PLACE WHEN THE WINDOW IS RUNNING
    current_event = event.get()
    x = gs.SCREEN_SIZE // 2 - -95   # POSITION OF THE TEXT
    y = gs.SCREEN_SIZE // 2 - -140
    left_top_x,left_top_y,right_bottom_x,right_bottom_y = display_message('START',(255,255,255),x,y,60)
    for e in current_event:
        if e.type == pygame.QUIT:
            exit()
            running_starting_window = False
        
        if e.type == pygame.MOUSEBUTTONDOWN:  # THIS PROCESS IS INITIATED WHEN THE MOUSE CLICKS THE TEXT
            mouse_x, mouse_y = pygame.mouse.get_pos()
            display_message('START',(51,102,225),x,y,60)
            if mouse_x >= x and mouse_y >= y and mouse_x <= x + right_bottom_x and mouse_y <= y + right_bottom_y :
                running_starting_window = False
    display.flip() 

matched = image.load('extra/good_job.png') # GETS EXECUTED WHEN THE TILES MATCH EACHOTHER

screen.fill((255,255,255))


print ("Good Bye")

###############################################################################

