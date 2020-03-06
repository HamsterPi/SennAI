import numpy as np
from race_data.race_environs.doscars.twocars import SennAI2D
import gym
from gym import spaces

class RaceEnv(gym.Env):
    metadata = {'render.modes' : ['human']}
    def __init__(self):
        print("init")
        self.act_space1 = spaces.Discrete(3)
        self.obs_space1 = spaces.Box(np.array([0, 0, 0, 0, 0]), np.array([10, 10, 10, 10, 10]), dtype=np.int)

        self.act_space2 = spaces.Discrete(3)
        self.obs_space2 = spaces.Box(np.array([0, 0, 0, 0, 0]), np.array([10, 10, 10, 10, 10]), dtype=np.int)

        self.is_view = True
        self.sennai = SennAI2D(self.is_view)
        self.memory1 = []
        self.memory2 = []

    # Recording various environment details to the memory list
    def recall1(self, state, action, reward, next_state, done):
        self.memory1.append((state, action, reward, next_state, done))

    def recall2(self, state, action, reward, next_state, done):
        self.memory2.append((state, action, reward, next_state, done))

    # Render environment for viewing
    def render(self, mode="human", close=False):
        if self.is_view:
            self.sennai.view()

    # Reset race environment
    def reset1(self):
        del self.sennai
        self.sennai = SennAI2D(self.is_view)
        obs1 = self.sennai.observe1()
        return obs1

    def reset2(self):
        del self.sennai
        self.sennai = SennAI2D(self.is_view)
        obs2 = self.sennai.observe2()
        return obs2

    # Define state of view of the environment
    def save_memory1(self, file):
        np.save(file, self.memory)
        print(file + " saved")

    def save_memory2(self, file):
        np.save(file, self.memory)
        print(file + " saved")

    # Save environment to a named file in a npy format
    def set_view(self, flag):
        self.is_view = flag

    # Evaluate several variables
    def step1(self, action):
        self.sennai.action1(action)
        reward1 = self.sennai.evaluate1()
        done1 = self.sennai.is_done1()
        obs1 = self.sennai.observe1()
        return obs1, reward1, done1, {}

    def step2(self, action):
        self.sennai.action2(action)
        reward2 = self.sennai.evaluate2()
        done2 = self.sennai.is_done2()
        obs2 = self.sennai.observe2()
        return obs2, reward2, done2, {}
