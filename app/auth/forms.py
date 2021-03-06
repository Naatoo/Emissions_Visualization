from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

#
# class RegistrationForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[
#                                         DataRequired(),
#                                         EqualTo('confirm_password')
#                                         ])
#     confirm_password = PasswordField('Confirm Password')
#     submit = SubmitField('Register')
