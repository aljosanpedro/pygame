# SURFACES
# Rects
    # don't merge, ex. pygame.Surface((0,0)).fill("blue")
    # types change -> not recog by blit
# test_surface = pygame.Surface((100,200))
# test_surface.fill("blue")

# EVENTS
# can call events via event loop, or via pygame.mouse/key/etc
    # for general events, use the event looop
    # for events inside classes, use class calls
    
# screen.fill("green")
# pygame.draw.line(screen,"black",(0,0),(screen.get_width(),screen.get_height()))

# if player_rect.colliderect(snail_rect):
    #     print("hit")
    
# mouse_position = pygame.mouse.get_pos()
# if player_rect.collidepoint(mouse_position):
#     print(pygame.mouse.get_pressed())

# keys = pygame.key.get_pressed()
# if keys[pygame.K_SPACE]:
#     print("jump")
