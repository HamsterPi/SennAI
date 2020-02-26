import numpy as np
from race_data.race_envs.SennAI_Base import SennAI2D
import gym
from gym import spaces

class RaceEnv(gym.Env):
    metadata = {'render.modes' : ['human']}
    def __init__(self):
        self.memory = []
        self.act_space = spaces.Discrete(3)
        self.obs_space = spaces.Box(np.array([0, 0, 0, 0, 0]), np.array([10, 10, 10, 10, 10]), dtype=np.int)
        self.view_state = True
        self.sennai = SennAI2D(self.view_state)
        print("START GAME")

    # Recording various environment details to the memory list
    def recall(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    # Render environment for viewing
    def render(self, mode="human", close=False):
        if self.view_state:
            self.sennai.view()

    # Reset race environment
    def reset(self):
        del self.sennai
        self.sennai = SennAI2D(self.view_state)
        obs = self.sennai.observe()
        return obs

    # Save environment to a named file in a npy format
    def save_memory(self, file):
        np.save(file, self.memory)
        print(file + " saved")

    # Define state of view of the environment
    def set_view(self, flag):
        self.view_state = flag

    # Evaluate several variables
    def step(self, action):
        self.sennai.action(action)
        reward = self.sennai.evaluate()
        done = self.sennai.is_done()
        obs = self.sennai.observe()
        return obs, reward, done, {}