from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import UserMixin
import uuid

csrf = CSRFProtect()
db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.String(36), primary_key=True, default= str(uuid.uuid4()))  # ✅ Uses UUID as primary key
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)  # ✅ Email must be unique and NOT NULL
    password = db.Column(db.String(255), nullable=False)  # ✅ Increased password length for security
    gender = db.Column(db.String(10), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    pincode = db.Column(db.Integer, nullable=False)
    occupation = db.Column(db.String(120), nullable=False)

    def get_id(self):
        return str(self.id)  # ✅ Flask-Login requires get_id() to return a string

    def __repr__(self):
        return f'<User {self.email}>'  # ✅ Fixed __repr__

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









