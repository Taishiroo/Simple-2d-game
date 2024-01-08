import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600

# Set up the drawing window
screen = pygame.display.set_mode([screen_width, screen_height])

# Set up the snake
snake_size = 20
snake_speed = 20
snake = [(100, 100), (90, 100), (80, 100)]  # Initial snake position
direction = (snake_speed, 0)  # Initial movement direction

# Set up the food
food_size = 20
food = (random.randint(0, screen_width - food_size), random.randint(0, screen_height - food_size))

# Run until the user asks to quit
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Update the snake direction based on arrow key input
    if keys[pygame.K_LEFT] and direction != (snake_speed, 0):
        direction = (-snake_speed, 0)
    if keys[pygame.K_RIGHT] and direction != (-snake_speed, 0):
        direction = (snake_speed, 0)
    if keys[pygame.K_UP] and direction != (0, snake_speed):
        direction = (0, -snake_speed)
    if keys[pygame.K_DOWN] and direction != (0, -snake_speed):
        direction = (0, snake_speed)

    # Update the snake position
    x, y = snake[0]
    x += direction[0]
    y += direction[1]

    # Check for collisions with walls
    if x < 0 or x >= screen_width or y < 0 or y >= screen_height:
        running = False

    # Check for collisions with food
    if x < food[0] + food_size and x + snake_size > food[0] and y < food[1] + food_size and y + snake_size > food[1]:
        # Snake ate the food, generate new food
        food = (random.randint(0, screen_width - food_size), random.randint(0, screen_height - food_size))
        snake.append((0, 0))  # Add a new segment to the snake

    # Update the snake segments
    snake = [(x, y)] + snake[:-1]

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw the snake
    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*segment, snake_size, snake_size))

    # Draw the food
    pygame.draw.rect(screen, (255, 0, 0), (*food, food_size, food_size))

    # Flip the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(10)  # Adjust the value to control the snake's speed

# Done! Time to quit.
pygame.quit()
