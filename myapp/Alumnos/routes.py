from flask import Flask, render_template, redirect
from flask import request
from flask import url_for
import  forms
from models import Alumnos 
from models import db 

from . import alumnos

@alumnos.route("/alumnos", methods=["GET", "POST"])
def iniciar():
    create_form = forms.UserForms(request.form)
    if request.method == 'POST':
        alumn = Alumnos(nombre = create_form.nombre.data,
                        apellidos =  create_form.apellidos.data,
                        email = create_form.email.data
                        )
        db.session.add(alumn)
        db.session.commit()
        return redirect(url_for('alumnos.ABCompleto'))
    return render_template("alumnos.html", form = create_form)

@alumnos.route("/modificar", methods=["GET", "POST"])
def modificar():
    create_form = forms.UserForms(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = request.args.get('id')
        create_form.nombre.data = alum1.nombre
        create_form.apellidos.data = alum1.apellidos
        create_form.email.data = alum1.email
    if request.method == 'POST':
        id = create_form.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alum.nombre  = create_form.nombre.data
        alum.apellidos  = create_form.apellidos.data
        alum.email  = create_form.email.data
        db.session.add(alum)
        db.session.commit()

        return redirect(url_for('alumnos.ABCompleto'))
    return render_template("modificar.html", form = create_form)

@alumnos.route("/eliminar", methods=["GET", "POST"])
def eliminar():
    create_form = forms.UserForms(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = request.args.get('id')
        create_form.nombre.data = alum1.nombre
        create_form.apellidos.data = alum1.apellidos
        create_form.email.data = alum1.email
    if request.method == 'POST':
        id = create_form.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alum.nombre  = create_form.nombre.data
        alum.apellidos  = create_form.apellidos.data
        alum.email  = create_form.email.data
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for('alumnos.ABCompleto'))
    return render_template("eliminar.html", form = create_form)
    
@alumnos.route("/ABCompleto", methods=["GET", "POST"])
def ABCompleto():
    create_form = forms.UserForms(request.form)
    alumno = Alumnos.query.all()
    return render_template("ABCompleto.html", form = create_form, alumno = alumno)

