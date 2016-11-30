from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Regexp, Email

class LoginForm(FlaskForm):
	email = StringField('Email', validators=[InputRequired(), Length(1, 64), \
											Email()])
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
#    secret_key = StringField('secret_key', validators=[Regexp('hahaha')])
    remember_me = BooleanField('Remember login', default=False)
    submit = SubmitField('Log In')