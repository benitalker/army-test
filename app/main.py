from flask import Flask
from app.routs.email_rout import email_blueprint

app = Flask(__name__)

app.register_blueprint(email_blueprint, url_prefix="/api")

if __name__ == '__main__':
    app.run()
