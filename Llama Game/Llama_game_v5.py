# Placed the background into the game

import pygame
import os

pygame.init()

SCREEN_HEIGHT = 600  # 600
SCREEN_WIDTH = 1100  # 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [pygame.image.load(os.path.join("Llama Game/Llama.png")),
           pygame.image.load(os.path.join("Llama Game/Llama2.png")),
           pygame.image.load(os.path.join("Llama Game/Llama3.png"))]

JUMPING = pygame.image.load(os.path.join("Llama Game/Llama.png"))

CACTUS = pygame.image.load(os.path.join("Llama Game/cactus.png"))

BACKGROUND = pygame.image.load(os.path.join("Llama Game/ground.png"))

class Llama:
    X_POS = 80
    Y_POS = 310
    JUMP_VEL = 8.5

    def __init__(self):
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.llama_run = True
        self.llama_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.llama_rect = self.image.get_rect()
        self.llama_rect.x = self.X_POS
        self.llama_rect.y = self.Y_POS

    def update(self, userInput):
        if self.llama_run:
            self.run()
        if self.llama_jump:
            self.jump()

        if self.step_index >= 15:
            self.step_index = 0

        if userInput [pygame.K_SPACE] and not self.llama_jump:
            self.llama_run = False
            self.llama_jump = True
        elif not self.llama_jump:
            self.llama_run = True
            self.llama_jump = False

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.llama_rect = self.image.get_rect()
        self.llama_rect.x = self.X_POS
        self.llama_rect.y = self.Y_POS
        self.step_index += 1


    def jump(self):
        self.image = self.jump_img
        if self.llama_jump:
            self.llama_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.llama_jump = False
            self.jump_vel = self.JUMP_VEL
    
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.llama_rect.x, self.llama_rect.y))


def main():
    global game_speed, bg_x_pos, bg_y_pos
    running = True
    clock = pygame.time.Clock()
    player = Llama()
    game_speed = 14
    bg_x_pos = 0
    bg_y_pos = 380

    def background():
        global bg_x_pos, bg_y_pos
        image_width = BACKGROUND.get_width()
        SCREEN.blit(BACKGROUND, (bg_x_pos, bg_y_pos))
        SCREEN.blit(BACKGROUND, (image_width + bg_x_pos, bg_y_pos))
        if bg_x_pos <= -image_width:
            SCREEN.blit(BACKGROUND, (image_width + bg_x_pos, bg_y_pos))
            bg_x_pos = 0
        bg_x_pos -= game_speed

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)

        background()

        clock.tick(30)
        pygame.display.update()


main()