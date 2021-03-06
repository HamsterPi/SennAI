import math
import pygame

class Measure:
    def __init__(self):
        # Screen dimensions
        self.screen_width = 1680
        self.screen_height = 1000

        self.check_point = ((1475, 185), (1475, 815), (200, 815), (200, 185), (810, 175))

        #old
        #self.screen_width = 2000
        #self.screen_height = 1100
        #((1420, 225), (1420, 805), (235, 805), (230, 230), (810, 180))

class Car:
    def __init__(self, car_image, track_image, car_position):
        # CAR SETUP
        # Determines that the car hasn't crashed yet
        self.is_alive = True
        # Angle which the car starts in
        self.angle = 0
        # Position of the car
        self.position = car_position
        # Base car speed, originally 3
        self.speed = 3
        # Lidar positionitions
        self.radar_list = []
        # Position of the center of the car

        self.radars_for_draw = []

        self.center = [self.position[0] + 50, self.position[1] + 50]
        # Loads new image of car and create surface object
        self.surface = pygame.image.load(car_image)
        # Resize surface new resolution to image (ALTERED FOR map3)
        self.surface = pygame.transform.scale(self.surface, (90, 90))
        # Surface of car to be drawn onto another surface
        self.rotate_surface = self.surface

        # CHECKPOINT SETUP
        # Current location of the car in respect to the next checkpoint
        self.current_check = 0
        # Distance travelled from last checkpoint
        self.prev_distance = 0
        # Current distance from next checkpoint
        self.cur_distance = 0
        # Within range of checkpoint?
        self.check_flag = False
        # Has a checkpoint been reached
        self.goal = False
        # Distance travelled overall
        self.distance = 0
        # Time spent travelling
        self.time_spent = 0
        # Incorporate screen specifications
        self.measure = Measure()
        # Loads new image of track and create surface object
        self.track = pygame.image.load(track_image)
        
        # Constantly observe checkpoint locations
        for s in range(-90, 120, 45):
            self.detect_radar(s)

        for d in range(-90, 105, 15):
            self.check_radar_for_draw(d)

    def detect_collision(self):
        self.is_alive = True
        # (ALTERED FOR map3)
        for point in self.all_points:
            if self.track.get_at((int(point[0]), int(point[1]))) == (77, 153, 0, 255):
                self.is_alive = False
                break

    def detect_radar(self, degree):
        len = 0
        x_coord = int(self.center[0] + math.cos(math.radians(360 - (self.angle + degree))) * len)
        y_coord = int(self.center[1] + math.sin(math.radians(360 - (self.angle + degree))) * len)

        # (ALTERED FOR map3)
        while not self.track.get_at((x_coord, y_coord)) == (77, 153, 0, 255) and len < 200:
            len = len + 1
            x_coord = int(self.center[0] + math.cos(math.radians(360 - (self.angle + degree))) * len)
            y_coord = int(self.center[1] + math.sin(math.radians(360 - (self.angle + degree))) * len)

        distance = int(math.sqrt(math.pow(x_coord - self.center[0], 2) + math.pow(y_coord - self.center[1], 2)))
        self.radar_list.append([(x_coord, y_coord), distance])

    def check_radar_for_draw(self, degree):
        len = 0
        x = int(self.center[0] + math.cos(math.radians(360 - (self.angle + degree))) * len)
        y = int(self.center[1] + math.sin(math.radians(360 - (self.angle + degree))) * len)

        # (ALTERED FOR map3)
        while not self.track.get_at((x, y)) == (77, 153, 0, 255) and len < 2000:
            len = len + 1
            x = int(self.center[0] + math.cos(math.radians(360 - (self.angle + degree))) * len)
            y = int(self.center[1] + math.sin(math.radians(360 - (self.angle + degree))) * len)

        dist = int(math.sqrt(math.pow(x - self.center[0], 2) + math.pow(y - self.center[1], 2)))
        self.radars_for_draw.append([(x, y), dist])

    def detect_checkpoint(self):
        point = self.measure.check_point[self.current_check]
        self.prev_distance = self.cur_distance
        distance = self.get_distance(point, self.center)
        if distance < 100:
            self.current_check += 1
            self.prev_distance = 9999
            self.check_flag = True
            if self.current_check >= len(self.measure.check_point):
                self.current_check = 0
                self.goal = True
            else:
                self.goal = False

        self.cur_distance = distance

    # Draws one image onto another, in this case the car's positionition and rotation
    def draw(self, screen):
        screen.blit(self.rotate_surface, self.position)



    # Illustrates lidar lines
    def draw_radar(self, screen):
        for r in self.radars_for_draw:
            pos, dist = r
            pygame.draw.line(screen, (25, 255, 251), self.center, pos, 3)
            pygame.draw.circle(screen, (25, 255, 251), pos, 5)
    
    def get_distance(self, point1, point2):
        return math.sqrt(math.pow((point1[0] - point2[0]), 2) + math.pow((point1[1] - point2[1]), 2))

    def rotate_center(self, image, angle):
        self.og_rect = image.get_rect()
        self.rotate_image = pygame.transform.rotate(image, angle)
        self.rotate_rect = self.og_rect.copy()
        self.rotate_rect.center = self.rotate_image.get_rect().center
        self.rotate_image = self.rotate_image.subsurface(self.rotate_rect).copy()
        return self.rotate_image

    def update(self):
        self.speed -= 0.5 #loss of speed rate
        if self.speed > 10: #upper speed of 5 (originally 10)
            self.speed = 10
        if self.speed < 1: #lower speed of .5 (originally 1)
            self.speed = 1
        #check position
        self.rotate_surface = self.rotate_center(self.surface, self.angle)
        self.position[0] += math.cos(math.radians(360 - self.angle)) * self.speed
        if self.position[0] < 20:
            self.position[0] = 20
        elif self.position[0] > self.measure.screen_width - 120:
            self.position[0] = self.measure.screen_width - 120

        self.distance += self.speed
        self.time_spent += 1
        self.position[1] += math.sin(math.radians(360 - self.angle)) * self.speed
        if self.position[1] < 20:
            self.position[1] = 20
        elif self.position[1] > self.measure.screen_height - 120:
            self.position[1] = self.measure.screen_height - 120

        # caculate 4 collision points
        self.center = [int(self.position[0]) + 50, int(self.position[1]) + 50]
        len = 40
        top_left = [self.center[0] + math.cos(math.radians(360 - (self.angle + 30))) * len, self.center[1] + math.sin(math.radians(360 - (self.angle + 30))) * len]
        top_right = [self.center[0] + math.cos(math.radians(360 - (self.angle + 150))) * len, self.center[1] + math.sin(math.radians(360 - (self.angle + 150))) * len]
        bottom_left = [self.center[0] + math.cos(math.radians(360 - (self.angle + 210))) * len, self.center[1] + math.sin(math.radians(360 - (self.angle + 210))) * len]
        bottom_right = [self.center[0] + math.cos(math.radians(360 - (self.angle + 330))) * len, self.center[1] + math.sin(math.radians(360 - (self.angle + 330))) * len]
        self.all_points = [top_left, top_right, bottom_left, bottom_right]

