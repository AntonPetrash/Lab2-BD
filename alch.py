from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Connecting to the database
DATABASE_URL = 'postgresql://postgres:1@localhost:5432/postgres'
engine = create_engine(DATABASE_URL)

# Creating a base class from which all models will inherit
Base = declarative_base()

# Create a session to interact with the database
Session = sessionmaker()
