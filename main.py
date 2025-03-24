from flask import Flask
from config import Config
from database import db, init_db
from models import User, Transaction

app = Flask(__name__)
app.config.from_object(Config)

init_db(app)

with app.app_context():
  db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