class SennAI2D: #imported by things
    def __init__(self, is_render = True):
        pygame.init()
        self.car = Car('car_red.png', 'track3.png', [810, 140])
        self.clock = pygame.time.Clock()
        self.game_rate = 60
        self.measure = Measure()
        self.render = is_render
        self.screen = pygame.display.set_mode((self.measure.screen_width, self.measure.screen_height))

    def action(self, action): #actions that the ai chooses, 
        if action == 0:
            self.car.speed += 2
                
        elif action == 1:
            self.car.angle += 5

        elif action == 2:
            self.car.angle -= 5

        self.car.update()

        self.car.detect_collision()

        self.car.detect_checkpoint()

        self.car.radar_list.clear()

        for s in range(-90, 120, 45):
            self.car.detect_radar(s)

    def evaluate(self):
        reward = 0
        if not self.car.is_alive:
            reward = -10000 + self.car.distance

        elif self.car.goal:
            reward = 10000
        return reward

    def is_done(self):
        if not self.car.is_alive or self.car.goal:
            self.car.current_check = 0
            self.car.distance = 0
            return True
        return False

    def observe(self):
        # Return state
        radar_list = self.car.radar_list
        return_state = [0, 0, 0, 0, 0]
        i = 0
        for radar in radar_list:
            return_state[i] = int(radar[1] / 20)
            i += 1
        return return_state

    def view(self):
        # Draw game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        self.screen.blit(self.car.track, (0, 0)) # Visualisation
        #Screen blackout for better visulisation of lidar lines and checkpoint circles
        #self.screen.fill((0, 0, 0))

        # (ALTERED FOR TESTING)
        self.car.radars_for_draw.clear()
        for d in range(-90, 105, 15):
            self.car.check_radar_for_draw(d)
        pygame.draw.circle(self.screen, (255, 255, 0), self.measure.check_point[self.car.current_check], 100, 1)
        
        #self.car.draw_collision(self.screen)
        self.car.draw_radar(self.screen)
        self.car.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(self.game_rate)
