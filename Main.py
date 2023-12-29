import pygame
pygame.init()

screen_height = 250
screen_width = 500

# Set up the drawing window
screen = pygame.display.set_mode([screen_width,screen_height ])

# Set up the player object
player_radius = 25
player_x, player_y = 250, 250
player_speed = 0.1

# Run until the user asks to quit
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the state of all keys
    keys = pygame.key.get_pressed()

    # Update the player position based on arrow key input
    if keys[pygame.K_LEFT] and (player_x -player_speed > 0):
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and (player_x + player_speed < screen_width):
        player_x += player_speed
    if keys[pygame.K_UP] and (player_y - player_speed > 0):
        player_y -= player_speed 
    if keys[pygame.K_DOWN] and (player_y -player_speed < screen_height):
        player_y += player_speed

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw the player as a red circle
    pygame.draw.circle(screen, (255, 0, 0), (int(player_x), int(player_y)), player_radius)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
