from dotenv import load_dotenv
from os import getenv
from datetime import timedelta


load_dotenv()


SECRET_KEY = getenv('SECRET_KEY')
ALGORITHM = getenv('ALGORITHM')
EXPIRATION_TIME = timedelta(seconds=30)
