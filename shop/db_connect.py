#from flask import Flask, render_template, url_for, flash, redirect
from flask_mysqldb import MySQL
#from forms import RegistrationForm, LoginForm
import pymysql

#app = Flask(__name__)

#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = ''
#app.config['MYSQL_DB'] = 'shop_2'
#app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

#db = pymysql.connect(host="localhost",user="root",passwd="" ) 
db = pymysql.connect(host="localhost",user="root",passwd="",database="shop_2" ) 

#db = MySQL(app)

#@app.route("/index")
#def create_tables():

cur = db.cursor()

# cur.execute("""DROP TABLE IF EXISTS Users, Posts, States, Shops, Cities """) 

#cur.execute(""" CREATE DATABASE shop_2 """)

cur.execute("""CREATE TABLE User(
                                 user_id INT(20) PRIMARY KEY AUTO_INCREMENT,
                                 name CHAR(20) NOT NULL,
                                 email CHAR(20) NOT NULL,
                                 image_file CHAR(20) NOT NULL,
                                  password CHAR(255) NOT NULL
                                 )""")


cur.execute("""CREATE TABLE Post(
                            post_id INT(20) PRIMARY KEY AUTO_INCREMENT,
                            user_id INT(20) NOT NULL,
                            title CHAR(20) NOT NULL,
                            date_posted DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
                            content CHAR(255) NOT NULL,
                            FOREIGN KEY (user_id) REFERENCES User(user_id)
                            )""")



cur.execute("""CREATE TABLE Zip_code(
                            zip_code_id INT(20) PRIMARY KEY AUTO_INCREMENT,
                            state_name CHAR (255) NOT NULL,
                            zip_code_name CHAR(255) NOT NULL,
                            city_name CHAR (255) NOT NULL                           
                            )""")


cur.execute("""CREATE TABLE Shop(
                            shop_id INT(20) PRIMARY KEY AUTO_INCREMENT,
                            zip_code_id INT (20) NOT NULL,
                            name CHAR(255) NOT NULL,
                            description CHAR(255) NOT NULL,
                            address CHAR(255) NOT NULL,
                            phone CHAR(255) NOT NULL,
                            shop_image CHAR(20) NOT NULL,
                            FOREIGN KEY (zip_code_id) REFERENCES Zip_code(zip_code_id)
                            )""")


db.commit()

#return 'Done!'


