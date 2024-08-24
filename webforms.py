from wtforms.widgets import TextArea
from wtforms import StringField,SubmitField ,PasswordField,BooleanField,ValidationError
from wtforms.validators import DataRequired , EqualTo, Length
from flask_wtf import FlaskForm    
#creating Login Forms
class LoginForm(FlaskForm):   
     username = StringField('username', validators=[DataRequired()])       
     password = PasswordField('password', validators=[DataRequired()])
     submit = SubmitField("Submit")


#creating Post Forms
class PostForm(FlaskForm):
     title = StringField('Title',validators=[DataRequired()])
     content = StringField('Content',validators=[DataRequired()],widget=TextArea())
     author =StringField('Author')
     slug = StringField('Slug',validators=[DataRequired()])
     submit = SubmitField('Submit')

#creating Forms Class
class UserForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    favourite_color = StringField('Favourite Color')
    username = StringField('Username',validators=[DataRequired()])
    password_hash = PasswordField('Password',validators=[DataRequired(),EqualTo('password_hash2',message='Password Must Match')])
    password_hash2 = PasswordField('Confirm Your Password',validators=[DataRequired()])
    submit = SubmitField("submit")


#creating PasswordForms Class
class PasswordForm(FlaskForm):
    email = StringField('What is your email?', validators=[DataRequired()])
    password_hash = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField("submit")
     


#creating Forms Class
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField("submit")