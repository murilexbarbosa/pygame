# -*- coding: utf-8 -*-


# Our Games Imports
import pygame
from pygame import mixer

pygame.init()
mixer.init()
screen = pygame.display.set_mode((500, 500))
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