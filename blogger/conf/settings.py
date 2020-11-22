# settings.py
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), 'service.env')
load_dotenv(dotenv_path)

WEB_APP_PORT = os.environ.get("WEB_APP_PORT")
print("The WEB_APP_PORT Key is : {} ".format(WEB_APP_PORT))
WEB_SOCKET_PORT = os.environ.get("WEB_SOCKET_PORT")
print("The WEB_SOCKET_PORT Key is : {} ".format(WEB_SOCKET_PORT))
SECRET_KEY = os.environ.get("SECRET_KEY")
print("The Secret Key is : {} ".format(SECRET_KEY))
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
print("The DATABASE_PASSWORD Key is : {} ".format(DATABASE_PASSWORD))