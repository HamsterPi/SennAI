import sys
import numpy as np
import math
import random
import gym
import race_data

def simulate():
    learning_rate = get_learning_rate(0)
    explore_rate = get_explore_rate(0)
    discount_factor = 0.99
    total_reward = 0
    total_reward_list = []
    training_done = False
    gen_threshold = 1000
    env.set_view(False)
    for gen in range(NUM_GENS):

        total_reward_list.append(total_reward)

        if gen == 10000: #to generation 10000
            env.save_memory('10000_aft.npy') #saves q-table at 10000th generation
            env.set_view(True)

        obv = env.reset()
        start_state = state_to_bucket(obv)
        total_reward = 0

        if gen >= gen_threshold:
            explore_rate = 0.01

        for t in range(MAX_T):
            action = select_action(start_state, explore_rate)
            obv, reward, done, _ = env.step(action)
            state = state_to_bucket(obv)
            env.recall(start_state, action, reward, state, done)
            total_reward += reward

            # Update the Q based on the result
            top_q = np.amax(q_table[state])
            q_table[start_state + (action,)] += learning_rate * (reward + discount_factor * (top_q) - q_table[start_state + (action,)])

            # Setting up for the next iteration
            start_state = state
            env.render()
            if done or t >= MAX_T - 1:
                print("Generation %d finished after %i time steps with total reward = %f."
                      % (gen, t, total_reward))
                break
        # Update parameters
        explore_rate = get_explore_rate(gen)
        learning_rate = get_learning_rate(gen)



def load_and_simulate():
    print("Start loading history")
    history_list = ['5000_aft.npy']

    # load data from history file
    print("Start updating q_table")
    discount_factor = 0.99
    i = 0
    for list in history_list:
        history = load_data(list)
        learning_rate = get_learning_rate(0)
        print(list)
        file_size = len(history)
        print("file size : " + str(file_size))
        for data in history:
            start_state, action, reward, state, done = data
            env.recall(start_state, action, reward, state, done)
            top_q = np.amax(q_table[state])
            q_table[start_state + (action,)] += learning_rate * (reward + discount_factor * (top_q) - q_table[start_state + (action,)])
            if done == True:
                i += 1
                learning_rate = get_learning_rate(i)

    print("Updating q_table is complete")


    # simulate
    env.set_view(True)
    for gen in range(NUM_GENS):
        obv = env.reset()
        start_state = state_to_bucket(obv)
        total_reward = 0

        for t in range(MAX_T):
            action = select_action(start_state, 0.01)
            obv, reward, done, _ = env.step(action)
            state = state_to_bucket(obv)
            env.recall(start_state, action, reward, state, done)
            start_state = state
            total_reward += reward
            top_q = np.amax(q_table[state])
            q_table[start_state + (action,)] += learning_rate * (reward + discount_factor * (top_q) - q_table[start_state + (action,)])
            env.render()
            if done or t >= MAX_T - 1:
                print("Generation %d finished after %i time steps with total reward = %f."
                      % (gen, t, total_reward))
                break

        learning_rate = get_learning_rate(i + gen)



def select_action(state, explore_rate):
    if random.random() < explore_rate:
        action = env.act_space.sample()
    else:
        action = int(np.argmax(q_table[state]))
    return action

def get_explore_rate(t):
    return max(MIN_EXPLORE_RATE, min(0.8, 1.0 - math.log10((t+1)/DECAY_FACTOR)))

def get_learning_rate(t):
    return max(MIN_LEARNING_RATE, min(0.8, 1.0 - math.log10((t+1)/DECAY_FACTOR)))

def state_to_bucket(state):
    bucket_indice = []
    for i in range(len(state)):
        if state[i] <= STATE_BOUNDS[i][0]:
            bucket_index = 0
        elif state[i] >= STATE_BOUNDS[i][1]:
            bucket_index = NUM_BUCKETS[i] - 1
        else:

            # Mapping the state bounds to the bucket array
            bound_width = STATE_BOUNDS[i][1] - STATE_BOUNDS[i][0]
            offset = (NUM_BUCKETS[i]-1)*STATE_BOUNDS[i][0]/bound_width
            scaling = (NUM_BUCKETS[i]-1)/bound_width
            bucket_index = int(round(scaling*state[i] - offset))
        bucket_indice.append(bucket_index)
    return tuple(bucket_indice)

def load_data(file):
    np_load_old = np.load
    np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)
    data = np.load(file)
    np.load = np_load_old
    return data


if __name__ == "__main__":
    env = gym.make("SennAI-v0")
    NUM_BUCKETS = tuple((env.obs_space.high + np.ones(env.obs_space.shape)).astype(int))
    NUM_ACTIONS = env.act_space.n
    STATE_BOUNDS = list(zip(env.obs_space.low, env.obs_space.high))

    MIN_EXPLORE_RATE = 0.001
    MIN_LEARNING_RATE = 0.2
    DECAY_FACTOR = np.prod(NUM_BUCKETS, dtype=float) / 10.0

    NUM_GENS = 9999999
    MAX_T = 2000
    #MAX_T = np.prod(NUM_BUCKETS, dtype=int) * 100

    q_table = np.zeros(NUM_BUCKETS + (NUM_ACTIONS,), dtype=float)
    #simulate()
    load_and_simulate()
