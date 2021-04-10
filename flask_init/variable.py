from flask import Flask
from flask import render_template
 
app=Flask(__name__)

@app.route('/variables')
def variables():
    student={'學號':'874523','姓名':'小明','性別':'男'}
    fruit=['appale','banana','orange','grape']
    return render_template('variable.html',**locals())


if __name__=='__main__':
    app.run()