
from flask import Flask, request, render_template
from structs import User, Message

logged_in = [1]
db_accounts = []
db_tweets = []
info = [""]
'''message, author, likes, dislikes'''

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/login')
def loginPage():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def loginPage_post():
    username = request.form['username']
    password = request.form['password']
    logged_in[0] = username

    return homepage()

@app.route('/register')
def registerPage():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def registerPage_post():
    form = User(request.form)
    db_accounts.append((request.form['username'], request.form['password']))

    return homepage()
    

@app.route('/myprofile')
def profilePage():
    return render_template('myprofile.html')


@app.route('/myprofileChange')
def profilePageChanges():
    return render_template('myprofileChange.html')

@app.route('/myprofileChange', methods = ['POST'])
def profilePageChanges_post():
    info[0] = ((request.form['profilename'], request.form['birthday'], request.form['location']))
    return render_template('myprofile.html', info = info)



@app.route('/tweets')
def tweetsPage():
    return render_template('tweets.html', db_tweets = db_tweets)

@app.route('/tweets', methods = ['POST'])
def tweetsPage_post():
    '''form = Message(request.form)'''
    db_tweets.append((request.form['message'], logged_in[0], 0, 0))
    return render_template('tweets.html', db_tweets = db_tweets)