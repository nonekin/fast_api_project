from dotenv import load_dotenv
import os
load_dotenv()

class Config:
    def __init__(self):
        self.deepseek_API_key = os.getenv('API_KEY')
        self.deepseek_base_url = os.getenv('BASE_URL')

        self.host = os.getenv("HOST")
        self.port = os.getenv("PORT")


config_obj = Config()