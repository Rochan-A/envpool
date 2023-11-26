from envpool.registration import register

register(
  task_id="Dummy-v0",
  import_path="envpool.dummy",
  spec_cls="DummyEnvSpec",
  gym_cls="DummyGymEnvPool",
  gymnasium_cls="DummyGymnasiumEnvPool",
  max_episode_steps=200,
  reward_threshold=195.0,
)