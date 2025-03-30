from flask import Blueprint,render_template,redirect,request,url_for,session
from .models import User,SignupForm,LoginForm,db
from flask_bcrypt import Bcrypt
main=Blueprint('main',__name__,url_prefix='/')
bcrypt=Bcrypt()

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
def dashboard():
    return render_template('dashboard/profile.html')






#auth
@main.route('/login',methods=["GET","POST"])
def loginPage():
    form=LoginForm()
    if request.method=="POST":  
        if form.validate_on_submit():
            email=form.email.data
            password=form.password.data
            user=User.query.filter_by(email=email).first()
            if user:
                if bcrypt.check_password_hash(user.password,password):
                    session['user']=user.first_name
                    return redirect(url_for('main.dashboard'))
            return render_template('auth/login.html',form=form)
    return render_template('auth/login.html',form=form)


@main.route('/signup',methods=["GET","POST"])
def signuPage():
    form=SignupForm()
    if request.method=="POST":
        if form.validate():
            hash_password=bcrypt.generate_password_hash(form.password.data).decode("utf-8")
            user=User(first_name=form.first_name.data,password=hash_password,last_name=form.last_name.data,email=form.email.data,gender=form.gender.data,dob=form.dob.data,pincode=form.pincode.data,occupation=form.occupation.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.loginPage'))
        
    return render_template('auth/signup.html',form=form)

@main.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.loginPage'))