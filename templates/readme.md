 <!-- to use for loop in render {%%} -->
Here Git is added 
 {{men.0}}  to access the index0
 {{men.0|reverse}} to reverse

  <br><br><br>
    {{men.0}}
    <br>
    {{men.3}}
    <br>
    {{men.3+10}}

     {% for i in men %}
        {% if i == 41 %}
            {{i + 100}}
        {% else %}
            {{ i }}
        {% endif %}
        <br>
    {% endfor %}


    <a class="navbar-brand" href="{{ url_for('power') }}">Flasker</a>
    here power refers to python function .

    ## for form validation we used to nstall flask-wtf then we have to impor it
    here we are going to do perfrm on secret key for protection of forms.

    <form method="post">
        {{form.hidden_tag()}}
        {{form.name.label}}
    <!-- contains label of like placeholder  -->
        {{form.name()}}
        <!-- usde for displaying name field -->

        <br>
        {{form.submit()}}
     </form>
     these are the forms without bootsrap

#importing flsah in flask for creating
#creating sql db for using pip install flask-sqlalchemy

After creating db to check we have to go  to terminAL and say python then do commamnds
> from app import app, db
>>> with app.app_context():
...     db.create_all()

we have to create db with mysql so we have to install 3 connectors  pip install mysql-connector, pip install mysql-connector-python,  pip install mysql-connector-python-rf.

After doing the connection part in create_db.py we will going to run on terminal python create_db.py
After that we have to comment sqllite and then we have to again go to the terminal and type from app imoprt db
and db.create_all() here we have to exit and install pip install pymysql and pip install mysqlclient so thatis why we app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/our_users1' pymysql

pip install cryptography to hash pasword
and we need werkzeug which is inbuilt
then we have to run a flask shell on a power shell,from app import Users, from app import Users
>>> u = Users()
>>> u.password = 'car' 
u.password()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "G:\Flasks\app.py", line 39, in password
    raise AttributeError('password is not a readable atribute')
AttributeError: password is not a readable atribute
Because password cant be redable 
 u.password_hash
'scrypt:32768:8:1$0yY6Gn60o6Nci4C4$6a00b972fb63a5646d674e27c3bbf3392e3e7dfe0af50410dac5ff7a14a0ca577231ccbb211709d99d247871533c98c7d675f89975de20a44c0f945d171c5e0d'
 u.verify_password('car')
True
Beacause we applied additional password field on db so we need to migrate it.terminl
flask db migrate -m 'added pass field'
flask db upgrade

migration is used for making changes internally on the db on this case we created one more colum so it provides error so we used this    pip install Flask-Migrate  from flask_migrate import Migrate  flask db init here migrate will creaatw the directry flask db to check dependenice   flask db migrate -m 'Initial Migration"
here we created migration initially so in the migration folder see the versiion contains initial migration.
so now we push the favotcolor column to db usng migrate 'flask db upgrade'

**Here we are going to create login features so "pip install flask_login" imort from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user,current_user we going to keep inside a user model. we created username then migrated changes.
{% if current_user.is_authenticated %} it can be used to check whether user loedin then they will see this.
we keep here else condition to make the user to understand  {% else %}
        <h2>Must be LOgged in Bro.....</h2>
        <p>You Must be logegd in</p>
        <a href="{{url_for('login')}}">Login Here</a>
    {% endif %}
    look at in add_post.html

Other Method is keeping @login_required under the function. 
We can add any other files to link the files so we can easily copy and paste the code to seperate files in app_bkp.py you can see

this in the update.html 

     {% if name %}
     <h1>Hello {{name|upper}} Update it!!!</h1>
     <br><br><br>
     <table class="table table-hover table-striped table-bordered">
        {% for our_user in our_users%}
        <tr>
            <!-- <td>{{our_user.id}}</td>.<td>{{our_user.name}}</td>--<td>{{our_user.email}}</td> -->
            <td>{{our_user.id}}.{{our_user.name}}--{{our_user.email}}--{{our_user.favourite_color}}</td>
        </tr>
           <br>
      {% endfor %}
     </table>
     {% else %}

** in update.html we used to check whenever we logged in we can access any update user info becuse whenevr we go to url and serch the update/15 or any it will shows the users and to update so to overcome that we use 
ID To Update : {{id}}
     Our current 
     id :here id used for the getting or if user typed any id in the url.
     but currentid determines that the logged id .


#### For user there is many posts but post conatins only single users so we need foreig key
look at the models
