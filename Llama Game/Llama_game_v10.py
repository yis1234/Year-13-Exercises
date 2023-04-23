# Added a game icon and named the game "Llama game - by Sun Woo Yi"

import pygame
import os

pygame.init()

SCREEN_HEIGHT = 600  # 600
SCREEN_WIDTH = 1100  # 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_icon = pygame.image.load('Llama Game/llama_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Llama game - by Sun Woo Yi")

RUNNING = [pygame.transform.scale(pygame.image.load(os.path.join("Llama Game/Llama.png")), (87, 94)), 
           pygame.transform.scale(pygame.image.load(os.path.join("Llama Game/Llama2.png")), (87, 94)), 
           pygame.transform.scale(pygame.image.load(os.path.join("Llama Game/Llama3.png")), (87, 94))]

JUMPING = pygame.transform.scale(pygame.image.load(os.path.join("Llama Game/Llama.png")), (87, 94))

CACTUS = pygame.image.load(os.path.join("Llama Game/Cactus1.png"))

BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("Llama Game/ground.png")), (1000, 80))

class Llama:
    X_POS = 80
    Y_POS = 333
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

class Obstacle:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = 332

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < - self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, self.rect)

class Cactus:
    def __init__(self, image):
        super().__init__(image)

def main():
    global game_speed, bg_x_pos, bg_y_pos, points, obstacles
    running = True
    clock = pygame.time.Clock()
    player = Llama()
    game_speed = 14
    bg_x_pos = 0
    bg_y_pos = 380
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    death_count = 0

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)

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
                quit()

        SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)

        if len(obstacles) == 0:
            obstacles.append(Obstacle(CACTUS))
        
        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
        if player.llama_rect.colliderect(obstacle.rect):
            pygame.time.delay(2000)
            death_count += 1
            menu(death_count)
            

        background()

        score()

        clock.tick(30)
        pygame.display.update()


def menu(death_count):
    global points
    running = True
    while running:
        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
        elif death_count > 0:
            text = font.render("Press any Key to Restart", True, (0, 0, 0))
            score = font.render("Your Score: " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                main()
            if event.type == pygame.QUIT:
                running = False
                quit()



menu(death_count=0)