import numpy as np

class RLAgent:
    def __init__(self, actions):
        self.q_table = np.zeros((5, len(actions)))  # Example state space of size 5
        self.actions = actions
        self.learning_rate = 0.1
        self.discount_factor = 0.95

    def choose_action(self, state):
        """Choose an action based on the current state."""
        return np.argmax(self.q_table[state])

    def update_q_value(self, state, action, reward, next_state):
        """Update the Q-value based on the action taken."""
        best_next_action = np.argmax(self.q_table[next_state])
        td_target = reward + self.discount_factor * self.q_table[next_state][best_next_action]
        self.q_table[state][action] += self.learning_rate * (td_target - self.q_table[state][action])

if __name__ == "__main__":
    actions = [0, 1, 2]  # Example actions
    agent = RLAgent(actions)
    # Example of updating Q-values
    agent.update_q_value(state=0, action=1, reward=10, next_state=1)
    print("Q-Table:", agent.q_table)
