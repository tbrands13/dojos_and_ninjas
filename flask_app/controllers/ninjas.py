from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.ninja import Ninja


@app.route('/ninjas')
def get_ninja():
    ninjas = Ninja.all_ninjas()
    return render_template("ninjas.html", ninjas = ninjas)

@app.route('/create', methods=["POST"])
def create_ninja():
    data = {
        "fname" : request.form['fname'],
        "lname" : request.form['lname'],
        "age" : request.form['age'],
        "dojo_id" : request.form['dojo_id']
    }
    Ninja.create_ninja(data)
    return redirect("/dojos")

