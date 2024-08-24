from flask import Flask, render_template, flash,request,redirect,url_for


from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime,date
from flask_migrate import Migrate 
from werkzeug.security import generate_password_hash, check_password_hash  

from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user,current_user
from webforms import LoginForm, PostForm,PasswordForm,NameForm,UserForm

#create  flask instances
app = Flask(__name__)
#secret key for the flask app
app.config['SECRET_KEY']="This is Abhi's Secret"
#database configuration
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

#new Mysql db
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/our_users1'


#JSOn Thing
@app.route('/date')
def get_current_date():
     favorite_car ={
          "brand": "Toyota",
           "brand":"Benz",
           "year": 2020
     }
     return favorite_car
     return {"Date:":date.today()}



#initialize databases
db = SQLAlchemy(app)
#decorting migrate
migrate = Migrate(app, db)
#flask loginn stuff
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
     return Users.query.get(int(user_id))
#create Login Page
@app.route('/login', methods = ["GET","POST"])
def login():
     form = LoginForm()
     if form.validate_on_submit():
          user = Users.query.filter_by(username = form.username.data).first()
          if user:
               #check the hash
               if check_password_hash(user.password_hash, form.password.data):
                    login_user(user)
                    flash('You have been logged in', 'success')
                    return redirect(url_for('dashboard'))
               else:
                    flash('Wrong Password -- TRy Again', 'danger')
          else:
               flash('Account does not exist', 'danger')
     return render_template('login.html', form = form)

#create logout pages
@app.route('/logout', methods = ["GET","POST"])
@login_required
def logout():
     logout_user()
     flash("You have been logged out")
     return redirect(url_for('login'))
#create Dashboard Page
@app.route('/dashboard', methods = ["GET","POST"])
@login_required
def dashboard():
     form = UserForm()
     id = current_user.id
     name_to_update = Users.query.get_or_404(id)
     if request.method == 'POST':
          name_to_update.name = request.form['name']
          name_to_update.email = request.form['email']
          name_to_update.favourite_color = request.form['favourite_color']
          name_to_update.username = request.form['username']
          try:
               db.session.commit()
               flash("user updated Succedegeeuhd")
               return render_template('dashboard.html',form = form, name_to_update = name_to_update)
          except:
               flash("error in updateing")
               return render_template('dashboard.html',form = form, name_to_update = name_to_update, id=id)
     else:
          return render_template('dashboard.html',form = form, name_to_update = name_to_update, id=id)


     return render_template('dashboard.html')

#creating Blog Post Models
class Posts(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String(255))
     content = db.Column(db.Text)
     author = db.Column(db.String(255))
     date_posted = db.Column(db.DateTime, default=datetime.utcnow)
     slug = db.Column(db.String(255))


@app.route("/posts")
def posts():
     #grabes all the posts from db
     posts = Posts.query.order_by(Posts.date_posted)

     return render_template('posts.html',posts = posts)

@app.route('/posts/<int:id>')
def post(id):
     post = Posts.query.get_or_404(id)
     return render_template('post.html',post = post)
@app.route('/post/edit/<int:id>',methods = ['GET','POST'])
@login_required
def edit_posts(id):
     post = Posts.query.get_or_404(id)
     form = PostForm()
     if form.validate_on_submit():
          post.title = form.title.data,
          post.content = form.content.data,
          post.author = form.author.data,
          post.slug = form.slug.data
          #update to db
          db.session.add(post)
          db.session.commit()
          flash('Post has been updated')
          return redirect(url_for('post',id = post.id))
     #another method for filling the forms one is putting values in a form fields other one is this .
     form.title.data = post.title
     form.author.data = post.author
     form.content.data = post.content
     form.slug.data = post.slug   
     return render_template('edit_post.html', form = form)  
@app.route('/post/delete/<int:id>')
def delete_post(id):
     post_to_delete = Posts.query.get_or_404(id)
     try:
          db.session.delete(post_to_delete)
          db.session.commit()
          flash('Post has been deleted')
          # return redirect(url_for('posts')) this is same as below one
          posts = Posts.query.order_by(Posts.date_posted)

          return render_template('posts.html',posts = posts)
     except:
          flash("There was an error")
          posts = Posts.query.order_by(Posts.date_posted)

          return render_template('posts.html',posts = posts)
          

