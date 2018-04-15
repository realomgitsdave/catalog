from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.update(dict(
    SQLALCHEMY_DATABASE_URI = 'sqlite:///sqlite.db',
    SECRET_KEY = 'balls',
))

db = SQLAlchemy(app)
session = db.session()
from . import views