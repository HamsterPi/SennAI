import sys

#sys.path.insert(0, '../../')

import os
from random import randrange
import pygame
import pygameMenu #mention we're using this
import sys
import numpy as np
import math
import random
import gym
import race_data

# -----------------------------------------------------------------------------
# Constants and global variables
# -----------------------------------------------------------------------------

leaderboard = []

COLOR_BACKGROUND = (71,0,0)#(128, 0, 128) #purple
MENU_BACKGROUND_COLOR = (228, 55, 36)

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
DIFFICULTY = ['EASY']
GENERATION = [0]
LIDAR = ['OFF']
CHECKPOINTS = ['OFF'] 
FPS = 60.0

WINDOW_SIZE = (640, 480)

clock = None
main_menu = None
surface = None

env = gym.make("SennAI-v0")

NUM_BUCKETS1 = tuple((env.obs_space1.high + np.ones(env.obs_space1.shape)).astype(int))
NUM_ACTIONS1 = env.act_space1.n
STATE_BOUNDS1 = list(zip(env.obs_space1.low, env.obs_space1.high))

NUM_BUCKETS2 = tuple((env.obs_space2.high + np.ones(env.obs_space2.shape)).astype(int))
NUM_ACTIONS2 = env.act_space2.n
STATE_BOUNDS2 = list(zip(env.obs_space2.low, env.obs_space2.high))

#difficulties
easy = '5000_aft.npy'
normal = '10000_aft.npy'

MIN_EXPLORE_RATE = 0.001
MIN_LEARNING_RATE = 0.2

DECAY_FACTOR1 = np.prod(NUM_BUCKETS1, dtype=float) / 10.0
DECAY_FACTOR2 = np.prod(NUM_BUCKETS2, dtype=float) / 10.0

NUM_GENS = 9999999
MAX_T = 2000
#MAX_T = np.prod(NUM_BUCKETS, dtype=int) * 100

q_table = np.zeros(NUM_BUCKETS1 + (NUM_ACTIONS1,), dtype=float)

# -----------------------------------------------------------------------------
# Methods
# -----------------------------------------------------------------------------
    
def change_difficulty(value, difficulty):
    selected, index = value
    print('Selected Difficulty: "{0}" ({1}) at index {2}'.format(selected, difficulty, index))
    DIFFICULTY[0] = difficulty

def change_gentotrainto(value, gentotrainto):
    selected, index = value
    print('Selected Gentotrainto: "{0}" ({1}) at index {2}'.format(selected, gentotrainto, index))
    GENERATION[0] = gentotrainto

def change_Lidar(value, Lidar):
    selected, index = value
    print('Selected Lidar: "{0}" ({1}) at index {2}'.format(selected, Lidar, index))
    LIDAR[0] = Lidar

def change_checkpoints(value, checkpoints):
    selected, index = value
    print('Selected Checkpoints: "{0}" ({1}) at index {2}'.format(selected, checkpoints, index))
    CHECKPOINTS[0] = checkpoints

def play_function(difficulty, font, test=False):

    assert isinstance(difficulty, (tuple, list))
    difficulty = difficulty[0]
    assert isinstance(difficulty, str)

    # Define globals
    global main_menu
    global clock

    if difficulty == 'EASY':
        #loading screen runs while waiting for load_and_simulate
        load_and_simulate(easy)

    elif difficulty == 'NORMAL':
        load_and_simulate(normal)

        #f = font.render('Playing as a champion (hard)', 1, COLOR_WHITE)
    else:
        raise Exception('Unknown difficulty {0}'.format(difficulty))

    # Draw random color and text
    #bg_color = random_color() #follow accessibility colour contrasts
    #f_width = f.get_size()[0]

    # Reset main menu and disable
    # You also can set another menu, like a 'pause menu', or just use the same
    # main_menu as the menu that will check all your input.
    main_menu.disable()
    main_menu.reset(1)

    while True:

        # Clock tick
        clock.tick(60)

        # Application events
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                #main_menu.enable()
                exit()
            #elif e.type == pygame.KEYDOWN:
             #   if e.key == pygame.K_ESCAPE and main_menu.is_disabled():
              #      main_menu.enable()

        # Pass events to main_menu
        main_menu.mainloop(events)

        # Continue playing
        surface.fill(bg_color)
        surface.blit(f, ((WINDOW_SIZE[0] - f_width) / 2, WINDOW_SIZE[1] / 2))
        pygame.display.flip()

