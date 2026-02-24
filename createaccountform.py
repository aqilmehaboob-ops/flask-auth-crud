from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField, DateField
from wtforms.validators import DataRequired

class Form(FlaskForm):
    name = StringField(label='name', validators=[DataRequired()])
    password = PasswordField(label='password', validators=[DataRequired()])
    age = PasswordField(label='age', validators=[DataRequired()])
    height = IntegerField(label='height', validators=[DataRequired()])
    date = DateField(label='date', validators=[DataRequired()])
    weight = IntegerField(label='weight', validators=[DataRequired()])
    submit = SubmitField(label='submit')

