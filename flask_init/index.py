from flask import Flask
from flask import request
from sqlalchemy import true
 
app=Flask(__name__)

@app.route('/',methods=['GET'])
@app.route('/index')
def index():
    name=request.args.get('name')
    if bool(name) == True:
        return f'hello {name}'
    else:
        return 'hello world'

@app.route('/about/<string:name>')
def about(name):
    return f'{name} practice flask'

if __name__=='__main__':
    app.run()