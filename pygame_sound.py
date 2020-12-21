import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))

fx1 = pygame.mixer.Sound("fx1.wav")
fx2 = pygame.mixer.Sound("fx2.wav")
fx3 = pygame.mixer.Sound("fx3.wav")
fx4 = pygame.mixer.Sound("fx4.wav")

color = (0,0,0)

while (True):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            exit()
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_1):
                fx1.play()
                color = (255, 0, 0)
            if (event.key == pygame.K_2):
                fx2.play()
                color = (0, 255, 0)
            if (event.key == pygame.K_3):
                fx3.play()
                color = (0, 255, 255)
            if (event.key == pygame.K_4):
                fx4.play()
                color = (255, 255, 0)

    screen.fill(color)
    
    pygame.display.flip()
