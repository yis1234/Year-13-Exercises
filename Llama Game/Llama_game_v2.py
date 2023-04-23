# Placing the images from the file into the game

import pygame
import os

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# This is so that the llama looks like it is moving which is why it is in a list
LLAMA = [pygame.image.load(os.path.join("Llama Game/Llama.png")),
         pygame.image.load(os.path.join("Llama Game/Llama2.png")),
         pygame.image.load(os.path.join("Llama Game/Llama3.png"))]

CACTUS = [pygame.image.load(os.path.join("Llama Game/cactus.png"))]

BACKGROUND = [pygame.image.load(os.path.join("Llama Game/ground.png"))]
