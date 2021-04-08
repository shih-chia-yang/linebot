from flask import Flask
from flask import request
from flask import render_template
from datetime import datetime
 
app=Flask(__name__)

@app.route('/',methods=['GET'])
@app.route('/index')
def index():
    name=request.args.get('name')
    now =datetime.now()
    return render_template('hello.html',**locals())

@app.route('/about/<string:name>')
def about(name):
    return f'{name} practice flask'

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method =="POST":
        username=request.values['username']
        password=request.values['password']
        if username=='stone' and password =='1234':
            return f' welcom {username} login'
        else:
            return 'wrong account or password'
    return """
        <form method='post' action=''>
            <p>account: <input type='text' name='username'/></p>
            <p>password: <input type='text' name='password'/></p>
            <p><button type='submit'>confirm</button></p>
        </form>
    """

if __name__=='__main__':
    app.run()