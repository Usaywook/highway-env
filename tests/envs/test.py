import gym
import highway_env

env = gym.make("highway-v0")
print(env.action_space)
print(env.observation_space)
done = False
while not done:
    action = env.action_space.sample() # Your agent code here
    obs, reward, done, info = env.step(action)
    env.render()