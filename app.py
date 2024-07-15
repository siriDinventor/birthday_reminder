import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, flash, jsonify, redirect, render_template, request, session
import sqlite3

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Connect to the birthdays SQLite database


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    connection = sqlite3.connect('birthdays.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    if request.method == "POST":
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")

        # TODO: Add the user's entry into the database
        if name and month and day:
            cursor.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", (name, month, day))
            connection.commit()

        return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html
        birthdays = cursor.execute("SELECT * FROM birthdays").fetchall()
        connection.close()

        return render_template("index.html", birthdays=birthdays)











# import os
# import sqlite3
# from flask import Flask, flash, jsonify, redirect, render_template, request, session

# # Configure application
# app = Flask(__name__)

# # Ensure templates are auto-reloaded
# app.config["TEMPLATES_AUTO_RELOAD"] = True

# def get_db_connection():
#     conn = sqlite3.connect('birthdays.db')
#     conn.row_factory = sqlite3.Row
#     return conn

# @app.after_request
# def after_request(response):
#     """Ensure responses aren't cached"""
#     response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
#     response.headers["Expires"] = 0
#     response.headers["Pragma"] = "no-cache"
#     return response

# @app.route("/", methods=["GET", "POST"])
# def index():
#     conn = get_db_connection()
#     cursor = conn.cursor()

#     if request.method == "POST":
#         name = request.form.get("name")
#         month = request.form.get("month")
#         day = request.form.get("day")

#         if name and month and day:
#             cursor.execute("INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)", (name, month, day))
#             conn.commit()
#         conn.close()

#         return redirect("/")

#     else:
#         birthdays = cursor.execute("SELECT * FROM birthdays").fetchall()
#         conn.close()

#         return render_template("index.html", birthdays=birthdays)

# if __name__ == "__main__":
#     app.run(debug=True)
