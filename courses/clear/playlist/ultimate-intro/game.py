# IMPORTS
import pygame
from random import seed,randint

# START
pygame.init()
seed()

# CONSTANTS
TITLE = "Runner"
RESOLUTION = (800,400)
FPS = 60

FONT = "font/Pixeltype.ttf"
FONT_SIZE = 50

SNAIL_MIN_SPEED = 5
SNAIL_MAX_SPEED = SNAIL_MIN_SPEED * 2

# SETUP
screen = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption(TITLE)

font = pygame.font.Font(FONT,FONT_SIZE)

clock = pygame.time.Clock()

running = True

# SURFACES
# Rects
    # don't merge, ex. pygame.Surface((0,0)).fill("blue")
    # types change -> not recog by blit
# test_surface = pygame.Surface((100,200))
# test_surface.fill("blue")

# Images
# backgrounds
sky_image = pygame.image.load("graphics/sky.png").convert()
sky_rect = sky_image.get_rect(topleft = (0,0))

ground_image = pygame.image.load("graphics/ground.png").convert()
ground_rect = ground_image.get_rect(topleft = (0,sky_image.get_height()))

# characters
player_image = pygame.image.load("graphics/player/player_stand.png").convert_alpha()
player_rect = player_image.get_rect(midbottom = (player_image.get_width()*(1.5),ground_rect.y))

snail_image = pygame.image.load("graphics/snail/snail_1.png").convert_alpha()
snail_rect = snail_image.get_rect(midbottom = (screen.get_width()-snail_image.get_width()*(1.5),ground_rect.y))
snail_speed = SNAIL_MIN_SPEED

# Texts
title_text = font.render(TITLE,False,"black")
title_position = (screen.get_width()/2-50, screen.get_height()/3)

# GAME LOOP
while running:
    # Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Screen
    # screen.fill("green")
    # backgrounds
    screen.blit(sky_image,sky_rect)
    screen.blit(ground_image,ground_rect)
    
    screen.blit(title_text,title_position)
    
    # characters
    screen.blit(player_image,player_rect)
    
    screen.blit(snail_image,snail_rect)
    snail_rect.x -= snail_speed
    
    if snail_rect.x <= 0:
        snail_rect.left = screen.get_width()
        snail_speed = randint(SNAIL_MIN_SPEED,SNAIL_MAX_SPEED)
    
    # Frame
    clock.tick(FPS)
    pygame.display.update()

# QUIT    
pygame.quit()
