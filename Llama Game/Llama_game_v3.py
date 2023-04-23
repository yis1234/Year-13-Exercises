# Making a class for llama which makes the llama seem like its moving by
# constantly changing the llama image

import pygame
import os

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

LLAMA_RUN = [pygame.image.load(os.path.join("Llama Game/Llama.png")),
         pygame.image.load(os.path.join("Llama Game/Llama2.png")),
         pygame.image.load(os.path.join("Llama Game/Llama3.png"))]

LLAMA_JUMP = [pygame.image.load(os.path.join("Llama Game/Llama.png"))]

CACTUS = [pygame.image.load(os.path.join("Llama Game/cactus.png"))]

BACKGROUND = [pygame.image.load(os.path.join("Llama Game/ground.png"))]

class Llama:
    x = 80
    y = 310

    def __init__(self):
        self.run_img = LLAMA_RUN
        self.jump_img = LLAMA_JUMP

        self.llama_run = True
        self.llama_jump = False

        self.step_index = 0
        self.image = self.run_img[0]
        self.llama_rect = self.image.get_rect()
        self.llama_rect.x = self.x
        self.llama_rect.y = self.y

    def update(self, userInput):
        if self.llama_run:
            self.run()
        if self.llama_jump:
            self.jump()

        if self.step_index >= 15:
            self.step_index = 0

        if userInput [pygame.K_UP] or userInput[pygame.K_SPACE]:
            self.llama_run = False
            self.llama_jump = True
        else:
            self.llama_run = True
            self.llama_jump = False

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.llama_rect = self.image.get_rect()
        self.llama_rect.x = self.x
        self.llama_rect.y = self.y
        self.step_index += 1



    def jump(self):
        pass
    
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.llama_rect.x, self.llama_rect.y))


def main():
    running = True
    clock = pygame.time.Clock()
    player = Llama()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)

        clock.tick(30)
        pygame.display.update()


main()