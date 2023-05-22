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

PLAYER_JUMP_SPEED = -20 # negative

SNAIL_MIN_SPEED = 5
SNAIL_MAX_SPEED = SNAIL_MIN_SPEED * 2

# SETUP
screen = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption(TITLE)

font = pygame.font.Font(FONT,FONT_SIZE)

clock = pygame.time.Clock()

game_running = True

# SURFACES
# Images
# backgrounds
sky_image = pygame.image.load("graphics/sky.png").convert()
sky_rect = sky_image.get_rect(topleft = (0,0))

ground_image = pygame.image.load("graphics/ground.png").convert()
ground_rect = ground_image.get_rect(topleft = (0,sky_image.get_height()))

# characters
player_image = pygame.image.load("graphics/player/player_stand.png").convert_alpha()
player_default_position = (player_image.get_width()*(1.5),ground_rect.y)
player_rect = player_image.get_rect(midbottom = player_default_position)
player_gravity = 0
player_on_ground = True

snail_image = pygame.image.load("graphics/snail/snail_1.png").convert_alpha()
snail_rect = snail_image.get_rect(midbottom = (screen.get_width()-snail_image.get_width()*(1.5),ground_rect.y))
snail_speed = SNAIL_MIN_SPEED

# Texts
score_value = 0
score_string = f"Score: {score_value}"

score_text = font.render(score_string,False,"black")
score_position = (screen.get_width()/2-50, screen.get_height()/3)
score_rect = score_text.get_rect(center = (screen.get_width()/2,screen.get_height()/8))
score_bg_color = "#c0e8ec" # add '#' at start

# GAME LOOP
while game_running:
    # Variables
    mouse_position = (0,0)
    mouse_clicked = False
    
    # Events
    for event in pygame.event.get():
        match event.type:
            # Quit
            case pygame.QUIT:
                game_running = False
                
            # Buttons
            case pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_on_ground:
                    player_gravity = PLAYER_JUMP_SPEED
                    player_on_ground = False
                
            # Mouse
            case pygame.MOUSEBUTTONDOWN:
                if player_on_ground:
                    player_gravity = PLAYER_JUMP_SPEED
                    player_on_ground = False
                    
    # Screen
    # backgrounds
    screen.blit(sky_image,sky_rect)
    screen.blit(ground_image,ground_rect)
    
    # text
    # 1st rect draws border only bc of 4th arg. 2nd rect draws insides.
    pygame.draw.rect(screen,score_bg_color,score_rect,6,20)
    pygame.draw.rect(screen,score_bg_color,score_rect)
    
    score_string = f"Score: {score_value}"
    score_text = font.render(score_string,False,"black")
    
    screen.blit(score_text,score_rect)
    
    # characters
    # player
    player_rect.y += player_gravity
    player_gravity += 1
    
    if player_rect.bottom >= ground_rect.top:
        player_rect.bottom = ground_rect.top
        player_on_ground = True
    
    screen.blit(player_image,player_rect)
    
    # snail
    screen.blit(snail_image,snail_rect)
    snail_rect.x -= snail_speed
    
    if snail_rect.right <= 0:
        snail_rect.left = screen.get_width()
        snail_speed = randint(SNAIL_MIN_SPEED,SNAIL_MAX_SPEED)
    
        score_value += 1
    
    # player-snail interaction
    if player_rect.colliderect(snail_rect):
        game_running = False

    
    # Frame
    clock.tick(FPS)
    pygame.display.update()

# QUIT    
pygame.quit()
