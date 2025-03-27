from flask import Flask
from config import Config
from database import db, init_db

app = Flask(__name__)
app.config.from_object(Config)

init_db(app)

@app.route('/')
def check():
  return 'Hello world'

with app.app_context():
  db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
