import os
from dotenv import load_dotenv, find_dotenv # type: ignore


# load environment variables from .env file
load_dotenv(find_dotenv())

config = {
    "MYSQL_DATABASE_HOST": os.getenv("MYSQL_DATABASE_HOST"),
    "MYSQL_DATABASE_USER": os.getenv("MYSQL_DATABASE_USER"),
    "MYSQL_DATABASE_PASSWORD": os.getenv("MYSQL_DATABASE_PASSWORD"),
    "MYSQL_DATABASE_DB": os.getenv("MYSQL_DATABASE_DB"),
}

#there is some testing going around here