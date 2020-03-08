#requires pygame, pygamemenu and gym to be installed

import sys
import os
from random import randrange
import pygame
import pygameMenu #mention we're using this
import numpy as np
import math
import random
import gym
import race_data
import re
from race_data.race_environs.unocar.onecar import *

#Constants and global variables
leaderboard = []

#red background for the space behind the menu
COLOUR_BACKGROUND = (71,0,0)

#red background for the menu
MENU_BACKGROUND_COLOUR = (228, 55, 36)

#colours to be used later
COLOUR_BLACK = (0, 0, 0)
COLOUR_WHITE = (255, 255, 255)

#toggles
DIFFICULTY = ['EASY']
GENERATION = [0]

#Frames per second of game
FPS = 60.0

#size of gameplay window
WINDOW_SIZE = (640, 480)

#initialize variables used later
surface = None
clock = None
main_menu = None

#play mode environment
env1 = gym.make("SennAI-v1")
#training mode environment
env2 = gym.make("SennAI-v2") 

#buckets for the ai---
NUM_BUCKETS1 = tuple((env1.obs_space1.high + np.ones(env1.obs_space1.shape)).astype(int))
NUM_ACTIONS1 = env1.act_space1.n
STATE_BOUNDS1 = list(zip(env1.obs_space1.low, env1.obs_space1.high))

#buckets for the user
NUM_BUCKETS2 = tuple((env2.obs_space2.high + np.ones(env2.obs_space2.shape)).astype(int))
NUM_ACTIONS2 = env2.act_space2.n
STATE_BOUNDS2 = list(zip(env2.obs_space2.low, env2.obs_space2.high))

#q-tables saved at relevant generations which are loaded as difficulties in play mode, at 5000 will crash and move slowly 
#easy = '5000_aft.npy'
#at 10000 more consistent and faster
#normal = '10000_aft.npy'

easy = '10000_aft.npy'
normal = '15000_aft.npy'

#lowest explore rate will ever drop to
MIN_EXPLORE_RATE = 0.001
#lowest learning rate will ever drop to
MIN_LEARNING_RATE = 0.2

DECAY_FACTOR = np.prod(NUM_BUCKETS1, dtype=float) / 10.0

#so we don't ever run out
NUM_GENS = 9999999
#after this time will run out, exited back to main menu
MAX_T = 2000

q_table1 = np.zeros(NUM_BUCKETS1 + (NUM_ACTIONS1,), dtype=float)
q_table2 = np.zeros(NUM_BUCKETS2 + (NUM_ACTIONS2,), dtype=float)

#functions, accessed through the menu
def change_difficulty(value, difficulty):
    selected, index = value
    print('Selected Difficulty: "{0}" ({1}) at index {2}'.format(selected, difficulty, index))
    DIFFICULTY[0] = difficulty

def change_gentotrainto(value, gentotrainto):
    selected, index = value
    print('Selected Gentotrainto: "{0}" ({1}) at index {2}'.format(selected, gentotrainto, index))
    GENERATION[0] = gentotrainto


def play_function(difficulty, font, test=False):

    #gets the first item in the list 'difficulty'
    difficulty = difficulty[0]

    # Define globals
    global main_menu
    global clock

    if difficulty == 'EASY':
        #loading screen runs while waiting for load_and_simulate
        img = pygame.image.load('loadingscreen.jpg') 
        surface.blit(img,(0,0))
        pygame.display.flip()
        load_and_simulate(easy)

    elif difficulty == 'NORMAL':
        #loading screen runs while waiting for load_and_simulate
        img = pygame.image.load('loadingscreen.jpg') 
        surface.blit(img,(0,0))
        pygame.display.flip()
        load_and_simulate(normal)

    #no need for else as input space is limited to options presented by us to the user



    # Reset main menu and disable
    # main_menu as the menu that will check all your input.
    main_menu.disable()
    main_menu.reset(1)

    while True:

        # Clock tick
        clock.tick(60)

        #to check for the user closing the window
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                #main_menu.enable()
                exit()

        # Pass events to main_menu
        main_menu.mainloop(events)

        # Continue playing
        surface.fill(bg_color)
        surface.blit(f, ((WINDOW_SIZE[0] - f_width) / 2, WINDOW_SIZE[1] / 2))
        pygame.display.flip()