def train_function(difficulty, font, test=False):
    #assert isinstance(difficulty, (tuple, list))
    #difficulty = difficulty[0]
    #assert isinstance(difficulty, str)

    # Define globals
    global main_menu
    global clock
    print(GENERATION[0])
    simulate(GENERATION[0])

    # Draw random color and text
    #bg_color = random_color() #follow accessibility colour contrasts
    #f_width = f.get_size()[0]

    # Reset main menu and disable
    # You also can set another menu, like a 'pause menu', or just use the same
    # main_menu as the menu that will check all your input.
    main_menu.disable()
    main_menu.reset(1)

    while True:

        # Clock tick
        clock.tick(60)

        # Application events
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                #main_menu.enable()
                exit()
            #elif e.type == pygame.KEYDOWN:
             #   if e.key == pygame.K_ESCAPE and main_menu.is_disabled():
              #      main_menu.enable()

        # Pass events to main_menu
        main_menu.mainloop(events)

        # Continue playing
        #surface.fill(bg_color)
        #surface.blit(f, ((WINDOW_SIZE[0] - f_width) / 2, WINDOW_SIZE[1] / 2))
        pygame.display.flip()


def main_background():
    """
    Function used by menus, draw on background while menu is active.

    :return: None
    """
    global surface
    surface.fill(COLOR_BACKGROUND)


