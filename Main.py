import pygame
import math
import random


pygame.init()



class FOOD:
    def __init__(self) -> None:
        self.x = 4
        self.y = 5
        self.pos = pygame.math.Vector2(self.x,self.y)





#make into a grid
cell_size = 30
cell_number = 40 
screen_height = 800
screen_width = 800

# Set up the drawing window
screen = pygame.display.set_mode([cell_size*cell_number,cell_size*cell_number ])
# clock 

clock = pygame.time.Clock()
# Set up random circles
# num_circles = 10
# circle_radius_range = (10, 50)
# circle = (random.randint(0, screen_width), random.randint(0, screen_height),
#             15) 

# Set up the player object
player_radius = 25
player_x, player_y = 250, 250
player_speed = 0.1

#true and false statements
up = False
down = False
left = False
right = False

#
new_circle = False

#snakes tail length
num_circles =0
# Run until the user asks to quit
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

     # Fill the background with white
    screen.fill((255, 255, 255))
    # Get the state of all keys
    keys = pygame.key.get_pressed()

    # Update the player position based on arrow key input
    if keys[pygame.K_LEFT] :
        up = False
        down = False
        left = True
        right = False

    if keys[pygame.K_RIGHT]:
        up = False
        down = False
        left = False
        right = True
    if keys[pygame.K_UP]:
        up = True
        down = False
        left = False
        right = False
    if keys[pygame.K_DOWN]:
        up = False
        down = True
        left = False
        right = False


    # Update the player position based on arrow key input
    if left and (player_x -player_speed > 0):
        player_x -= player_speed
        for i in range(num_circles+1):
            pygame.draw.circle(screen, (100, 0,0 ), (int(player_x+i*player_radius), int(player_y)), player_radius)
    if right and (player_x + player_speed < screen_width):
        player_x += player_speed
        for i in range(num_circles+1):
            pygame.draw.circle(screen, (100, 0,0 ), (int(player_x-i*player_radius), int(player_y)), player_radius)
    if up and (player_y - player_speed > 0):
        player_y -= player_speed 
        for i in range(num_circles+1):
            pygame.draw.circle(screen, (100, 0,0 ), (int(player_x), int(player_y+i*player_radius)), player_radius)
    if down and (player_y -player_speed < screen_height):
        player_y += player_speed
        for i in range(num_circles+1):
            pygame.draw.circle(screen, (100, 0,0 ), (int(player_x), int(player_y-i*player_radius)), player_radius)

    
    circle_x, circle_y, circle_radius = circle
    distance = math.sqrt((player_x - circle_x)**2 + (player_y - circle_y)**2)



    if distance < player_radius + circle_radius and new_circle!= True:
       
        #snakes tail length
        num_circles += 1
        #new circle
        new_circle = True
    elif new_circle!= True:
        pygame.draw.circle(screen, (0, 0, 255), (int(circle[0]), int(circle[1])), circle[2])
    elif new_circle:
        circle = (random.randint(0, screen_width), random.randint(0, screen_height),
            15) 
        new_circle = False

    

    # Draw the player as a red circle
    pygame.draw.circle(screen, (255, 0, 0), (int(player_x), int(player_y)), player_radius)
  
    # Flip the display
    pygame.display.flip()

    clock.tick(60)

# Done! Time to quit.
pygame.quit()
