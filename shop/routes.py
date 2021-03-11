from flask import render_template, url_for, flash, redirect, request
from shop import app, db
from shop.forms import RegistrationForm, LoginForm


@app.route("/index")
def index():
    return render_template('index.html', title='Index')

@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def home():
    cur = db.connection.cursor() 
    cur.execute("""SELECT * FROM Shop""")
    shops = cur.fetchall()
    return render_template('home.html', shops = shops)


@app.route('/search', methods=['GET', 'POST'])
def search():

    cur = db.connection.cursor()
    if request.method == "POST":
        user_input = request.form["user_input"]  
        cur.execute("SELECT s.name, s.description, s.address, s.phone FROM Shop s WHERE s.address LIKE %s ORDER BY name", ( "%" + user_input + "%", )) 
        results = cur.fetchall()
        return render_template('search_results.html', user_input=user_input, results=results)   
    else:
        return redirect(url_for('home'))


@app.route("/about")
def about():
    return render_template('about.html', title='About')



@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


