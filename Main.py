import pygame
import math
import random
from pygame.math import Vector2


pygame.init()



class FOOD:
    def __init__(self) -> None:
        self.x = 4
        self.y = 5
        self.pos = pygame.math.Vector2(self.x,self.y)

    def draw_food(self):
        food_rect = pygame.Rect(self.pos.x*cell_size,self.pos.y*cell_size,cell_size,cell_size) 
        pygame.draw.rect(screen,(126,123,123),food_rect)
    
class Snake: 
    def __init__(self):
        self.body = [Vector2(1,2),Vector2(1,3)]
        self.direction =1 
    
    def draw_snake(self):
        
        for block in self.body:
            food_rect = pygame.Rect(block.x*cell_size,block.y*cell_size,cell_size,cell_size) 
            pygame.draw.rect(screen,(126,0,123),food_rect)

    def move_snake(self):
        self.body[0]+= Vector2(0,1)
        prev = self.body[0]

        for block in self.body:
            copy = block
            block = prev
            prev = copy

        self.body[1]=block

#make into a grid
cell_size = 20
cell_number = 20 
screen_height = 800
screen_width = 800

# Set up the drawing window
screen = pygame.display.set_mode([cell_size*cell_number,cell_size*cell_number ])
# clock 

clock = pygame.time.Clock()
# Set up random circles
# num_circles = 10
circle_radius_range = (10, 50)
circle = (random.randint(0, screen_width), random.randint(0, screen_height),
            15) 

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

#
food = FOOD()
snake = Snake()
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

    food.draw_food()
    snake.draw_snake()
    snake.move_snake()
    # Update the player position based on arrow key input
    if left and (player_x -player_speed > 0):
        player_x -= player_speed*cell_size
        for i in range(num_circles+1):
            pygame.draw.circle(screen, (100, 0,0 ), (int(player_x+i*player_radius), int(player_y)), player_radius)
    if right and (player_x + player_speed < screen_width):
        player_x += player_speed *cell_size
        for i in range(num_circles+1):
            pygame.draw.circle(screen, (100, 0,0 ), (int(player_x-i*player_radius), int(player_y)), player_radius)
    if up and (player_y - player_speed > 0):
        player_y -= player_speed *cell_size
        for i in range(num_circles+1):
            pygame.draw.circle(screen, (100, 0,0 ), (int(player_x), int(player_y+i*player_radius)), player_radius)
    if down and (player_y -player_speed < screen_height):
        player_y += player_speed*cell_size
        for i in range(num_circles+1):
            pygame.draw.circle(screen, (100, 0,0 ), (int(player_x), int(player_y-i*player_radius)), player_radius)

    
    circle_x, circle_y, circle_radius = circle
    distance = math.sqrt((player_x - circle_x)**2 + (player_y - circle_y)**2)



    # if distance < player_radius + circle_radius and new_circle!= True:
       
    #     #snakes tail length
    #     num_circles += 1
    #     #new circle
    #     new_circle = True
    # elif new_circle!= True:
    #     pygame.draw.rect(screen, (0, 0, 255), (int(circle[0]), int(circle[1])), circle[2])
    # elif new_circle:
    #     circle = (random.randint(0, screen_width), random.randint(0, screen_height),
    #         15) 
    #     new_circle = False

    

    # Draw the player as a red circle

  
    # Flip the display
    pygame.display.flip()

    clock.tick(5)

# Done! Time to quit.
pygame.quit()
