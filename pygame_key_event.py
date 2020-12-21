import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))

while (True):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            exit()
        if (event.type == pygame.KEYDOWN):
            print("Key = " + str(event.key))
            if (event.key == pygame.K_ESCAPE):
                exit()
