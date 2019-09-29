from flask import request,Flask,url_for,render_template

app = Flask(__name__)

@app.route('/')
def index():
    url_for('login')

@app.route('/login',method=['POST','GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    return render_template('login.html',error=error)