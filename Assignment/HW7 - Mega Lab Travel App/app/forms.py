from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, SelectField, RadioField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired
from models import *
from flask import render_template, session, redirect, request, url_for, escape


class TripForm(Form):
    name = StringField('name', validators=[DataRequired()])
    destination = StringField('destination', validators=[DataRequired()])
    friend = RadioField('Your Friend', choices = [])
