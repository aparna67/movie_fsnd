import os
from settings import DB_USER, DB_PASSWORD, DB_NAME

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database

# SQLALCHEMY_DATABASE_URI = "postgresql://postgres:america@localhost:5432/casting_data"
SQLALCHEMY_DATABASE_URI = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost:5432/{DB_NAME}"
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
