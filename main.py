#! /home/atmosmaciel/.workzone-python-virtual-envs/env-pygame/bin/python
# -*- coding: utf-8 -*-

# PingPong Game!
# By: atmosmaciel.github.io

# Our Games Imports
import sys
import os
import time
import pygame


# Verificando erros de inicializacao
check_errors = pygame.init()
if check_errors[1] > 0:
    print("(!) Ops, {0} o Pygame iniciou com algum problema..." . format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) O Pygame foi inicializado com sucesso!")


# Global Variables
color = pygame.Color(255, 255, 255, 255)  # background
width = 700
height = 700
size = (width, height)

# Play surface
playSurface = pygame.display.set_mode(size)
pygame.display.set_caption("PingPong Game!")
time.sleep(10)