from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from config import config_obj



class DataBase():
    def __init__(self):
        self.DATABASE_URL = f"postgresql://{config_obj.db_user}:{config_obj.db_password}@{config_obj.db_host}:{config_obj.db_port}/{config_obj.db_name}"
        self.engine = create_engine(self.DATABASE_URL)
        self.session = sessionmaker(self.engine)


database = DataBase()

