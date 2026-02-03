from dotenv import load_dotenv
import os
load_dotenv()

class Config:
    def __init__(self):
        self.deepseek_API_key = os.getenv('API_KEY')


config = Config()