import pygame
import time

pygame.init()

screen = pygame.display.set_mode((1000, 750))
game_icon = pygame.image.load('snake_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Snake game – by Sun Woo Yi")

running = True

# game loop
counter = 0
while running:
    print(counter)
    time.sleep(1)
    counter += 1


    # for loop through the event queue

    for event in pygame.event.get():

        # Check for QUIT event

        if event.type == pygame.QUIT:
            running = False

# time.sleep(5)
pygame.quit()
quit()
