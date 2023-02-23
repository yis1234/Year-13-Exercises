import pygame
import time
import random

pygame.init()

screen = pygame.display.set_mode((1000, 750))
game_icon = pygame.image.load('snake_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Snake game – by Sun Woo Yi")

# Tuples containing the colours to be used in the game
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (187, 227, 199)
yellow = (255, 255, 0)

score_font = pygame.font.SysFont("snake chan.ttf", 20)
exit_font = pygame.font.SysFont("freesansbold.ttf", 30)
msg_font = pygame.font.SysFont("arialblack", 20)

clock = pygame.time.Clock()  # Sets the speed at which the snake moves


def load_high_score():
    try:
        hi_score_file = open("HI_SCORE.txt", "r")
    except IOError:
        hi_score_file = open("HI_SCORE.txt", "w")
        hi_score_file.write("0")
    hi_score_file = open("HI_SCORE.txt", "r")
    value = hi_score_file.read()
    hi_score_file.close()
    return value


def update_high_score(score, hi_score):
    if int(score) > int(hi_score):
        return score
    else:
        return hi_score


def save_high_score(hi_score):
    hi_score_file = open("HI_SCORE.txt", "w")
    hi_score_file.write(str(hi_score))
    hi_score_file.close()


def player_score(score, score_colour, hi_score):
    display_score = score_font.render(f"Score: {score}", True, score_colour)
    screen.blit(display_score, (800, 20))

    # High Score
    display_score = score_font.render(f"High Score: {hi_score}", True,
                                      score_colour)
    screen.blit(display_score, (10, 10))

# Create snake - replaces the previous snake drawing section in main loop
def draw_snake(snake_list):
    print(f"snake_list: {snake_list}")
    for i in snake_list:
        pygame.draw.rect(screen, red, [i[0], i[1], 20, 20])


def message(msg, txt_colour, bkgd_colour):
    txt = msg_font.render(msg, True, txt_colour, bkgd_colour)

    # Centre rectangle: 1000/2 = 500 and 720/2 = 360
    text_box = txt.get_rect(center=(500, 360))
    screen.blit(txt, text_box)


# Function to run the main game loop
def game_loop():
    quit_game = False
    game_over = False

    # snake will be 20 x 20 pixels
    snake_x = 480  # Centre point horizontally is (1000-20 snake width)/2 = 490
    snake_y = 340  # Centre point vertically is (720-20 snake height)/2 = 350

    snake_x_change = 0  # holds the value of changes in the x-coordinate
    snake_y_change = 0  # holds the value of changes in the y-coordinate
    snake_list = []
    snake_length = 1

    # Setting a random position for the food - to start
    food_x = round(random.randrange(20, 1000 - 20) / 20) * 20
    food_y = round(random.randrange(20, 750 - 20) / 20) * 20

    high_score = load_high_score()
    print(f"hi_score test: {high_score}")

    while not quit_game:
        # Give user the option to quit or play again when they die
        while game_over:
            save_high_score(high_score)
            screen.fill(white)
            message("You died! Press 'Q' to Quit or 'A' to play Again",
                    red, black)
            pygame.display.update()

            # Check if user wants to quit (Q) or play again (A)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        quit_game = True
                        game_over = False
                    if event.key == pygame.K_a:
                        game_loop()  # Restart the main game loop

        # Handling response if user presses 'X' - giving them the option to
        # quit, start a new game, or keep playing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                instructions = "Exit: X to Quit, Space to resume, R to reset"
                message(instructions, white, black)
                pygame.display.update()

                end = False
                while not end:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            quit_game = True
                            end = True

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_x:
                                quit_game = True
                                end = True
                            if event.key == pygame.K_r:
                                end = True, game_loop()  # Restart the main game loop
                            if event.key == pygame.K_SPACE:
                                end = True  # Restart the main game loop

            # Handling snake movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change = -20
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_change = 20
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_x_change = 0
                    snake_y_change = -20
                elif event.key == pygame.K_DOWN:
                    snake_x_change = 0
                    snake_y_change = 20

        if snake_x >= 1000 or snake_x < 0 or snake_y >= 720 or snake_y < 0:
            game_over = True

        snake_x += snake_x_change
        snake_y += snake_y_change

        screen.fill(green)  # Changes screen (surface) from default black to green

        # Create snake (replaces simple rectangle in previous version)
        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True

        draw_snake(snake_list)

        score = snake_length - 1
        player_score(score, black)

        high_score = update_high_score(score, high_score)

        if score > 3:
            speed = score
        else:
            speed = 3

        # Create circle for food
        food = pygame.Rect(food_x, food_y, 20, 20)
        apple = pygame.image.load('apple_3.png').convert_alpha()
        resized_apple = pygame.transform.smoothscale(apple, [20, 20])
        screen.blit(resized_apple, food)

        pygame.display.update()

        print(f"Snake_x: {snake_x}")
        print(f"Food_x: {food_x}")
        print(f"Snake_y: {snake_y}")
        print(f"Food_y: {food_y}")
        print("\n\n")

        # Collision detection (see if snake touches food)
        if snake_x == food_x and snake_y == food_y:
            # Set random position for food if snake touches it:
            food_x = round(random.randrange(20, 1000 - 20) / 20) * 20
            food_y = round(random.randrange(20, 750 - 20) / 20) * 20
            print("Got it!")

            # Increase length of snake (by original size)
            snake_length += 1

        clock.tick(speed)  # sets the speed of at which each iteration of the game loop
        # runs in frames per second (fps). In this case it is set to 5fps

    pygame.quit()
    quit()


# Main routine
game_loop()
