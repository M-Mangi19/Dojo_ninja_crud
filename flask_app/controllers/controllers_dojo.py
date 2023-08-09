from flask_app import app
from flask import Flask, render_template, redirect, request, session, flash
from flask_app.models.models_dojo import Dojo
from flask_app.models.models_ninja import Ninja



@app.route('/dashboard')
def dashboard():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template('dashboard.html', dojos = dojos)


@app.route('/new_ninja')
def new_ninja():
    ninja =Ninja.get_all()
    return render_template('index.html', ninjas = ninjas)



@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    data ={
        "name" : request.form["name"],
        # "ninja_id" : request.form["ninja_id"]
    }
    Dojo.create(request.form)
    return redirect('/dashboard')

@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = {
        "id" : id
    }
    return render_template('dojo.html', dojo = Dojo.get_dojo_with_ninjas(data))



