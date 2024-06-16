import pygame
import math
pygame.init()

window = pygame.display.set_mode((800,600))
pygame.display.set_caption("DOTA 3")

pygame_image = pygame.image.load("pipa.png")
pygame_rect = pygame_image.get_rect(center = (800//2, 600//2))

PURPLE =(127,0,255)
RED =  (255,0,0)
YELLOW = (255,255,0)

bull = []
bull_image = pygame.Surface((10,10))
bull_image.fill((0,0,0))




game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                mouse_x, mouse_y = pygame.mouse.get_pos()  
                angle = math.degrees (math.atan2( mouse_y - pygame_rect.centery, mouse_x - pygame_rect.centerx)) - 90
                bull_x = math.cos(angle) * 10
                bull_y = math.sin(angle) * 10
                bull.append([pygame_rect.centerx, pygame_rect.centery, bull_x, bull_y])


                



    mouse_x, mouse_y = pygame.mouse.get_pos()


    angle = math.degrees (math.atan2( mouse_y - pygame_rect.centery, mouse_x - pygame_rect.centerx)) - 90

    image_rotated = pygame.transform.rotate(pygame_image, -angle)
    new_rect = image_rotated.get_rect(center = pygame_rect.center)


    window.fill(PURPLE)
    window.blit(image_rotated, new_rect )

    for b in bull:
        b[0] += b[2]
        b[1] += b[3]
        

    for b in bull:
        window.blit(bull_image, (b[0], b[1]))

    
    pygame.display.flip()