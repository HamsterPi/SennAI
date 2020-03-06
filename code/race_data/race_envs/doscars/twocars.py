import math
import pygame

class Measure:
    def __init__(self):
        # Screen dimensions
        # New 1660, 1000
        # Old 2000, 1100
        self.screen_width = 1680
        self.screen_height = 1000
        # Checkpoint locations (ALTERED FOR map3)
        self.check_point = ((1475, 185), (1475, 815), (200, 815), (200, 185), (810, 175))
        # ((1440, 210), (1440, 790), (235, 790), (230, 230), (810, 180))
        # most recent: ((1420, 225), (1420, 805), (235, 805), (230, 230), (810, 180))
        #((1420, 225), (1420, 805), (810, 810), (190, 805), (190, 190), (810, 180))

class Car:
    def __init__(self, car1_image, car2_image, track_image, car1_position, car2_position,):
        # CAR SETUP
        # Determines that the car hasn't crashed yet
        self.is_alive1 = True
        self.is_alive2 = True
        # Angle which the car starts in
        self.angle1 = 0
        self.angle2 = 0
        # Position of the car
        self.position1 = car1_position
        self.position2 = car2_position
        # Base car speed
        self.speed1 = 3 #2
        self.speed2 = 0
        # Lidar positionitions
        self.lidar_list1 = []
        self.lidar_list2 = []
        # Lidar lights
        self.lidars_for_draw1 = []
        self.lidars_for_draw2 = []
        # Position of the center of the car
        self.center1 = [self.position1[0] + 50, self.position1[1] + 50]
        self.center2 = [self.position2[0] + 50, self.position2[1] + 50]
        # Loads new image of car and create surface object
        self.surface1 = pygame.image.load(car1_image)
        self.surface2 = pygame.image.load(car2_image)
        # Resize surface new resolution to image (ALTERED FOR map3)
        self.surface1 = pygame.transform.scale(self.surface1, (90, 90))
        self.surface2 = pygame.transform.scale(self.surface2, (90, 90))
        # Surface of car to be drawn onto another surface
        self.rotate_surface1 = self.surface1
        self.rotate_surface2 = self.surface2

        # CHECKPOINT SETUP
        # Current location of the car in respect to the next checkpoint
        self.current_check1 = 0
        self.current_check2 = 0
        # Distance travelled from last checkpoint
        self.prev_distance1 = 0
        self.prev_distance2 = 0
        # Current distance from next checkpoint
        self.cur_distance1 = 0
        self.cur_distance2 = 0
        # Within range of checkpoint?
        self.check_flag1 = False
        self.check_flag2 = False
        # Has a checkpoint been reached
        self.goal1 = False
        self.goal2 = False
        # Distance travelled overall
        self.distance1 = 0
        self.distance2 = 0
        # Time spent travelling
        self.time_spent1 = 0
        self.time_spent2 = 0
        # Incorporate screen specifications

        self.measure = Measure() #one or two

        # Loads new image of track and create surface object
        self.track = pygame.image.load(track_image)
        
        for s in range(-90, 120, 45):
            self.detect_lidar1(s)

        for s in range(-90, 120, 45):
            self.detect_lidar2(s)

        for d in range(-90, 105, 15):
            self.detect_lidar_visuals1(d)

        for d in range(-90, 105, 15):
            self.detect_lidar_visuals2(d)

    # Determine if car has collided with the edge of the track
    def detect_collision1(self):
        self.is_alive1 = True
        for point in self.all_points1:
            if self.track.get_at((int(point[0]), int(point[1]))) == (77, 153, 0, 255):
                self.is_alive1 = False
                break

    def detect_collision2(self):
        self.is_alive2 = True
        for point in self.all_points2:
            if self.track.get_at((int(point[0]), int(point[1]))) == (77, 153, 0, 255):
                self.is_alive2 = False
                #print("collision")
                break

    # Determine lidar positions based on  the edge of the track
    def detect_lidar1(self, degree):
        len = 0
        x_coord = int(self.center1[0] + math.cos(math.radians(360 - (self.angle1 + degree))) * len)
        y_coord = int(self.center1[1] + math.sin(math.radians(360 - (self.angle1 + degree))) * len)

        while not self.track.get_at((x_coord, y_coord)) == (77, 153, 0, 255) and len < 200:
            len = len + 1
            x_coord = int(self.center1[0] + math.cos(math.radians(360 - (self.angle1 + degree))) * len)
            y_coord = int(self.center1[1] + math.sin(math.radians(360 - (self.angle1 + degree))) * len)

        distance = int(math.sqrt(math.pow(x_coord - self.center1[0], 2) + math.pow(y_coord - self.center1[1], 2)))
        self.lidar_list1.append([(x_coord, y_coord), distance])

    def detect_lidar2(self, degree):
        len = 0
        x_coord = int(self.center2[0] + math.cos(math.radians(360 - (self.angle2 + degree))) * len)
        y_coord = int(self.center2[1] + math.sin(math.radians(360 - (self.angle2 + degree))) * len)

        while not self.track.get_at((x_coord, y_coord)) == (77, 153, 0, 255) and len < 200:
            len = len + 1
            x_coord = int(self.center2[0] + math.cos(math.radians(360 - (self.angle2 + degree))) * len)
            y_coord = int(self.center2[1] + math.sin(math.radians(360 - (self.angle2 + degree))) * len)

        distance = int(math.sqrt(math.pow(x_coord - self.center2[0], 2) + math.pow(y_coord - self.center2[1], 2)))
        self.lidar_list2.append([(x_coord, y_coord), distance])

    # Determine lidar positions for visualistion later
    def detect_lidar_visuals1(self, degree):
        len = 0
        x = int(self.center1[0] + math.cos(math.radians(360 - (self.angle1 + degree))) * len)
        y = int(self.center1[1] + math.sin(math.radians(360 - (self.angle1 + degree))) * len)

        # (ALTERED FOR map3)
        while not self.track.get_at((x, y)) == (77, 153, 0, 255) and len < 2000:
            len = len + 1
            x = int(self.center1[0] + math.cos(math.radians(360 - (self.angle1 + degree))) * len)
            y = int(self.center1[1] + math.sin(math.radians(360 - (self.angle1 + degree))) * len)

        dist = int(math.sqrt(math.pow(x - self.center1[0], 2) + math.pow(y - self.center1[1], 2)))
        self.lidars_for_draw1.append([(x, y), dist])

    def detect_lidar_visuals2(self, degree):
        len = 0
        x = int(self.center2[0] + math.cos(math.radians(360 - (self.angle2 + degree))) * len)
        y = int(self.center2[1] + math.sin(math.radians(360 - (self.angle2 + degree))) * len)

        # (ALTERED FOR map3)
        while not self.track.get_at((x, y)) == (77, 153, 0, 255) and len < 2000:
            len = len + 1
            x = int(self.center2[0] + math.cos(math.radians(360 - (self.angle2 + degree))) * len)
            y = int(self.center2[1] + math.sin(math.radians(360 - (self.angle2 + degree))) * len)

        dist = int(math.sqrt(math.pow(x - self.center2[0], 2) + math.pow(y - self.center2[1], 2)))
        self.lidars_for_draw2.append([(x, y), dist])

    # Determine if the car has reached a predefined checkpoint location
    def detect_checkpoint1(self):
        point = self.measure.check_point[self.current_check1]
        self.prev_distance1 = self.cur_distance1
        distance = self.get_distance(point, self.center1)
        if distance < 110: #70
            self.current_check1 += 1
            self.prev_distance1 = 9999
            self.check_flag1 = True
            if self.current_check1 >= len(self.measure.check_point):
                self.current_check1 = 0
                self.goal1 = True
            else:
                self.goal1 = False

        self.cur_distance1 = distance

    def detect_checkpoint2(self):
        point = self.measure.check_point[self.current_check2]
        self.prev_distance2 = self.cur_distance2
        distance = self.get_distance(point, self.center2)
        if distance < 110: #70
            self.current_check2 += 1
            self.prev_distance2 = 9999
            self.check_flag2 = True
            if self.current_check2 >= len(self.measure.check_point):
                self.current_check2 = 0
                self.goal2 = True
            else:
                self.goal2 = False

        self.cur_distance2 = distance



    # Draws one image onto another, in this case the car's positionition and rotation
    def draw1(self, screen):
        screen.blit(self.rotate_surface1, self.position1)

    def draw2(self, screen):
        screen.blit(self.rotate_surface2, self.position2)

        # Illustrates collision points
    def draw_collision1(self, screen):
        for i in range(4):
            x = int(self.all_points1[i][0])
            y = int(self.all_points1[i][1])
            pygame.draw.circle(screen, (255, 255, 255), (x, y), 5)

    def draw_collision2(self, screen):
        for i in range(4):
            x = int(self.all_points2[i][0])
            y = int(self.all_points2[i][1])
            pygame.draw.circle(screen, (255, 255, 255), (x, y), 5)

    # Illustrates lidar lines
    def draw_lidar1(self, screen):
        for r in self.lidars_for_draw1:
            pos, dist = r
            pygame.draw.line(screen, (25, 255, 251), self.center1, pos, 3)
            pygame.draw.circle(screen, (25, 255, 251), pos, 5)

    def draw_lidar2(self, screen):
        for r in self.lidars_for_draw2:
            pos, dist = r
            pygame.draw.line(screen, (25, 255, 251), self.center2, pos, 3)
            pygame.draw.circle(screen, (25, 255, 251), pos, 5)

    # Calculate the distance between two specified points on the track
    def get_distance(self, point1, point2):
        return math.sqrt(math.pow((point1[0] - point2[0]), 2) + math.pow((point1[1] - point2[1]), 2))

    def rotate_center1(self, image, angle):
        self.og_rect = image.get_rect()
        self.rotate_image = pygame.transform.rotate(image, angle)
        self.rotate_rect = self.og_rect.copy()
        self.rotate_rect.center = self.rotate_image.get_rect().center
        self.rotate_image = self.rotate_image.subsurface(self.rotate_rect).copy()
        return self.rotate_image

    def rotate_center2(self, image, angle):
        self.og_rect = image.get_rect()
        self.rotate_image = pygame.transform.rotate(image, angle)
        self.rotate_rect = self.og_rect.copy()
        self.rotate_rect.center = self.rotate_image.get_rect().center
        self.rotate_image = self.rotate_image.subsurface(self.rotate_rect).copy()
        return self.rotate_image

    def update(self):
        #check speed
        self.speed1 -= 0.5 #0.5
        if self.speed1 > 10: #5
            self.speed1 = 10 #5
        if self.speed1 < 1: #.5
            self.speed1 = 1 #.5

        self.speed2 -= 0.5 #0.5
        if self.speed2 > 5: #5
            self.speed2 = 5 #5
        if self.speed2 < 0: #.5
            self.speed2 = 0 #.5

        #check positionition
        self.rotate_surface1 = self.rotate_center1(self.surface1, self.angle1)
        self.rotate_surface2 = self.rotate_center2(self.surface2, self.angle2)

        self.position1[0] += math.cos(math.radians(360 - self.angle1)) * self.speed1
        self.position2[0] += math.cos(math.radians(360 - self.angle2)) * self.speed2

        if self.position1[0] < 20:
            self.position1[0] = 20
        elif self.position1[0] > self.measure.screen_width - 120:
            self.position1[0] = self.measure.screen_width - 120

        if self.position2[0] < 20:
            self.position2[0] = 20
        elif self.position2[0] > self.measure.screen_width - 120:
            self.position2[0] = self.measure.screen_width - 120

        self.distance1 += self.speed1
        self.distance2 += self.speed2

        self.time_spent1 += 1
        self.time_spent2 += 1

        self.position1[1] += math.sin(math.radians(360 - self.angle1)) * self.speed1
        self.position2[1] += math.sin(math.radians(360 - self.angle2)) * self.speed2

        if self.position1[1] < 20:
            self.position1[1] = 20
        elif self.position1[1] > self.measure.screen_height - 120:
            self.position1[1] = self.measure.screen_height - 120

        if self.position2[1] < 20:
            self.position2[1] = 20
        elif self.position2[1] > self.measure.screen_height - 120:
            self.position2[1] = self.measure.screen_height - 120

        # caculate 4 collision points
        self.center1 = [int(self.position1[0]) + 50, int(self.position1[1]) + 50]
        self.center2 = [int(self.position2[0]) + 50, int(self.position2[1]) + 50]

        len = 40
        top_left1 = [self.center1[0] + math.cos(math.radians(360 - (self.angle1 + 30))) * len, self.center1[1] + math.sin(math.radians(360 - (self.angle1 + 30))) * len]
        top_right1 = [self.center1[0] + math.cos(math.radians(360 - (self.angle1 + 150))) * len, self.center1[1] + math.sin(math.radians(360 - (self.angle1 + 150))) * len]
        bottom_left1 = [self.center1[0] + math.cos(math.radians(360 - (self.angle1 + 210))) * len, self.center1[1] + math.sin(math.radians(360 - (self.angle1 + 210))) * len]
        bottom_right1 = [self.center1[0] + math.cos(math.radians(360 - (self.angle1 + 330))) * len, self.center1[1] + math.sin(math.radians(360 - (self.angle1 + 330))) * len]
        
        top_left2 = [self.center2[0] + math.cos(math.radians(360 - (self.angle2 + 30))) * len, self.center2[1] + math.sin(math.radians(360 - (self.angle2 + 30))) * len]
        top_right2 = [self.center2[0] + math.cos(math.radians(360 - (self.angle2 + 150))) * len, self.center2[1] + math.sin(math.radians(360 - (self.angle2 + 150))) * len]
        bottom_left2 = [self.center2[0] + math.cos(math.radians(360 - (self.angle2 + 210))) * len, self.center2[1] + math.sin(math.radians(360 - (self.angle2 + 210))) * len]
        bottom_right2 = [self.center2[0] + math.cos(math.radians(360 - (self.angle2 + 330))) * len, self.center2[1] + math.sin(math.radians(360 - (self.angle2 + 330))) * len]

        self.all_points1 = [top_left1, top_right1, bottom_left1, bottom_right1]
        self.all_points2 = [top_left2, top_right2, bottom_left2, bottom_right2]

