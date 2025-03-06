from flask import Flask


app = Flask(__name__)



@app.route('/')
def check():
  return 'Hello world'







with app.app_context():

 if __name__ == '__main__':
    app.run(debug=True)