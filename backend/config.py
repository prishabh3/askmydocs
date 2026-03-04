# Configuration management for the RAG system

class Config:
    def __init__(self):
        # Database configuration
        self.db_uri = "your_database_uri_here"
        self.db_name = "your_database_name_here"

        # API Keys
        self.api_key = "your_api_key_here"

        # Model Configuration
        self.model_name = "your_model_name_here"
        self.model_version = "1.0"
    
    # Add other configuration parameters as required
    def display_config(self):
        print(f"Database URI: {self.db_uri}")
        print(f"Database Name: {self.db_name}")
        print(f"API Key: {self.api_key}")
        print(f"Model Name: {self.model_name}")
        print(f"Model Version: {self.model_version}")

# Example of using the configuration
if __name__ == "__main__":
    config = Config()
    config.display_config()