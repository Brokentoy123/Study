
#encoding:utf-8
from flask import Flask,redirect,url_for
 
app = Flask(__name__)
 
 
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

 
 
if __name__ == '__main__':
    app.run()