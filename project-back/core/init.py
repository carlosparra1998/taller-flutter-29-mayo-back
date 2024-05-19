import json
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

config_path = os.path.abspath('config.json')
config = open(config_path)
config = json.load(config)
SQLALCHEMY_DATABASE_URI = f'postgresql://{config["db_user"]}:{config["db_pwd"]}@database/{config["db_db"]}'
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
Base = declarative_base()
Base.metadata.create_all(engine)