import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))

while (True):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            exit()

    k = pygame.key.get_pressed()

    r, g, b = 255, 255, 255

    if (k[pygame.K_1]):
        r = 0
    if (k[pygame.K_2]):
        g = 0
    if (k[pygame.K_3]):
        b = 0
        
    screen.fill((0,0,0))

    pygame.draw.circle(screen, (r,g,b), (320, 240), 20, 5)

    pygame.display.flip()