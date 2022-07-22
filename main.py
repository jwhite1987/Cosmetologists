import flask
from google.cloud import bigquery
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'credentials_2.json'
from sqlalchemy import *
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from flask import Flask, render_template, request, flash
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, RadioField, HiddenField, StringField, IntegerField, FloatField
from wtforms.validators import InputRequired, Length, Regexp, NumberRange
from datetime import date

app = flask.Flask(__name__)

project_id = 'stylist-project-357102'
dataset_name = 'stylist_dataset'
credentials = 'credentials_2.json'
url = 'bigquery://'+project_id+"/"+dataset_name+"?credentials_path="+credentials

app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class cosm(db.Model):
    __tablename__ = 'dataset-table'
    ID = db.Column(db.Integer, primary_key=True)
    string_field_0 = db.Column(db.String)
    string_field_1 = db.Column(db.String)
    string_field_2 = db.Column(db.String)
    string_field_3 = db.Column(db.String)
    string_field_4 = db.Column(db.String)
    string_field_5 = db.Column(db.String)
    string_field_6 = db.Column(db.String)
    def __init__(self, first_name, last_name, city, state, license_code, miles_away):
        self.first_name = string_field_0
        self.last_name = string_field_1
        self.city = string_field_2
        self.state = string_field_3
        self.license_code = string_field_4
        self.miles_away = string_field_6

class DeleteForm(FlaskForm):
    id_field = HiddenField()
    purpose = HiddenField()
    submit = SubmitField('Delete This Sock')

@app.route("/")
def index():
    return flask.render_template('index.html')

@app.route("/home")
def home():
    client = bigquery.Client()
    query_job = client.query(
        """
        SELECT
        *
        FROM
        `stylist-project-357102.stylist_dataset.dataset-table`
        LIMIT 50
        """
    )
    cosms = query_job.result()
    return flask.render_template('home.html', cosms=cosms)

@app.route("/select_record", methods=['POST'])
def select_record():
    id = request.form['id']
    choice = request.form['choice']
    results = cosm.query.filter(cosm.ID == id).first()
    # two forms in this template
    form = DeleteForm()
    return flask.render_template("select_record.html", results=results, form=form, choice=choice)

# @app.route('/delete_result', methods=['POST'])
# def delete_result():
#     id = request.form['id_field']
#     purpose = request.form['purpose']
#     Cosm = cosm.query.filter(cosm.ID == id).first()
#     if purpose == 'delete':
#         db.session.delete(Cosm)
#         db.session.commit()
#         message = f"The sock {cosm.first_name} has been deleted from the database."
#         return flask.render_template('result.html', message=message)
#     else:
#         return flask.render_template("index.html")
#         this calls an error handler
#         abort(405)
# @app.route("/ft_mill")
# def ft_mill():
#     return flask.render_template('ft_mill.html')
#
# @app.route("/huntersville")
# def huntersville():
#     return flask.render_template('huntersville.html')
#
# @app.route("/matthews")
# def matthews():
#     return flask.render_template('matthews.html')
#
if __name__ == "__main__":
    app.run(debug=True)
