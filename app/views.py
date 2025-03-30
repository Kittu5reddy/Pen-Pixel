from flask import Blueprint, render_template, redirect, request, url_for, session
from .models import User, SignupForm, LoginForm, db
from flask_bcrypt import Bcrypt
from flask_login import login_required, LoginManager, login_user, logout_user, current_user















login_manager = LoginManager()
main = Blueprint('main', __name__, url_prefix='/')
bcrypt = Bcrypt()















#auth
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first() 


@login_manager.unauthorized_handler
def unauthorized():
    return render_template('unauth.html')

# Login Route
@main.route('/login', methods=["GET", "POST"])
def loginPage():
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            session['user']=user.first_name  
            return redirect(url_for('main.dashboard'))
        return render_template('auth/login.html', form=form, message="Invalid Credentials")
    
    return render_template('auth/login.html', form=form)

# Signup Route
@main.route('/signup', methods=["GET", "POST"])
def signuPage():
    form = SignupForm()
    if request.method == "POST" and form.validate():
        if User.query.filter_by(email=form.email.data).first():
            return render_template('auth/signup.html', form=form, message="User already exists!")

        hash_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=hash_password,
            gender=form.gender.data,
            dob=form.dob.data,
            pincode=form.pincode.data,
            occupation=form.occupation.data
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.loginPage'))

    return render_template('auth/signup.html', form=form)

# Logout Route
@main.route('/logout')
@login_required
def logout():
    logout_user()  
    session.clear()  
    return redirect(url_for('main.loginPage'))





@main.route('/')
def homePage():
    return render_template('main/home.html')

@main.route('/about')
def aboutPage():
    return render_template('main/about.html')

@main.route('/contact')
def contactPage():
    return render_template('main/contact.html')

@main.route('/dashboard/profile')
@login_required
def dashboard():
    return render_template('dashboard/profile.html')
