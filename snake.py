import pygame
import time
import random

# Αρχικοποίηση του Pygame
pygame.init()

# Ορισμός χρωμάτων
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Διαστάσεις παραθύρου
width, height = 600, 400
snake_block = 10
speed = 15

# Δημιουργία παραθύρου
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Ρολόι για τον έλεγχο της ταχύτητας
clock = pygame.time.Clock()

# Γραμματοσειρά για τα μηνύματα
font = pygame.font.SysFont("bahnschrift", 25)

def show_score(score):
    value = font.render("Score: " + str(score), True, white)
    window.blit(value, [10, 10])

def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(window, green, [block[0], block[1], snake_block, snake_block])

def game_loop():
    game_over = False
    game_close = False

    # Αρχική θέση φιδιού
    x, y = width // 2, height // 2
    x_change, y_change = 0, 0

    snake_list = []
    length_of_snake = 1

    # Δημιουργία αρχικού φαγητού
    food_x = random.randrange(0, width - snake_block, 10)
    food_y = random.randrange(0, height - snake_block, 10)

    while not game_over:
        while game_close:
            window.fill(black)
            message = font.render("Game Over! Press Q to Quit or R to Restart", True, red)
            window.blit(message, [width / 6, height / 3])
            show_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        # Έλεγχος αν το φίδι βγήκε εκτός ορίων
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_change
        y += y_change
        window.fill(black)

        pygame.draw.rect(window, red, [food_x, food_y, snake_block, snake_block])

        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Έλεγχος αν το φίδι έφαγε τον εαυτό του
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_list)
        show_score(length_of_snake - 1)
        pygame.display.update()

        # Αν το φίδι φάει το φαγητό
        if x == food_x and y == food_y:
            food_x = random.randrange(0, width - snake_block, 10)
            food_y = random.randrange(0, height - snake_block, 10)
            length_of_snake += 1

        clock.tick(speed)

    pygame.quit()

# Εκκίνηση του παιχνιδιού
game_loop()
