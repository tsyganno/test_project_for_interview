from dotenv import load_dotenv
from os import getenv
from datetime import timedelta


load_dotenv()


SECRET_KEY = getenv('SECRET_KEY')
ALGORITHM = getenv('ALGORITHM')
EXPIRATION_TIME = timedelta(seconds=30)

user = getenv('POSTGRESQL_USER')
name_db = getenv('POSTGRESQL_NAME')
password = getenv('POSTGRESQL_PASSWORD')

POSTGRESQL_HOST = getenv('POSTGRESQL_HOST', '127.0.0.1')
POSTGRESQL_PORT = int(getenv('POSTGRESQL_PORT', 5432))
POSTGRESQL_USER = getenv('POSTGRESQL_USER', user)
POSTGRESQL_PASSWORD = getenv('POSTGRESQL_PASSWORD', password)
POSTGRESQL_MAX_CONNECTIONS = int(getenv('POSTGRESQL_MAX_CONNECTIONS', '2'))
POSTGRESQL_DATABASE = getenv('POSTGRESQL_DATABASE', name_db)

POSTGRES_STR_FOR_CONNECT = (
    f'postgresql+asyncpg://'
    f'{POSTGRESQL_USER}:'
    f'{POSTGRESQL_PASSWORD}@'
    f'{POSTGRESQL_HOST}:'
    f'{POSTGRESQL_PORT}/'
    f'{POSTGRESQL_DATABASE}'
)
