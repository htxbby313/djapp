from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = https://test.idgt.me/("https://test.idgt.me/")

engine = create_engine(https://test.idgt.me/)
metadata = MetaData()
metadata.create_all(engine)
