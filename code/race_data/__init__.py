from gym.envs.registration import register

register(
    id='SennAI-v0',
    entry_point='race_data.race_envs:RaceEnv',
    max_episode_steps=2000,
)