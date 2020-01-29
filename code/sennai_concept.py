#track boundaries

#grass slows

#no tank turning (if still can't turn)

#car doesn't move unless you hold forwards

#menu system


import pygame, math, sys, random
from pygame.locals import *

display_width = 840
display_height = 520

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
        #self.angle = 90
       # self.src_image = pygame.transform.rotate(self.src_image, self.angle)
        self.position = 420,70 #choose start position of the car
        self.speed = 0
        self.direction = 270 #direction car is facing in (will drive in direction facing)
        self.k_left = 0
        self.k_right = 0
        self.k_down = 0
        self.k_up = 0


    def update(self, time):
        # SIMULATION
        self.speed += (self.k_up +self.k_down)
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

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
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
        #diagnostics
        print(car.position)
        print(car.speed)
        #print(car.direction) #direction car is facing in (will drive in direction facing)
        #print(car.left)
        #print(car.right)
        #print(car.up)
        #print(car.down)
        #USER INPUT
        # Sets frame rate
        time = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if not hasattr(event, 'key'):
                continue
            

            down = event.type == KEYDOWN


            if event.key == K_d and car.speed != 0:
                car.k_right = down * -5

            elif event.key == K_a and car.speed != 0:
                car.k_left = down * 5

            elif event.key == K_w:
                car.k_up = down * 2

            elif event.key == K_s:
                car.k_down = down * -2


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