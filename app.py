from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


#create  flask instances
app = Flask(__name__)
#secret key for the flask app
app.config['SECRET_KEY']="This is Abhi's Secret"
#database configuration
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

#new Mysql db
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/users"


#initialize databases
db = SQLAlchemy(app)

#creating Models
class Users(db.Model):
     id = db.Column(db.Integer, primary_key=True, unique=True)
     name = db.Column(db.String(200), nullable=False)
     email =db.Column(db.String(200), nullable=False,unique=True)
     date_added = db.Column(db.DateTime, default= datetime.utcnow)

     #create String
     def __repr__(self):
          return '<Name %r>' % self.name
#creating Forms Class
class UserForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    submit = SubmitField("submit")


#creating Forms Class
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField("submit")

#creating routes for userdb
@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
     name = None
     form = UserForm()
     if form.validate_on_submit():
          user = Users.query.filter_by(email = form.email.data).first()
          if user is None:
                user = Users(name = form.name.data, email = form.email.data)
                db.session.add(user)
                db.session.commit()
          name= form.name.data
          form.name.data = ''
          form.email.data = ''
          flash("User Adedd Succefuly") 
     our_users = Users.query.order_by(Users.date_added)
          
     return render_template("add_user.html",
                            form=form,name=name,our_users = our_users)
     

#creating routes
@app.route('/')


def power():
    flash('Hi Welcome to this webpage')
    finame="Abhi"
    stuff = "<strong>Safety</strong> Text"
    men = ["Smart","Intelligebt","killer",41]
    return render_template("index.html",finame=finame, stuff = stuff, men=men)

@app.route('/user/<name>')
def user(name):
    # return "<h1>Hello {}</h1>".format(name)
    return render_template("user.html",name1=name)
    #right name is imortant.

#creating custom error pages

#Invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

#Internal Server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"),500
    
 #creating A Name Form
@app.route('/form',methods=['GET', 'POST'])
def Form_validations():
        name = None
        form = NameForm()
        #checking the validation
        if form.validate_on_submit():
            name = form.name.data
            form.name.data = ''
            flash('Form Submited Successfully!!!!!')
        return render_template('FormName.html',name=name, form=form)   

if __name__ == '__main__':
    app.run(debug=True)