from flask import Blueprint,render_template,redirect,request
from .models import User,SignupForm,LoginForm,db
main=Blueprint('main',__name__,url_prefix='/')

@main.route('/')
def homePage():
    return render_template('main/home.html')

@main.route('/about')
def aboutPage():
    return render_template('main/about.html')


@main.route('/contact')
def contactPage():
    return render_template('main/contact.html')










#dashboard
@main.route('/post')
def postPage():
    return render_template('dashboard/post.html')



































#auth
@main.route('/login',methods=["GET","POST"])
def loginPage():
    form=LoginForm()
    if request.method=="POST":  
        return redirect('/')
    return render_template('auth/login.html',form=form)


@main.route('/signup',methods=["GET","POST"])
def signuPage():
    form=SignupForm()
    if request.method=="POST":
        if form.validate():
            if User.query.filter(User.email=="22eg107c61@anurag.edu.in").first():
                return render_template('auth/signup.html',form=form,message='user exit')
            user=User(first_name=form.first_name.data,last_name=form.last_name.data,email=form.email.data,gender=form.gender.data,dob=form.dob.data,pincode=form.pincode.data,occupation=form.occupation.data)
            db.session.add(user)
            db.session.commit()
            return redirect('/')
    return render_template('auth/signup.html',form=form)

