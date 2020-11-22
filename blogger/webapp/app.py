from flask import Flask
from blogger.conf import settings

app = Flask(__name__)

def main():
    app.run("localhost", settings.WEB_APP_PORT)

if __name__ == "__main__":
    main()