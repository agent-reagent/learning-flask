from flask import Flask,request,render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'avanish'
app.config['MYSQL_PASSWORD'] = 'S6V+%6#NeuAQ4=w'
app.config['MYSQL_DB'] = 'twitter_clone'


mysql = MySQL(app=app)
@app.route("/")
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * from tw_user")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template("home.html", data=fetchdata)

# @app.route("/messaging")
# def messages():
#     return render_template("tweets.html")