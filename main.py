# -*- coding: utf-8 -*-


# Our Games Imports
import pygame
from pygame import mixer

pygame.init()
mixer.init()
screen = pygame.display.set_mode((500, 400))
done = False
x=60
y=60
image=pygame.image.load(r'wallpaper.jpg')
screen.blit(image, (0, 0))
pygame.mixer.music.load(r'song.mp3')
pygame.mixer.music.play(-1)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(x, y, 90, 90))

    pygame.display.flip()

    is_red = True
    color = (255, 0, 0)
    #in infinite while loop:-
    
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: 
            y -= 1
        if pressed[pygame.K_DOWN]: 
            y += 1
        if pressed[pygame.K_LEFT]: 
            x -= 1
        if pressed[pygame.K_RIGHT]: 
            x += 1	

        is_red = not is_red
        if is_red: 
            color = (255, 0, 0)
        else: 
            color = (102, 0, 0)			

    pygame.draw.rect(screen, color, pygame.Rect(x, y, 90, 90))

