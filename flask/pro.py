from flask import Flask
from flask import render_template
app=Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/index')
def hello():
      return render_template('/index.html')


@app.route('/index')
def base():
      return render_template('/base.html')

if __name__=='__main__':
        app.run(debug=True,port=8001)