import json
import os

class Config:
    """Class for managing configuration settings."""
    
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.settings = self.load_config()

    def load_config(self):
        """Load configuration settings from a JSON file."""
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                return json.load(file)
        else:
            print(f"Configuration file '{self.config_file}' not found. Using default settings.")
            return {}

    def get(self, key, default=None):
        """Get a configuration value by key."""
        return self.settings.get(key, default)

    def set(self, key, value):
        """Set a configuration value by key."""
        self.settings[key] = value
        self.save_config()

    def save_config(self):
        """Save the current configuration settings to a JSON file."""
        with open(self.config_file, 'w') as file:
            json.dump(self.settings, file, indent=4)
        print("Configuration settings saved.")

# Example usage
if __name__ == "__main__":
    config = Config()
    print("Current settings:", config.settings)
    config.set('api_key', '12345')
    print("Updated settings:", config.settings)
