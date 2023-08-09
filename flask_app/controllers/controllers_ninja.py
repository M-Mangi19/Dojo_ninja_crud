from flask_app import app
from flask import Flask, render_template, redirect, request, session, flash
from flask_app.models.models_ninja import Ninja
from flask_app.models.models_dojo import Dojo


@app.route('/')
def index():
    # ninjas = Ninja.get_all()
    # print(ninjas)
    return render_template('index.html', dojos = Dojo.get_all())



# @app.route('/new_ninja')
# def new_ninja():
#     return render_template('')




@app.route('/create_ninja', methods=['POST'])
def create_ninja():
    data ={
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form['age']
    }
    Ninja.create(request.form)
    return redirect('/dashboard')