def train_function(difficulty, font, test=False):

    # Define global variables
    global main_menu
    global clock
    print(GENERATION[0])
    simulate(GENERATION[0])


    # Reset main menu and disable
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
    #
    global surface
    surface.fill(COLOUR_BACKGROUND)


def main():
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

    #Setup menus, using pygamemenu

    # Play menu
    play_menu = pygameMenu.Menu(surface,
                                bgfun=main_background,
                                color_selected=COLOUR_WHITE,
                                font=pygameMenu.font.FONT_BEBAS,
                                font_color=COLOUR_BLACK,
                                font_size=30,
                                menu_alpha=100,
                                menu_color=MENU_BACKGROUND_COLOUR,
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
                                   color_selected=COLOUR_WHITE,
                                   font=pygameMenu.font.FONT_BEBAS,
                                   font_color=COLOUR_BLACK,
                                   font_size=30,
                                   menu_alpha=100,
                                   menu_color=MENU_BACKGROUND_COLOUR,
                                   menu_height=int(WINDOW_SIZE[1] * 0.5),
                                   menu_width=int(WINDOW_SIZE[0] * 0.7),
                                   option_shadow=False,
                                   title='Submenu',
                                   window_height=WINDOW_SIZE[1],
                                   window_width=WINDOW_SIZE[0]
                                   )

    #upon click you'll return to the main menu
    play_submenu.add_option('Back', pygameMenu.events.BACK)

    #play menu
    play_menu.add_option('Start',
                         play_function,
                         DIFFICULTY,
                         pygame.font.Font(pygameMenu.font.FONT_FRANCHISE, 30))

    #selects either 5000aft or 10000aft
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
                                     color_selected=COLOUR_WHITE,
                                     font=pygameMenu.font.FONT_BEBAS,
                                     font_color=COLOUR_BLACK,
                                     font_size_title=30,
                                     font_title=pygameMenu.font.FONT_8BIT,
                                     menu_color=MENU_BACKGROUND_COLOUR,
                                     menu_color_title=COLOUR_WHITE,
                                     menu_height=int(WINDOW_SIZE[1] * 0.6),
                                     menu_width=int(WINDOW_SIZE[0] * 0.6),
                                     onclose=pygameMenu.events.DISABLE_CLOSE,
                                     option_shadow=False,
                                     text_color=COLOUR_BLACK,
                                     text_fontsize=20,
                                     title='Leaderboard',
                                     window_height=WINDOW_SIZE[1],
                                     window_width=WINDOW_SIZE[0]
                                     )


    #FIX
    #leaderboard prior was only printing the first five times ever recorded, now wil display the top
    #five times
    i = 0
    #sort last digits of a string
    for l in sorted(leaderboard, key=lambda x: int(re.search(r'\d+$',x).group())):
        if i == 5:
            break
        leaderboard_menu.add_line(l)
        i += 1

    leaderboard_menu.add_line(pygameMenu.locals.TEXT_NEWLINE)
    leaderboard_menu.add_option('Return to menu', pygameMenu.events.BACK)


    train_menu = pygameMenu.Menu(surface,
                                bgfun=main_background,
                                color_selected=COLOUR_WHITE,
                                font=pygameMenu.font.FONT_BEBAS,
                                font_color=COLOUR_BLACK,
                                font_size=30,
                                menu_alpha=100,
                                menu_color=MENU_BACKGROUND_COLOUR,
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
    train_menu.add_selector('Generation to train to',
                           [('0', '0'),
                            ('50','50'),
                            ('100','100'),
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
                                color_selected=COLOUR_WHITE,
                                font=pygameMenu.font.FONT_BEBAS,
                                font_color=COLOUR_BLACK,
                                font_size=30,
                                menu_alpha=100,
                                menu_color=MENU_BACKGROUND_COLOUR,
                                menu_height=int(WINDOW_SIZE[1] * 0.7),
                                menu_width=int(WINDOW_SIZE[0] * 0.7),
                                onclose=pygameMenu.events.DISABLE_CLOSE,
                                option_shadow=False,
                                title='options menu',
                                window_height=WINDOW_SIZE[1],
                                window_width=WINDOW_SIZE[0]
                                )


    # Main menu
    main_menu = pygameMenu.Menu(surface,
                                bgfun=main_background,
                                color_selected=COLOUR_WHITE,
                                font=pygameMenu.font.FONT_BEBAS,
                                font_color=COLOUR_BLACK,
                                font_size=25,
                                menu_alpha=100,
                                menu_color=MENU_BACKGROUND_COLOUR,
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
    main_menu.add_option('Quit', pygameMenu.events.EXIT)

    # Configure main menu
    main_menu.set_fps(FPS)
    #Main loop
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
        main_menu.mainloop(events)

        # Flip surface
        pygame.display.flip()


#used by the training function, to train the AI from scratch
def simulate(generation): 
    #retrieves initial learning rate for the ai (first gen)
    learning_rate = get_learning_rate(0)
    #retrieves initial explore rate for the ai (first gen)
    explore_rate = get_explore_rate(0)
    #discount factor is set to a constant 0.99, The discount factor determines the importance of future rewards. When set to 0, we will only consider immediate rewards and 1 will make algorithm take it in full
    discount_factor = 0.99
    #total reward initialized at 0
    total_reward = 0
    #initialization of reward list
    total_reward_list = []
    #training done set to false
    training_done = False
    #after which explore rate is bumped up
    gen_threshold = 1000
    #initially turn view off
    env1.set_view(False)
    #for each generation of the ai...
    for gen in range(NUM_GENS):
        #turn on view at desired generation
        if gen == int(generation):
            print("view on")
            env1.set_view(True)
        #append current reward to the total reward list
        total_reward_list.append(total_reward)
        #reset the environment
        obv = env1.reset()
        #get the initial state of the program
        start_state = state_to_bucket1(obv)
        #initialize the total reward
        total_reward = 0
        #bump explore rate up to 0.01 after reaching 1000 generations
        if gen >= gen_threshold:
            explore_rate = 0.01
        #for every time step an action is performed by the ai until either the time runs out, the ai completes the track, or crashes
        for t in range(MAX_T):
            #get action
            action = select_action1(start_state, 0.01)

            #step through the enivornment
            obv, reward, done, _ = env1.step(action)

            #get state
            state = state_to_bucket1(obv)

            #recall state
            env1.recall(start_state, action, reward, state, done)

            #update total reward
            total_reward += reward

            # Update the Q based on the result
            top_q = np.amax(q_table1[state])
            q_table1[start_state + (action,)] += learning_rate * (reward + discount_factor * (top_q) - q_table1[start_state + (action,)])

            # Setting up for the next iteration
            start_state = state

            #render for viewing
            env1.render()

            #if crashed, completed track or run out of time
            if done or t >= MAX_T - 1:
                print("Generation %d finished after %i time steps with total reward = %f."
                      % (gen, t, total_reward))
                if total_reward > 0:
                    #append score to leaderboard
                    leaderboard.append("gen: {} time: {}".format(gen + 5000,t))
                break


            #check to see if user is exiting, take them back to main menu
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    main()
                    #change generation back to 0 for training
                    change_gentotrainto(0,0)
        print(state)


        #get new explore rates and learning rates
        explore_rate = get_explore_rate(gen)
        learning_rate = get_learning_rate(gen)

            



#used for loading q-tables saved prior, in the play mode
def load_and_simulate(table):
    #determine what generation we're at
    if table == '15000_aft.npy':
        additional = 15000
    else:
        additional = 10000

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
            start_state1, action1, reward1, state1, done1 = data
            env2.recall1(start_state1, action1, reward1, state1, done1)
            top_q1 = np.amax(q_table1[state1])
            q_table1[start_state1 + (action1,)] += learning_rate * (reward1 + discount_factor * (top_q1) - q_table1[start_state1 + (action1,)])
            if done1 == True:
                i += 1
                learning_rate = get_learning_rate(i)

   # print("Updating q_table is complete")


    #like simulate except with two of everything as there is the car and the AI racing simultaneously
    env2.set_view(True)
    for gen in range(NUM_GENS):
        obv1 = env2.reset1()
        obv2 = env2.reset2()

        start_state1 = state_to_bucket1(obv1)
        start_state2 = state_to_bucket2(obv2)

        total_reward1 = 0
        total_reward2 = 0

        for t in range(MAX_T):
            action1 = select_action1(start_state1, 0.01)
            action2 = select_action2(start_state2, 0.01)

            obv1, reward1, done1, _ = env2.step1(action1)
            obv2, reward2, done2, _ = env2.step2(action2)

            state1 = state_to_bucket1(obv1)
            state2 = state_to_bucket2(obv2)

            env2.recall1(start_state1, action1, reward1, state1, done1)
            env2.recall2(start_state2, action2, reward2, state2, done2)

            start_state1 = state1
            start_state2 = state2

            total_reward1 += reward1
            total_reward2 += reward2

            top_q1 = np.amax(q_table1[state1])
            q_table1[start_state1 + (action1,)] += learning_rate * (reward1 + discount_factor * (top_q1) - q_table1[start_state1 + (action1,)])

            top_q2 = np.amax(q_table2[state2])
            q_table2[start_state2 + (action2,)] += learning_rate * (reward2 + discount_factor * (top_q2) - q_table2[start_state2 + (action2,)])
            

            env2.render()  #differentiate between these two
            if done1: #ai
                print("SennAI Generation %d finished after %i time steps with total reward = %f."
                      % (gen, t, total_reward1))

                if total_reward1 > 0: #completed track

                    #gen + 5000/10000
                    leaderboard.append("SennAI gen {}'s time: {}".format(gen + additional,t))

                    #display a win or lose screen
                    print("you lose")
                    img = pygame.image.load('losescreen.jpg') 
                    surface.blit(img,(0,0))
                    pygame.display.flip()
                else: #crashed
                    print("you win")
                    img = pygame.image.load('winscreen.jpg') 
                    surface.blit(img,(0,0))
                    pygame.display.flip()
                break

            elif done2:
                print("User finished after %i time steps with total reward = %f."
                      % (t, total_reward2))

                if total_reward2 > 0: #completed track
                    leaderboard.append("Your time: {}".format(t))
                    #print sceens if the user wins or loses
                    print("you win")
                    img = pygame.image.load('winscreen.jpg') 
                    surface.blit(img,(0,0))
                    pygame.display.flip()
                else: #crashed
                    print("you lose")
                    img = pygame.image.load('losescreen.jpg') 
                    surface.blit(img,(0,0))
                    pygame.display.flip()
                break

            #max time exceeded
            elif t >= MAX_T - 1:
                print("time out")

            #for the leaderboard
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    #back to main menu
                    main()

        #get new learning and explore rates
        learning_rate = get_learning_rate(i + gen)
        explore_rate = get_explore_rate(i + gen)



#select action for the AI
def select_action1(state, explore_rate):
    if random.random() < explore_rate:
        action1 = env2.act_space1.sample()
    else:
        action1 = int(np.argmax(q_table1[state]))

    return action1

#select action for the user through keypresses
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

#calculate explore rate which varies from the min explore rate to 0.8
def get_explore_rate(t):
    return max(MIN_EXPLORE_RATE, min(0.8, 1.0 - math.log10((t+1)/DECAY_FACTOR)))

#calculate learning rate which varies from min learning rate to 0.8
def get_learning_rate(t):
    return max(MIN_LEARNING_RATE, min(0.8, 1.0 - math.log10((t+1)/DECAY_FACTOR)))

#state tot bucket for the AI
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

#state to bucket for the user
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

#load data function using openAI gym's load function
def load_data(file):
    np_load_old = np.load
    np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)
    data = np.load(file)
    np.load = np_load_old
    return data


#run the main function
if __name__ == '__main__':
    main()
