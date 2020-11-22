# settings.py
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), 'service.env')
load_dotenv(dotenv_path)

SECRET_KEY = os.environ.get("SECRET_KEY")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
WEB_SOCKET_PORT = os.environ.get("WEB_SOCKET_PORT")
print("The Secret Key is : {} ".format(SECRET_KEY))
print("The DATABASE_PASSWORD Key is : {} ".format(DATABASE_PASSWORD))
print("The WEB_SOCKET_PORT Key is : {} ".format(WEB_SOCKET_PORT))