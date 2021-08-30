from flask import *
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect
from flask_mysqldb import MySQL
from flask_mail import Mail, Message
import string    
import random


app = Flask(__name__)
app.secret_key = "abc" 

app.config['MYSQL_HOST'] = 'remotemysql.com'
app.config['MYSQL_USER'] = 'HY7fMPc3YD'
app.config['MYSQL_PASSWORD'] = 'CkAOufafJj'
app.config['MYSQL_DB'] = 'HY7fMPc3YD'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'johnsmitcool@gmail.com'
app.config['MAIL_PASSWORD'] = 'tintit2020'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mysql = MySQL(app)
mail = Mail(app)


@app.route("/")
def hello_world():
    return render_template("home.html")


@app.route("/login", methods=['GET', 'POST'])
def callLogin():
    if request.method == 'POST':
        accountNumber = request.form['accountNumber']
        pin = request.form['pin']
    return render_template("login.html")


@app.route("/create", methods=['GET', 'POST'])
def createAccount():
    if request.method == 'POST':
        firstName = request.form['firstName']
        middleName = request.form['middleName']
        lastName = request.form['lastName']
        gender = request.form['gender']
        email = request.form['email']
        address = request.form['address']
        dateOfBirth = request.form['dateOfBirth']
        phone = request.form['phone']
        occupation = request.form['occupation']

        ran = ''.join(random.choices(string.digits, k = 4))    

        cursor = mysql.connection.cursor()
        sql = " INSERT INTO Accounts(First_Name,Middle_Name,Last_Name,Gender,Email,Address,Date_Of_Birth,Phone,Occupation,Pin,Is_OnBoarded) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',{})".format(firstName,middleName,lastName,gender,email,address,dateOfBirth,phone,occupation,ran,0)
        cursor.execute(sql)
        mysql.connection.commit()
        if(cursor.rowcount > 0):
            sql2="SELECT Account_Number,Pin FROM Accounts WHERE Email='{}' ORDER BY Account_Number DESC".format(email)
            cursor.execute(sql2)
            account = cursor.fetchone()  
            msg = Message('Account Successfully Created', sender = 'johnsmitcool@gmail.com', recipients = [email])
            msg.body = "Welcome to the Bank Of TINT\nYour Account has been Successfully Created\nPlease Store Your Credentials for future referances\nAccount Number:{}\nPIN:{}\nChange Your PIN after first Login.".format(account[0],account[1])
            mail.send(msg)
            return render_template("home.html",create=True)
        else:
            return render_template("home.html",create=False)
        cursor.close()
        
    return render_template("createAccount.html")
if __name__ == "__main__":
    app.run(debug=True, port=8000)
