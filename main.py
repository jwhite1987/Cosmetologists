from flask import Flask, render_template, redirect, url_for, jsonify, request, redirect
from config import DB_PASSWORD
from flask_cors import CORS
import psycopg2
# import os

###################################### I G N O R E ################
# import sqlalchemy
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine
# from sqlalchemy import func
# import numpy as np
###################################### I G N O R E ################

app = Flask(__name__)

CORS(app)

try:
    con = psycopg2.connect(
        database='postgres',
        user='postgres',
        password=DB_PASSWORD,
        host='34.86.56.198',
        port='5432'
    )

    cur = con.cursor()

except:
    print('Error')

@app.route("/")
def index():

    # Return template and data
    return render_template("index.html")
#
# @app.route("/home")
# def home():
#
#     # Return template and data
#     return render_template("home.html")
#
#
# @app.route('/search', methods=['GET', 'POST'])
# def search():
#     if request.method == "POST":
#         wine = request.form['wine']
#         cur.execute(f'SELECT * FROM gws_cleaned_dataset WHERE vintage = {wine} ORDER BY score DESC;')
#         con.commit()
#         data = cur.fetchall()
#         if len(data) == 0 and wine == 'all':
#             cur.execute("SELECT * FROM gws_cleaned_dataset")
#             con.commit()
#             data = cursor.fetchall()
#         return render_template('search.html', data=data)
#     return render_template('search.html')
#
#     cur.rollback()
#
# @app.route('/search2', methods=['GET', 'POST'])
# def search2():
#     if request.method == "POST":
#         country = request.form['country']
#         cur.execute(f'SELECT * FROM gws_cleaned_dataset WHERE country = \'{country}\' ORDER BY score DESC;')
#         con.commit()
#         data = cur.fetchall()
#         if len(data) == 0 and country == 'all':
#             cur.execute("SELECT * FROM gws_cleaned_dataset")
#             con.commit()
#             data = cursor.fetchall()
#         return render_template('search2.html', data=data)
#     return render_template('search2.html')
#
#     cur.rollback()
#
# @app.route('/colors', methods=['GET', 'POST'])
# def colors():
#     if request.method == "POST":
#         color = request.form['colorWine']
#         cur.execute(f'SELECT * FROM gws_cleaned_dataset WHERE color = \'{color}\' ORDER BY score DESC;')
#         con.commit()
#         data = cur.fetchall()
#         if len(data) == 0 and color == 'all':
#             cur.execute("SELECT * FROM gws_cleaned_dataset")
#             con.commit()
#             data = cursor.fetchall()
#         return render_template('colors.html', data=data)
#     return render_template('colors.html')
#
#     cur.rollback()
#
# @app.route("/map")
# def map():
#
#     # Return template and data
#     return render_template("map.html")
#
# @app.route("/new_charts")
# def new_charts():
#
#     # Return template and data
#     return render_template("new_charts.html")
#
# @app.route("/team")
# def team():
#
#     # Return template and data
#     return render_template("team.html")
#
# @app.route("/test")
# def test():
#
#     # Return template and data
#     return render_template("test.html")
#
# @app.route("/icons")
# def icons():
#
#     # Return template and data
#     return render_template("icons.html")
#
# @app.route("/winemag")
# def winemag():
#
#     # Return template and data
#     return render_template("wine-mag.html")
#
# @app.route("/charts")
# def charts():
#
#     # Return template and data
#     return render_template("charts.html")



if __name__ == "__main__":
    app.run(debug=True)
