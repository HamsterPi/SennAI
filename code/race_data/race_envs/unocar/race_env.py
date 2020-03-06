import numpy as np
from race_data.race_environs.unocar.onecar import SennAI2D
import gym
from gym import spaces

class RaceEnv(gym.Env):
    metadata = {'render.modes' : ['human']}
    def __init__(self):
        print("init")
        self.act_space1 = spaces.Discrete(3)
        self.obs_space1 = spaces.Box(np.array([0, 0, 0, 0, 0]), np.array([10, 10, 10, 10, 10]), dtype=np.int)
        self.is_view = True
        self.sennai = SennAI2D(self.is_view)
        self.memory = []

    # Recording various environment details to the memory list
    def recall(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    # Render environment for viewing
    def render(self, mode="human", close=False):
        if self.is_view:
            self.sennai.view()

    # Reset race environment
    def reset(self):
        del self.sennai
        self.sennai = SennAI2D(self.is_view)
        obs1 = self.sennai.observe()
        return obs1

    # Define state of view of the environment
    def save_memory(self, file):
        np.save(file, self.memory)
        print(file + " saved")

    # Save environment to a named file in a npy format
    def set_view(self, flag):
        self.is_view = flag

    # Evaluate several variables
    def step(self, action):
        self.sennai.action(action)
        reward = self.sennai.evaluate()
        done = self.sennai.is_done()
        obs = self.sennai.observe()
        return obs, reward, done, {}
