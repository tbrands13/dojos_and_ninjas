from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja



@app.route('/dojos')
def index():
    all_dojos = Dojo.get_all_dojos()
    return render_template("dojos.html", all_dojos= all_dojos)




@app.route('/dojocreate', methods=['POST'])
def make_dojo():
    data = {
        "name" : request.form["name"]
    }
    Dojo.make_dojo(data)
    return redirect('/dojos')






@app.route('/show/<int:id>')
def show_ninjas(id):

    data = {
        'id' : id

    }
    print("******************")
    dojo = Dojo.pick_one_dojo(data)
    print(dojo,data)
    print(request.form)
    return render_template("dojosshow.html", dojo = dojo)


