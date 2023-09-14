from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from map.map import map

choice = list(map)
print(choice)
class PackageForm(FlaskForm):
    sender = StringField("Sender", validators=[DataRequired()])
    recipient = StringField("Recipient", validators=[DataRequired()])
    origin = SelectField("Origin", validators=[DataRequired()], choices=choice)
    destination = SelectField("Destination", validators=[DataRequired()], choices=choice)
    express = BooleanField("Express", validators=[DataRequired()])
    submit = SubmitField("Create Package")
