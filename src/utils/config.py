import json

class Config:
    def __init__(self, config_file='config.json'):
        """Load configuration from a JSON file."""
        self.config_file = config_file
        self.config_data = self.load_config()

    def load_config(self):
        """Load configuration data from the JSON file."""
        with open(self.config_file, 'r') as file:
            return json.load(file)

    def get(self, key):
        """Get a configuration value by key."""
        return self.config_data.get(key)

if __name__ == "__main__":
    config = Config()
    print("Database URL:", config.get("database_url"))
