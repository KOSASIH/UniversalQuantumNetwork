import random

class ScenarioGenerator:
    def __init__(self):
        self.scenarios = []

    def generate_scenario(self, num_nodes, max_traffic):
        """Generate a random network scenario."""
        scenario = {
            'nodes': num_nodes,
            'traffic': [random.randint(1, max_traffic) for _ in range(num_nodes)]
        }
        self.scenarios.append(scenario)
        return scenario

if __name__ == "__main__":
    generator = ScenarioGenerator()
    scenario = generator.generate_scenario(num_nodes=5, max_traffic=100)
    print("Generated Scenario:", scenario)