def main(test=False):
    """
    Main program.

    :param test: Indicate function is being tested
    :type test: bool
    :return: None
    """

    # -------------------------------------------------------------------------
    # Globals
    # -------------------------------------------------------------------------
    global clock
    global main_menu
    global surface

    # -------------------------------------------------------------------------
    # Init pygame
    # -------------------------------------------------------------------------
    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    # Create pygame screen and objects
    surface = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('SennAI')
    clock = pygame.time.Clock()

    # -------------------------------------------------------------------------
    # Create menus
    # -------------------------------------------------------------------------

    # Play menu
    play_menu = pygameMenu.Menu(surface,
                                bgfun=main_background,
                                color_selected=COLOR_WHITE,
                                font=pygameMenu.font.FONT_BEBAS,
                                font_color=COLOR_BLACK,
                                font_size=30,
                                menu_alpha=100,
                                menu_color=MENU_BACKGROUND_COLOR,
                                menu_height=int(WINDOW_SIZE[1] * 0.7),
                                menu_width=int(WINDOW_SIZE[0] * 0.7),
                                onclose=pygameMenu.events.DISABLE_CLOSE,
                                option_shadow=False,
                                title='Play menu',
                                window_height=WINDOW_SIZE[1],
                                window_width=WINDOW_SIZE[0]
                                )

    play_submenu = pygameMenu.Menu(surface,
                                   bgfun=main_background,
                                   color_selected=COLOR_WHITE,
                                   font=pygameMenu.font.FONT_BEBAS,
                                   font_color=COLOR_BLACK,
                                   font_size=30,
                                   menu_alpha=100,
                                   menu_color=MENU_BACKGROUND_COLOR,
                                   menu_height=int(WINDOW_SIZE[1] * 0.5),
                                   menu_width=int(WINDOW_SIZE[0] * 0.7),
                                   option_shadow=False,
                                   title='Submenu',
                                   window_height=WINDOW_SIZE[1],
                                   window_width=WINDOW_SIZE[0]
                                   )

    play_submenu.add_option('Back', pygameMenu.events.BACK)

    #play menu
    play_menu.add_option('Start',  # When pressing return -> play(DIFFICULTY[0], font)
                         play_function,
                         DIFFICULTY,
                         pygame.font.Font(pygameMenu.font.FONT_FRANCHISE, 30))

    play_menu.add_selector('Select difficulty',
                           [('1 - Easy', 'EASY'),
                            ('2 - Normal', 'NORMAL')],
                           onchange=change_difficulty,
                           selector_id='select_difficulty')
    #play_menu.add_option('Another menu', play_submenu)
    play_menu.add_option('Return to main menu', pygameMenu.events.BACK)

    # Leaderboard menu
    leaderboard_menu = pygameMenu.TextMenu(surface,
                                     bgfun=main_background,
                                     color_selected=COLOR_WHITE,
                                     font=pygameMenu.font.FONT_BEBAS,
                                     font_color=COLOR_BLACK,
                                     font_size_title=30,
                                     font_title=pygameMenu.font.FONT_8BIT,
                                     menu_color=MENU_BACKGROUND_COLOR,
                                     menu_color_title=COLOR_WHITE,
                                     menu_height=int(WINDOW_SIZE[1] * 0.6),
                                     menu_width=int(WINDOW_SIZE[0] * 0.6),
                                     onclose=pygameMenu.events.DISABLE_CLOSE,
                                     option_shadow=False,
                                     text_color=COLOR_BLACK,
                                     text_fontsize=20,
                                     title='Leaderboard',
                                     window_height=WINDOW_SIZE[1],
                                     window_width=WINDOW_SIZE[0]
                                     )
    for m in leaderboard: #change
        leaderboard_menu.add_line(m)
    leaderboard_menu.add_line(pygameMenu.locals.TEXT_NEWLINE)
    leaderboard_menu.add_option('Return to menu', pygameMenu.events.BACK)


    train_menu = pygameMenu.Menu(surface,
                                bgfun=main_background,
                                color_selected=COLOR_WHITE,
                                font=pygameMenu.font.FONT_BEBAS,
                                font_color=COLOR_BLACK,
                                font_size=30,
                                menu_alpha=100,
                                menu_color=MENU_BACKGROUND_COLOR,
                                menu_height=int(WINDOW_SIZE[1] * 0.7),
                                menu_width=int(WINDOW_SIZE[0] * 0.7),
                                onclose=pygameMenu.events.DISABLE_CLOSE,
                                option_shadow=False,
                                title='training menu',
                                window_height=WINDOW_SIZE[1],
                                window_width=WINDOW_SIZE[0]
                                )


    #descriptive text needs to be included at top
    train_menu.add_option('Start',  # When pressing return -> play(DIFFICULTY[0], font)
                         train_function,
                         DIFFICULTY,
                         pygame.font.Font(pygameMenu.font.FONT_FRANCHISE, 30))

    #replace with number field
    train_menu.add_selector('Generation to train to', #replace with input()
                           [('0', '0'),
                            ('1000','1000'),
                            ('2000', '2000'),
                            ('3000','3000'),
                            ('4000', '4000'),
                            ('5000','5000'),
                            ('6000', '6000'),
                            ('7000','7000'),
                            ('8000','8000'),
                            ('9000','9000'),
                            ('10000', '10000'),
                            ('11000','11000'),
                            ('12000', '12000'),
                            ('13000','13000'),
                            ('14000', '14000'),
                            ('15000','15000'),
                            ('16000','16000'),
                            ('17000','17000'),
                            ('18000','18000'),
                            ('19000','19000'),
                            ('20000','20000'),
                            ],
                           onchange=change_gentotrainto,
                           selector_id='select_gentotrainto')

    train_menu.add_option('Return to main menu', pygameMenu.events.BACK)

    options_menu = pygameMenu.Menu(surface,
                                bgfun=main_background,
                                color_selected=COLOR_WHITE,
                                font=pygameMenu.font.FONT_BEBAS,
                                font_color=COLOR_BLACK,
                                font_size=30,
                                menu_alpha=100,
                                menu_color=MENU_BACKGROUND_COLOR,
                                menu_height=int(WINDOW_SIZE[1] * 0.7),
                                menu_width=int(WINDOW_SIZE[0] * 0.7),
                                onclose=pygameMenu.events.DISABLE_CLOSE,
                                option_shadow=False,
                                title='options menu',
                                window_height=WINDOW_SIZE[1],
                                window_width=WINDOW_SIZE[0]
                                )


    options_menu.add_selector('Checkpoints',
                           [('OFF', 'OFF'),('ON', 'ON')],
                           onchange=change_difficulty,
                           selector_id='checkpoints_onoff')

    options_menu.add_selector('Lidar',
                            [('OFF', 'OFF'),('ON', 'ON')],
                           onchange=change_difficulty,
                           selector_id='Lidar_onoff')


    options_menu.add_option('Return to main menu', pygameMenu.events.BACK)

    # Main menu
    main_menu = pygameMenu.Menu(surface,
                                bgfun=main_background,
                                color_selected=COLOR_WHITE,
                                font=pygameMenu.font.FONT_BEBAS,
                                font_color=COLOR_BLACK,
                                font_size=25,
                                menu_alpha=100,
                                menu_color=MENU_BACKGROUND_COLOR,
                                menu_height=int(WINDOW_SIZE[1] * 0.6),
                                menu_width=int(WINDOW_SIZE[0] * 0.6),
                                onclose=pygameMenu.events.DISABLE_CLOSE,
                                option_shadow=False,
                                title='SennAI',
                                window_height=WINDOW_SIZE[1],
                                window_width=WINDOW_SIZE[0]
                                )

    #options submenus as seen from main menu
    main_menu.add_option('Play', play_menu)
    main_menu.add_option('Train', train_menu)
    main_menu.add_option('Leaderboard', leaderboard_menu)
    main_menu.add_option('Options', options_menu)
    main_menu.add_option('Quit', pygameMenu.events.EXIT)

    # Configure main menu
    main_menu.set_fps(FPS)

    # -------------------------------------------------------------------------
    # Main loop
    # -------------------------------------------------------------------------
    while True:

        # Tick
        clock.tick(FPS)

        # Paint background
        main_background()

        # Application events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        # Main menu
        main_menu.mainloop(events, disable_loop=test)

        # Flip surface
        pygame.display.flip()

        # At first loop returns
        #if test:
         #   break

