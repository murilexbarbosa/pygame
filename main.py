# -*- coding: utf-8 -*-


# Our Games Imports
import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
done = False
x=60
y=60

while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pygame.draw.rect(screen, (0,128,255), pygame.Rect(x, y, 90, 90))        
        pygame.display.flip()
