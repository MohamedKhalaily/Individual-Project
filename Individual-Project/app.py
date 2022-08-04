from urllib import response
from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config= {
  "apiKey": "AIzaSyCGPnCitCNj9d9aRhHqCGE4eiulJW5KFzc",
  "authDomain": "hamodaly-9e7bf.firebaseapp.com",
  "projectId": "hamodaly-9e7bf",
  "storageBucket": "hamodaly-9e7bf.appspot.com",
  "messagingSenderId": "354369135578",
  "appId": "1:354369135578:web:406f790e52196455df96e3",
  "measurementId": "G-XXTRXTWHJE",
  "databaseURL": ""
}
 
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()



app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'



@app.route('/signup', methods=['GET', 'POST'])
def signup():
   error = ""
   if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('home'))
       except:
           error = "Authentication failed"
   return render_template("signup.html")



@app.route('/', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method == 'POST':
       email = request.form['email'] = request.form['email']
       password = request.form['password'] =  request.form['password']
       try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('home'))
       except:
           error = "Authentication failed"
    return render_template("signin.html")


@app.route('/signout')
def signout():
    login_session['user'] = None
    auth.current_user = None
    return redirect(url_for('signin'))


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")
     
#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)