class SennAI2D: #imported by things
    def __init__(self, is_render = True):
        pygame.init()
        self.car = Car('car_red.png', 'car_blue.png','track3.png', [810, 140], [810, 85]) #second is user car spawn
        self.clock = pygame.time.Clock()
        self.game_rate = 60
        self.measure = Measure()
        self.render = is_render
        self.screen = pygame.display.set_mode((self.measure.screen_width, self.measure.screen_height))

    def action1(self, action): #actions that the ai chooses, 
        if action == 0:
            self.car.speed1 += 2 #forward
        elif action == 1:
            self.car.angle1 += 5 #left/right
        elif action == 2:
            self.car.angle1 -= 5 #left/right

        self.car.update()

        self.car.detect_collision1()

        self.car.detect_checkpoint1()

        self.car.lidar_list1.clear()

        for s in range(-90, 120, 45):
            self.car.detect_lidar1(s)

    def action2(self, action): #actions that the ai chooses, 
        if action == 0:
            self.car.speed2 += 2 #forward
        if action == 1:
            self.car.angle2 += 5 #left/right
        elif action == 2:
            self.car.angle2 -= 5 #left/right

        self.car.update()

        self.car.detect_collision2()

        self.car.detect_checkpoint2()

        self.car.lidar_list2.clear()

        for s in range(-90, 120, 45):
            self.car.detect_lidar2(s)


    def evaluate1(self):
        reward1 = 0
        if not self.car.is_alive1:
            reward1 = -10000 + self.car.distance1

        elif self.car.goal1:
            reward1 = 10000
        return reward1

    def evaluate2(self):
        reward2 = 0
        if not self.car.is_alive2:
            reward2 = -10000 + self.car.distance2

        elif self.car.goal2:
            reward2 = 10000
        return reward2

    def is_done1(self):
        if not self.car.is_alive1 or self.car.goal1:
            self.car.current_check1 = 0
            self.car.distance1 = 0
            return True
        return False

    def is_done2(self):
        if not self.car.is_alive2 or self.car.goal2:
            self.car.current_check2 = 0
            self.car.distance2 = 0
            return True
        return False

    def observe1(self):
        # Return state
        lidar_list = self.car.lidar_list1
        return_state = [0, 0, 0, 0, 0]
        i = 0
        for lidar in lidar_list:
            return_state[i] = int(lidar[1] / 20)
            i += 1
        return return_state

    def observe2(self):
        # Return state
        lidar_list = self.car.lidar_list2
        return_state = [0, 0, 0, 0, 0]
        i = 0
        for lidar in lidar_list:
            return_state[i] = int(lidar[1] / 20)
            i += 1
        return return_state

    def view(self):
        # Draw game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        self.screen.blit(self.car.track, (0, 0)) # Visualisation
        # Screen blackout for better visulisation of lidar lines and checkpoint circles
        # self.screen.fill((0, 0, 0))

        # (ALTERED FOR TESTING)
        self.car.lidars_for_draw1.clear()
        self.car.lidars_for_draw2.clear()

        for d in range(-90, 105, 15):
            self.car.detect_lidar_visuals1(d)
        for d in range(-90, 105, 15):
            self.car.detect_lidar_visuals2(d)

        #disabled checkpoint visibility for play mode
        #pygame.draw.circle(self.screen, (255, 255, 0), self.measure.check_point[self.car.current_check1], 110, 1) #70
        #pygame.draw.circle(self.screen, (255, 255, 0), self.measure.check_point[self.car.current_check2], 110, 1) #70

        #disabled collision box visibility for play mode
        #self.car.draw_collision1(self.screen)
        #self.car.draw_collision2(self.screen)

        #disabled lidar for play mode
        #self.car.draw_lidar1(self.screen)
        #self.car.draw_lidar2(self.screen)

        self.car.draw1(self.screen)
        self.car.draw2(self.screen)

        pygame.display.flip()
        self.clock.tick(self.game_rate)
