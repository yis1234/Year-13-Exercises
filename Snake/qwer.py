# import pygame

import pygame


# defined the RGB color code for the background

background_colour = (139,0,0)


# defined the size of the screen (width, height)

screen = pygame.display.set_mode((600, 300))


# set caption

pygame.display.set_caption('GuidingCode.com')


# fill the screen with the above-defined background color

screen.fill(background_colour)

# update the display using flip

pygame.display.flip()

# keep the game looping

running = True


# game loop

while running:



# for loop through the event queue

   for event in pygame.event.get():

       # Check for QUIT event

       if event.type == pygame.QUIT:

           running = False
