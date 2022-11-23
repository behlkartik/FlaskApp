from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from app.models import User



class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError("Username already exists, Please try another username")

    def validate_email(self, email_to_check):
        user = User.query.filter_by(email=email_to_check.data).first()
        if user:
            raise ValidationError("Email already exists, Please try another email address")

    username = StringField(label="Username", validators=[Length(min=5, max=20), DataRequired()])
    email = StringField(label="Email Address", validators=[Email(), DataRequired()])
    password = PasswordField(label="Password",  validators=[Length(min=8), DataRequired()])
    confirm_password = PasswordField(label="Confirm Password", validators=[EqualTo('password'), DataRequired()])
    submit_button = SubmitField(label="Create Account")


