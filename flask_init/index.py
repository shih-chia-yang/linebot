from flask import Flask
from sqlalchemy import true
app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return 'hello world'

@app.route('/about/<string:name>')
def about(name):
    return f'{name} practice flask'

if __name__=='__main__':
    app.run()