import json
import os

class DataStorage:
    def __init__(self, storage_file='data_storage.json'):
        """Initialize the data storage with a specified file."""
        self.storage_file = storage_file
        if not os.path.exists(self.storage_file):
            with open(self.storage_file, 'w') as file:
                json.dump({}, file)  # Create an empty JSON file

    def save_data(self, key, value):
        """Save data to the storage file."""
        with open(self.storage_file, 'r') as file:
            data = json.load(file)
        data[key] = value
        with open(self.storage_file, 'w') as file:
            json.dump(data, file)

    def load_data(self, key):
        """Load data from the storage file."""
        with open(self.storage_file, 'r') as file:
            data = json.load(file)
        return data.get(key)

if __name__ == "__main__":
    storage = DataStorage()
    storage.save_data("example_key", "example_value")
    value = storage.load_data("example_key")
    print("Loaded Value:", value)
