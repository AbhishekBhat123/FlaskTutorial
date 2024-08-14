 <!-- to use for loop in render {%%} -->

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

#importing flsah in flask for cre