def simulate(generation):
    learning_rate = get_learning_rate(0)
    explore_rate = get_explore_rate(0)
    discount_factor = 0.99
    total_reward = 0
    total_reward_list = []
    training_done = False
    gen_threshold = 1000

    if generation == 0:
        env.set_view(True)
    else:
        env.set_view(False)
    for gen in range(NUM_GENS):

        total_reward_list.append(total_reward)

        if gen == int(generation) and int(generation) > 0: #to generation 10000
            env.save_memory('{}_aft.npy'.format(generation)) #saves user trained generation at whatever gen
            env.set_view(True)

        obv1 = env.reset1()
        start_state = state_to_bucket1(obv1)
        total_reward = 0

        #why this
        if gen >= gen_threshold:
            explore_rate = 0.01

        for t in range(MAX_T):
            action1 = select_action1(start_state, 0.01)
            action2 = select_action2(start_state, 0.01)
            obv1, reward1, done1, _ = env.step1(action1)
            obv2, reward2, done2, _ = env.step2(action2)
            state = state_to_bucket1(obv1)
            env.recall1(start_state, action1, reward1, state, done1)
            total_reward += reward1

            # Update the Q based on the result
            top_q = np.amax(q_table[state])
            q_table[start_state + (action1,)] += learning_rate * (reward1 + discount_factor * (top_q) - q_table[start_state + (action1,)])

            # Setting up for the next iteration
            start_state = state
            env.render()
            if done1 or t >= MAX_T - 1:
                print("Generation %d finished after %i time steps with total reward = %f."
                      % (gen, t, total_reward))
                if total_reward > -1:
                    #+ 5000 as we start from 5000 rather than 0
                    leaderboard.append("gen: {} time: {}".format(gen + 5000,t))
                break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    main()


        explore_rate = get_explore_rate(gen)
        learning_rate = get_learning_rate(gen)
    """ 
            key_press = pygame.key.get_pressed()
        
            if key_press[pygame.K_RIGHT]:
                action = 2
                return action
                
            elif key_press[pygame.K_LEFT]:
                action = 1
                return action
        
            elif key_press[pygame.K_UP]:
                action = 0
                return action
        
            else:
                pass
        
    """

            