#add possts
@app.route('/add_post', methods=['GET', 'POST'])
def add_post():
     form = PostForm()
     if form.validate_on_submit():
          Post = Posts(title = form.title.data, content = form.content.data, author = form.author.data, slug = form.slug.data)
          form.title.data = ''
          form.content.data = ''
          form.author.data = ''
          form.slug.data = ''
          #add post data to db
          db.session.add(Post)
          db.session.commit()
          flash('Post Added Successfully')
          #redirect to the webpage
     return render_template('add_post.html', form = form)

#creating Models
class Users(db.Model, UserMixin):
     id = db.Column(db.Integer, primary_key=True, unique=True)
     name = db.Column(db.String(200), nullable=False)
     email =db.Column(db.String(200), nullable=False,unique=True)
     favourite_color = db.Column(db.String(200))
     username = db.Column(db.String(20), nullable = False, unique=True )
     date_added = db.Column(db.DateTime, default= datetime.utcnow)
#Doing Some Password stuff
     password_hash = db.Column(db.String(200))
     @property
     def password(self):
          raise AttributeError('password is not a readable atribute')
     @password.setter
     def password(self, password):
          self.password_hash = generate_password_hash(password)
     def verify_password(self,password):
          return check_password_hash(self.password_hash,password)

     #create String
     def __repr__(self):
          return '<Name %r>' % self.name



#updatedb using mysql
@app.route('/update/<int:id>',methods = ['GET','POST'])
@login_required
def update(id):
     form = UserForm()
     name_to_update = Users.query.get_or_404(id)
     if request.method == 'POST':
          name_to_update.name = request.form['name']
          name_to_update.email = request.form['email']
          name_to_update.favourite_color = request.form['favourite_color']
          name_to_update.username = request.form['username']
          try:
               db.session.commit()
               flash("user updated Succedegeeuhd")
               return render_template('update.html',form = form, name_to_update = name_to_update)
          except:
               flash("error in updateing")
               return render_template('update.html',form = form, name_to_update = name_to_update, id=id)
     else:
          return render_template('update.html',form = form, name_to_update = name_to_update, id=id)

#deletedb using mysql
@app.route('/delete/<int:id>',methods = ['GET','POST'])
def delete(id):
     form = UserForm()
     name = None
     user_to_delete = Users.query.get_or_404(id)
     try:
          db.session.delete(user_to_delete)
          db.session.commit()
          flash("DEleted successfully")
          #here we used our_user because to do operation or to visible after deleting.
          our_users = Users.query.order_by(Users.date_added)
          return render_template("add_user.html",
                            form=form,name=name,our_users = our_users)

     except:
          flash("error in deleting")
          our_users = Users.query.order_by(Users.date_added)
          return render_template("add_user.html",
                            form=form,name=name,our_users = our_users)



#creating routes for userdb
@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
     name = None
     form = UserForm()
     if form.validate_on_submit():
          user = Users.query.filter_by(email = form.email.data).first()
          if user is None:
                #because if we not hashed it will be visible as what we erite 
               #  hashed_pw = generate_password_hash(form.password_hash.data, 'sha256')
                hashed_pw = generate_password_hash(form.password_hash.data, method='pbkdf2:sha256')
                user = Users(name = form.name.data, email = form.email.data, username = form.username.data, favourite_color = form.favourite_color.data,password_hash = hashed_pw,)
                db.session.add(user)
                db.session.commit()
          name= form.name.data
          form.name.data = ''
          form.email.data = ''
          form.favourite_color.data = ''
          form.password_hash.data = ''
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
    return render_template("user.html",name=name)
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

#creating A Password Testing Form
@app.route('/test_pw',methods=['GET', 'POST'])
def test_pw():
        #all None is used for checking purose
        email = None
        password = None
        pw_to_check = None
        passed = None
        form = PasswordForm()
        #checking the validation
        if form.validate_on_submit():
            email = form.email.data
            password = form.password_hash.data
            form.email.data = ''
            form.password_hash.data = ''
            #getting the whole user details by their email
            pw_to_check = Users.query.filter_by(email=email).first()
            #checking hashed Passwords
            passed = check_password_hash(pw_to_check.password_hash,password)

            flash('Form Submited Successfully!!!!!')
        return render_template('test_pw.html',email = email, password = password,passed = passed, pw_to_check = pw_to_check, form=form)


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