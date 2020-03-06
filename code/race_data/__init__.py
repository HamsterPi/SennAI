from gym.envs.registration import register

register(
    id='SennAI-v1',
    entry_point='race_data.race_environs.unocar:RaceEnv',
    max_episode_steps=2000,
)

register(
    id='SennAI-v2',
    entry_point='race_data.race_environs.doscars:RaceEnv',
    max_episode_steps=2000,
)