def load_and_simulate(table):

    #loading screen

    #print("Start loading history")
    history_list = [table]

    # load data from history file
    #print("Start updating q_table")
    discount_factor = 0.99
    i = 0
    for list in history_list:
        history = load_data(list)
        learning_rate = get_learning_rate(0)
        #print(list)
        file_size = len(history)
        #print("file size : " + str(file_size))
        for data in history:
            start_state, action, reward, state, done = data
            env.recall1(start_state, action, reward, state, done)
            top_q = np.amax(q_table[state])
            q_table[start_state + (action,)] += learning_rate * (reward + discount_factor * (top_q) - q_table[start_state + (action,)])
            if done == True:
                i += 1
                learning_rate = get_learning_rate(i)

   # print("Updating q_table is complete")


    # simulate
    env.set_view(True)
    for gen in range(NUM_GENS):
        obv1 = env.reset1()
        obv2 = env.reset2()
        start_state1 = state_to_bucket1(obv1)
        start_state2 = state_to_bucket2(obv2)
        total_reward = 0

        for t in range(MAX_T):
            action1 = select_action1(start_state, 0.01)
            action2 = select_action2(start_state, 0.01)
            obv1, reward, done, _ = env.step1(action)
            obv2, reward, done, _ = env.step2(action2)
            state = state_to_bucket(obv1)
            env.recall1(start_state, action, reward, state, done)
            start_state = state
            total_reward += reward
            top_q = np.amax(q_table[state])
            q_table[start_state + (action,)] += learning_rate * (reward + discount_factor * (top_q) - q_table[start_state + (action,)])
            env.render()
            if done or t >= MAX_T - 1:
                print("Generation %d finished after %i time steps with total reward = %f."
                      % (gen, t, total_reward))
                if total_reward > -1:
                    #+ 5000 as we start from 5000 rather than 0
                    leaderboard.append("gen: {} time: {}".format(gen + 5000,t))
                    #resort leaderboard to show fastest times at top

                break

            #for the leaderboard
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    #back to main menu
                    main()

                #elif e.type == pygame.KEYDOWN:
                 #   if e.key == pygame.K_ESCAPE and main_menu.is_disabled():
                  #      main_menu.enable()

                    # Quit this function, then skip to loop of main-menu on line 317
                    #return
        learning_rate = get_learning_rate(i + gen)
        explore_rate = get_explore_rate(i + gen)



def select_action1(state, explore_rate):
    if random.random() < explore_rate:
        action1 = env.act_space1.sample()
    else:
        action1 = int(np.argmax(q_table[state]))

    return action1

def select_action2(state, explore_rate):
    key_press = pygame.key.get_pressed()
        
    if key_press[pygame.K_RIGHT]:
        action2 = 2
        return action2
                
    elif key_press[pygame.K_LEFT]:
        action2 = 1
        return action2

    elif key_press[pygame.K_UP]:
        action2 = 0
        return action2

    else:
        pass

def get_explore_rate(t):
    return max(MIN_EXPLORE_RATE, min(0.8, 1.0 - math.log10((t+1)/DECAY_FACTOR1)))

def get_learning_rate(t):
    return max(MIN_LEARNING_RATE, min(0.8, 1.0 - math.log10((t+1)/DECAY_FACTOR1)))

def state_to_bucket1(state):
    bucket_indice = []
    for i in range(len(state)):
        if state[i] <= STATE_BOUNDS1[i][0]:
            bucket_index = 0
        elif state[i] >= STATE_BOUNDS1[i][1]:
            bucket_index = NUM_BUCKETS1[i] - 1
        else:

            # Mapping the state bounds to the bucket array
            bound_width = STATE_BOUNDS1[i][1] - STATE_BOUNDS1[i][0]
            offset = (NUM_BUCKETS1[i]-1)*STATE_BOUNDS1[i][0]/bound_width
            scaling = (NUM_BUCKETS1[i]-1)/bound_width
            bucket_index = int(round(scaling*state[i] - offset))
        bucket_indice.append(bucket_index)
    return tuple(bucket_indice)

def state_to_bucket2(state):
    bucket_indice = []
    for i in range(len(state)):
        if state[i] <= STATE_BOUNDS2[i][0]:
            bucket_index = 0
        elif state[i] >= STATE_BOUNDS2[i][1]:
            bucket_index = NUM_BUCKETS2[i] - 1
        else:

            # Mapping the state bounds to the bucket array
            bound_width = STATE_BOUNDS2[i][1] - STATE_BOUNDS2[i][0]
            offset = (NUM_BUCKETS2[i]-1)*STATE_BOUNDS2[i][0]/bound_width
            scaling = (NUM_BUCKETS2[i]-1)/bound_width
            bucket_index = int(round(scaling*state[i] - offset))
        bucket_indice.append(bucket_index)
    return tuple(bucket_indice)

def load_data(file):
    np_load_old = np.load
    np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)
    data = np.load(file)
    np.load = np_load_old
    return data


if __name__ == '__main__':
    main()