import numpy as np

class Environment:
    def __init__(self):
        self.state = 0  # Initial state

    def step(self, action):
        """Take an action and return the next state and reward."""
        if action == 0:
            self.state += 1  # Move to the right
            reward = 1
        elif action == 1:
            self.state -= 1  # Move to the left
            reward = -1
        else:
            reward = 0  # No movement

        self.state = max(0, min(self.state, 4))  # Keep state within bounds
        return self.state, reward

if __name__ == "__main__":
    env = Environment()
    next_state, reward = env.step(action=0)
    print("Next State:", next_state, "Reward:", reward)
