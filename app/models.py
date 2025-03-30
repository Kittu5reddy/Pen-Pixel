from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
csrf=CSRFProtect()
db=SQLAlchemy()









class User(db.Model):
    def __init__(self,first_name,last_name,email,gender,dob,pincode,occupation,password):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.gender=gender
        self.dob=dob
        self.pincode=pincode
        self.occupation=occupation
        self.password=password
    first_name=db.Column(db.String(120),nullable=False)
    last_name=db.Column(db.String(120),nullable=False)
    email=db.Column(db.String(120),primary_key=True)
    password=db.Column(db.String(120))
    gender=db.Column(db.String(120),nullable=False)
    dob=db.Column(db.String(120),nullable=False)
    pincode=db.Column(db.Integer,nullable=False)
    occupation=db.Column(db.String(120),nullable=False)
    def repr(self):
        return str(self.email)
#forms
from flask_wtf import FlaskForm  # Import FlaskForm instead of Form
from wtforms import StringField, PasswordField, RadioField, DateField, IntegerField, validators

class SignupForm(FlaskForm):  # Change Form to FlaskForm
    first_name = StringField(
        'First Name',
        [validators.DataRequired(), validators.Length(max=120)],
        render_kw={"placeholder": "Enter your first name"}
    )
    last_name = StringField(
        'Last Name',
        [validators.DataRequired(), validators.Length(max=120)],
        render_kw={"placeholder": "Enter your last name"}
    )
    email = StringField(
        'Email ID',
        [validators.DataRequired(), validators.Email()],
        render_kw={"placeholder": "Enter your email"}
    )
    password = PasswordField(
        'Password',
        [validators.DataRequired(), validators.Length(min=6)],
        render_kw={"placeholder": "Enter your password"}
    )
    confirm_password = PasswordField(
        'Confirm Password',
        [validators.DataRequired(), validators.EqualTo('password', message='Passwords must match')],
        render_kw={"placeholder": "Confirm your password"}
    )
    gender = RadioField('Gender', choices=[('female', 'Female'), ('male', 'Male'), ('other', 'Other')],
        validators=[validators.DataRequired()]
    )
    dob = DateField('Date of Birth', [validators.DataRequired()], render_kw={"placeholder": "Enter your date of birth"})
    pincode = IntegerField('Pincode', [validators.DataRequired()], render_kw={"placeholder": "Enter your pincode"})
    occupation = StringField('Occupation', [validators.DataRequired()], render_kw={"placeholder": "Enter your occupation"})


class LoginForm(FlaskForm):  # Change Form to FlaskForm
    email = StringField(
        'Email',
        [validators.DataRequired(), validators.Email()],
        render_kw={"placeholder": "Enter your email"}
    )
    password = PasswordField(
        'Password',
        [validators.DataRequired()],
        render_kw={"placeholder": "Enter your password"}
    )









