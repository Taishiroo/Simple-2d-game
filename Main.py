import pygame
import math
import random
from pygame.math import Vector2


pygame.init()



class FOOD:
    def __init__(self) -> None:
        self.x = random.randint(1,cell_number-1)
        self.y = random.randint(1,cell_number-1)
        self.pos = pygame.math.Vector2(self.x,self.y)

    def draw_food(self):
        food_rect = pygame.Rect(self.pos.x*cell_size,self.pos.y*cell_size,cell_size,cell_size) 
        screen.blit(apple,food_rect)
        # pygame.draw.rect(screen,(126,123,123),food_rect)
    
    def randomize(self):
        self.x = random.randint(1,cell_number-1)
        self.y = random.randint(1,cell_number-1)
        self.pos = pygame.math.Vector2(self.x,self.y)
class Snake: 
    def __init__(self):
        self.body = [Vector2(1,2),Vector2(1,3),Vector2(1,4)]
        self.direction = Vector2(1,0)
    
    def draw_snake(self):
        
        for block in self.body:
            block_rect = pygame.Rect(block.x*cell_size,block.y*cell_size,cell_size,cell_size) 
            pygame.draw.rect(screen,(126,0,123),block_rect)

    def move_snake(self):
  
        body_copy = self.body[:-1]
        body_copy.insert(0,body_copy[0] +self.direction)
        self.body = body_copy[:]

class MAIN:
    def __init__(self) -> None:
        self.snake = Snake()
        self.food = FOOD()
    
    def update(self):
        self.snake.move_snake()
        self.check_eat()
        self.check_fail()

    def draw_elements(self):
        self.food.draw_food()
        self.snake.draw_snake()
    
    def check_eat(self):
        if self.snake.body[0] == self.food.pos:
           self.snake.body.insert(-1,self.snake.body[-1] ) 
           self.food.randomize()
    def check_fail(self):
        if not 0 <= self.snake.body[0].x  < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()




        
#make into a grid
cell_size = 30
cell_number = 20 
screen_height = 800
screen_width = 800

# Set up the drawing window
screen = pygame.display.set_mode([cell_size*cell_number,cell_size*cell_number ])
# clock 
apple = pygame.image.load('apple.png').convert_alpha()
apple = pygame.transform.scale(apple, (30, 30))

clock = pygame.time.Clock()
# Set up random circles
# num_circles = 10
circle_radius_range = (10, 50)
circle = (random.randint(0, screen_width), random.randint(0, screen_height),
            15) 


player_x, player_y = 250, 250




#snakes tail length
num_circles =0
# Run until the user asks to quit

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)


main = MAIN()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SCREEN_UPDATE:
            main.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main.snake.direction.y != 1:
                    main.snake.direction= Vector2(0,-1)
            if event.key == pygame.K_LEFT :
                if main.snake.direction.x != 1:
                    main.snake.direction= Vector2(-1,0)

            if event.key == pygame.K_RIGHT:
               if main.snake.direction.x != -1:
                main.snake.direction= Vector2(1,0)
    
            if event.key == pygame.K_DOWN:
               if main.snake.direction.y != -1:
                main.snake.direction= Vector2(0,1)
     # Fill the background with white
    screen.fill((255, 255, 255))
    # Get the state of all keys
    keys = pygame.key.get_pressed()


    main.draw_elements()
    

    
    circle_x, circle_y, circle_radius = circle
    distance = math.sqrt((player_x - circle_x)**2 + (player_y - circle_y)**2)




    pygame.display.flip()

    clock.tick(60)

# Done! Time to quit.
pygame.quit()
