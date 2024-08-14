from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

#createe  flask instances
app = Flask(__name__)
app.config['SECRET_KEY']="This is Abhi's Secret"

#creating Forms Class
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField("submit")

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