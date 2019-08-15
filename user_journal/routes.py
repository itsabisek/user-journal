from user_journal import app, bcrypt, db
from user_journal.forms import RegForm, LoginForm
from user_journal.models import User, Journal
from flask import redirect, render_template, url_for, request, flash


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    reg_form = RegForm()
    login_form = LoginForm()

    if reg_form.validate_on_submit():
        username = reg_form.reg_username.data
        if reg_form.validate_input(username):
            name = reg_form.name.data
            password = bcrypt.generate_password_hash(reg_form.reg_password.data).decode('utf-8')
            user = User(name=name, username=username, password=password)
            db.session.add(user)
            db.session.commit()
            flash("User Created Successfully!", 'success')
            return redirect(url_for('register', _method='POST'))

        flash("Username already exists. Please try another username!!", "danger")
        return redirect(url_for('home'))

    # elif login_form.validate_on_submit():
    #     username = reg_form.username.data
    #     password = reg_form.password.data
    #     if login_form.validate_input(username, password):
    #         print("validated")
    #         return redirect(url_for('login'))
    #     return render_template('home.html', reg_form=reg_form, login_form=login_form, reg_error=False, login_error=True)

    return render_template('home.html', reg_form=reg_form, login_form=login_form)


@app.route('/about')
def about():
    return render_template('about.html', title="About")


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', title="Register")


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html', title="Register")


@app.route('/user/<username>')
def user(username):
    pass
