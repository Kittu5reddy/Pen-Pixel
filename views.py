from flask import Blueprint,render_template,redirect

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
@main.route('/login')
def loginPage():
    return render_template('auth/login.html')


@main.route('/signup')
def signuPage():
    return render_template('auth/signup.html')

