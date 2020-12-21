import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))

while (True):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            exit()
    
    screen.fill((0,0,0))
    
    color = (255, 255, 255)
    mb = pygame.mouse.get_pressed()
    if (mb[0]):
        color = (255, 0, 0)
    elif (mb[2]):
        color = (0, 255, 0)

    pos = pygame.mouse.get_pos()

    pygame.draw.circle(screen, color, pos, 20, 5)

    pygame.display.flip()
