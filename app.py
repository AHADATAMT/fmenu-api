from src import app
from flask import render_template

@app.route('/')
def index():
    return ("This is home page")

if __name__ == '__main__':
    app.run(dedug=True)