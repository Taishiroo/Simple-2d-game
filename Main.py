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
        self.new_block = False
        #import the images 
        self.head_up =  pygame.image.load('Graphics/head_up.png').convert_alpha()
        self.head_down =  pygame.image.load('Graphics/head_down.png').convert_alpha()
        self.head_right =  pygame.image.load('Graphics/head_right.png').convert_alpha()
        self.head_left =  pygame.image.load('Graphics/head_left.png').convert_alpha()

        self.tail_up =  pygame.image.load('Graphics/tail_up.png').convert_alpha()
        self.tail_down =  pygame.image.load('Graphics/tail_down.png').convert_alpha()
        self.tail_left =  pygame.image.load('Graphics/tail_left.png').convert_alpha()
        self.tail_right =  pygame.image.load('Graphics/tail_right.png').convert_alpha()

        self.body_vertical =  pygame.image.load('Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal =  pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

        self.body_tl =  pygame.image.load('Graphics/body_tl.png').convert_alpha()
        self.body_tr =  pygame.image.load('Graphics/body_tr.png').convert_alpha()
        self.body_bl =  pygame.image.load('Graphics/body_bl.png').convert_alpha()
        self.body_br =  pygame.image.load('Graphics/body_br.png').convert_alpha()
        self.crunch_sound = pygame.mixer.Sound('Sound/crunch.wav')


    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index,block in enumerate(self.body):
            block_rect = pygame.Rect(block.x*cell_size,block.y*cell_size,cell_size,cell_size) 

            if index == 0:
                screen.blit(self.head,block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail,block_rect)

            else:
                previous_block= self.body[index +1]-block
                next_block = self.body[index-1]-block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical,block_rect)
                if previous_block.y== next_block.y:
                    screen.blit(self.body_horizontal,block_rect)
                else:
                    if previous_block.x == -1 and  next_block.y == -1 or previous_block.y==-1 and next_block.x==-1:
                        screen.blit(self.body_tl,block_rect)     
                    elif previous_block.x == 1 and  next_block.y == 1 or previous_block.y==1 and next_block.x==1:
                        screen.blit(self.body_br,block_rect)   
                    elif previous_block.x == 1 and  next_block.y == - 1 or previous_block.y== -1 and next_block.x==1:
                        screen.blit(self.body_tr,block_rect)  
                    elif previous_block.x == -1 and  next_block.y ==  1 or previous_block.y== 1 and next_block.x==-1:
                        screen.blit(self.body_bl,block_rect)  
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        if head_relation == Vector2(-1,0): self.head = self.head_right
        if head_relation == Vector2(0,-1): self.head = self.head_down
        if head_relation == Vector2(0,1): self.head = self.head_up

    def update_tail_graphics(self):
        head_relation = self.body[-1] - self.body[-2]
        if head_relation == Vector2(1,0): self.tail = self.tail_right
        if head_relation == Vector2(-1,0): self.tail = self.tail_left
        if head_relation == Vector2(0,-1): self.tail = self.tail_up
        if head_relation == Vector2(0,1): self.tail = self.tail_down

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] +self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] +self.direction)
            self.body = body_copy[:]
    
    def add_block(self):
        self.new_block = True
    
    def play_crunch_sound(self):
        self.crunch_sound.play()

class MAIN:
    def __init__(self) -> None:
        self.snake = Snake()
        self.food = FOOD()
    
    def update(self):
        self.snake.move_snake()
        self.check_eat()
        self.check_fail()

    def draw_elements(self):
 
        self.draw_grass()
        self.food.draw_food()
        self.snake.draw_snake()
        self.draw_score()
    
    def check_eat(self):
        if self.snake.body[0] == self.food.pos:
           self.snake.add_block()
           self.snake.play_crunch_sound()
           self.food.randomize()
        
        for block in self.snake.body[1:]:
            if block == self.food.pos:
                self.food.randomize()
    def check_fail(self):
        if not 0 <= self.snake.body[0].x  < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
    
    def draw_grass(self):
        grass_color = (167,209,91)
        for row in range(cell_number):
            if row % 2== 0:
                for col in range(cell_number):
                    if col % 2== 0:
                        grass_rect = pygame.Rect(col* cell_size, row*cell_size , cell_size, cell_size   )
                        pygame.draw.rect(screen,grass_color, grass_rect)
            else: 
                for col in range(cell_number):
                    if col % 2!= 0:
                        grass_rect = pygame.Rect(col* cell_size, row*cell_size , cell_size, cell_size   )
                        pygame.draw.rect(screen,grass_color, grass_rect)
    

    def draw_score(self):
        score_text = str(len(self.snake.body)-3)
        score_surface = game_font.render(score_text,True, (56,74,12) )
        score_x = int(cell_size * cell_number - 60 )
        score_y = int(cell_size * cell_number - 40 )
        score_rect = score_surface.get_rect(center = (score_x,score_y   ))
        apple_rect = apple.get_rect(midright = (score_rect.left,score_rect.centery))

        screen.blit(score_surface,score_rect)
        screen.blit(apple,apple_rect)


        
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


game_font = pygame.font.Font(None, 25)

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
    screen.fill((167,200,91))
    # Get the state of all keys
    keys = pygame.key.get_pressed()


    main.draw_elements()
    

    
    circle_x, circle_y, circle_radius = circle
    distance = math.sqrt((player_x - circle_x)**2 + (player_y - circle_y)**2)




    pygame.display.flip()

    clock.tick(60)

# Done! Time to quit.
pygame.quit()
