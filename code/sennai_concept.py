# Priorities:
# - Grass slows
# - Resets if you go outofbounds (IP)
# - Incremental acceleration
# - Car doesn't move unless you hold forwards

# Menu system


import pygame, math, sys, random
from pygame.locals import *

display_width = 841
display_height = 521

# Sets size of screen
screen = pygame.display.set_mode((display_width, display_height))

# Initialises clock
clock = pygame.time.Clock()

# Colours
white = (255,255,255)
black = (0,0,0)

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class VehicleSprite(Entity):
    # Creates a vehicle class
    MAX_FORWARD_SPEED = 5
    MAX_REVERSE_SPEED = 1
    ACCELERATION = 0.05
    TURN_SPEED = 0.000000000001

    def __init__(self, image, position):
        Entity.__init__(self)

        # Creates object instance off
        pygame.sprite.Sprite.__init__(self)

        self.src_image = pygame.image.load(image)

        self.position = 420,70 # Choose start position of the car
        self.speed = 0
        self.direction = 270 # Direction car is facing in (will drive in direction facing)
        self.k_left = 0
        self.k_right = 0
        self.k_down = 0
        self.k_up = 0


    def update(self, time):
        self.speed += (self.k_up + self.k_down)
        if self.speed > self.MAX_FORWARD_SPEED:
            self.speed = self.MAX_FORWARD_SPEED
        if self.speed < -self.MAX_REVERSE_SPEED:
            self.speed = -self.MAX_REVERSE_SPEED

        # Degrees sprite is facing (direction)
        self.direction += (self.k_right + self.k_left)
        x, y = self.position
        rad = self.direction * math.pi / 180
        x += -self.speed*math.sin(rad)
        y += -self.speed*math.cos(rad)
        self.position = (x, y)
        self.image = pygame.transform.rotate(self.src_image, self.direction)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def outofbounds(self, position): # Resets to original state
        if self.position[0] > 840 or self.position[0] < 1 or self.position[1] > 521 or self.position[1] < 1:     
            self.position = 420, 70
            self.direction = 270
            self.speed = 0
            self.k_left = 0
            self.k_right = 0
            self.k_down = 0
            self.k_up = 0

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # Call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

rect = screen.get_rect()

# Background
BackGround = Background('track1.png', [0, 0])

# Car image load
car = VehicleSprite('car.png',rect.midtop)
car_group = pygame.sprite.RenderPlain(car)

# Main game loop

def game_loop():
    run = True
 
    while run:
        # Various Diagnostics for Car Details
        print()
        print("position",car.position)
        print("speed",car.speed)
        print("direction",car.direction) # Needs to reset at 0/360
        print("left",car.k_left)
        print("right",car.k_right)
        print("forwards",car.k_up)
        print("backwards",car.k_down)
        #USER INPUT
        # Sets frame rate
        time = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if not hasattr(event, 'key'):
                continue
            
            down = event.type == KEYDOWN


            if event.key == K_d and car.speed != 0: # no tank turning
                car.k_right = down * -5
                
            elif event.key == K_a and car.speed != 0: #no tank turning
                car.k_left = down * 5
#
            elif event.key == K_w:
                car.k_up = down * 2
#
            elif event.key == K_s:
                car.k_down = down * -2
            
            # Resets to start line if car goes out of bounds, currently doesn't work until a key is pressed after going  out of bounds
            car.outofbounds(car.position)

        # Game background
        screen.fill(white)
        screen.blit(BackGround.image, BackGround.rect)

        # Car render
        car_group.update(time)
        car_group.draw(screen)

        pygame.display.flip()


game_loop()
pygame.quit()
quit()