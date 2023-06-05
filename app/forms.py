from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField # StringField() is a field
from wtforms.validators import DataRequired, Length, Email, EqualTo # DataRequired() is a validator


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password= PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField ('Register')
    
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField ('Login')
    
class AddMarvelCharacterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    comics_appeared_in = StringField('Comics Appeared In', validators=[DataRequired()])
    super_power = StringField('Super Power', validators=[DataRequired()])
    submit = SubmitField ('Add')
    
class AddDrinkForm(FlaskForm):
    idDrink = StringField('Drink ID', validators=[DataRequired()])
    strDrink = StringField('Drink Name', validators=[DataRequired()])
    strDrinkThumb = StringField('Drink Image', validators=[DataRequired()])
    submit = SubmitField ('Add')
    