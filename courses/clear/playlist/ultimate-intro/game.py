# IMPORTS
import pygame

# START
pygame.init()

# CONSTANTS
TITLE = "Runner"
RESOLUTION = (800,400)
FPS = 60

FONT = "font/Pixeltype.ttf"
FONT_SIZE = 50

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
sky_image = pygame.image.load("graphics/sky.png")
sky_position = (0,0)

ground_image = pygame.image.load("graphics/ground.png")
ground_position = (0,sky_image.get_height())

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
    screen.blit(sky_image,sky_position)
    screen.blit(ground_image, ground_position)
    screen.blit(title_text,title_position)
    
    # Update Frame
    clock.tick(FPS)
    pygame.display.update()

# QUIT    
pygame.quit()
