import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))

pygame.mixer.music.load('cyberpunk.ogg')
pygame.mixer.music.play(0)

r = 0

while (True):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            exit()

    screen.fill((r,0,0))
    
    r = r + 0.01
    if (r > 255):
        r = 0

    pygame.display.flip()
