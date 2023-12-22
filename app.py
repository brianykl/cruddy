from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world"

@app.route('/create')
def create():
    return "create world wahoo"

@app.route('/read')
def read():
    return "read world owaowa"

@app.route('/update')
def update():
    return "update world wooha"

@app.route('/delete')
def delete():
    return "delete world byebye"

if __name__ == '__main__':
    app.run()
    