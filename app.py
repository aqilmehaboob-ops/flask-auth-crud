from flask import Flask, render_template, redirect, url_for, request, session, flash, get_flashed_messages
from createaccountform import Form
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = 'secret_key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(200))
    age = db.Column(db.Integer())
    height = db.Column(db.Integer())
    date = db.Column(db.String(50))
    weight = db.Column(db.String(20))

    def __init__(self, name, password, age, height, date, weight):
        self.name = name
        self.password = password
        self.age = age
        self.height = height
        self.date = date
        self.weight = weight
 
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/createaccount", methods = ['GET', 'POST'])
def createaccount():
    form = Form()
    if form.validate_on_submit():
        name = form.name.data
        existing_user = Users.query.filter_by(name=name).first()
        if existing_user:
            flash("name is already taken")
            return redirect(url_for('createaccount'))
        hashed_password = generate_password_hash(form.password.data)
        age = form.age.data
        height = form.height.data
        date = form.date.data
        weight = form.weight.data

        user = Users(name=name, password=hashed_password, age=age, height=height, date=date, weight=weight)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('accountcreated'))

    return render_template('createaccountpage.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        user = Users.query.filter_by(name=name).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('successlogin'))
        else:
            return render_template('loginaccountpage.html')

    return render_template("loginaccountpage.html")

@app.route("/successlogin")
def successlogin():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = Users.query.get(session['user_id'])
 
    return render_template('successloginpage.html', user=user)

@app.route("/update/<int:id>", methods=['POST'])
def update(id):

    if not 'user_id' in session:
        return redirect(url_for('login'))

    user = Users.query.get(session['user_id'])

    if user:

        new_age = request.form.get("updateweight")
        user.weight = new_age

        db.session.commit()

        return redirect(url_for('successlogin'))

@app.route("/deleteaccount/<int:id>", methods=['POST'])
def delete(id):

    if not 'user_id' in session:
        return redirect(url_for('login'))
    
    user = Users.query.get(session['user_id'])
    
    if user:
        db.session.delete(user)
        db.session.commit()
    return redirect(url_for('login'))

@app.route("/accountcreated")   
def accountcreated():
    return render_template('accountcreatedpage.html')

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('home'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)