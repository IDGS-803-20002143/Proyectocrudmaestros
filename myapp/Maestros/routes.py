from flask import Flask, render_template, redirect
from flask import request
from flask import url_for
import forms
from models import Maestros 
from db import get_connection

from . import maestros

@maestros.route("/maestros", methods=["GET", "POST"])
def iniciar():
    create_form = forms.UserForms(request.form)
    if request.method == 'POST':
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call AGREGAR_MAESTRO(%s, %s, %s)', 
                               (create_form.nombre.data, 
                                create_form.apellidos.data,
                                create_form.email.data))                        

                connection.commit()
                connection.close()
        except Exception as ex:
            print(ex)
        return redirect(url_for('maestros.ABCompletoM'))
    return render_template("maestros.html", form = create_form)

    
@maestros.route("/ABCompletoM", methods=["GET", "POST"])
def ABCompletoM():
    create_form = forms.UserForms(request.form)
    maestro = []
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('call consultar_maestros()')
            maestros = cursor.fetchall()
            for row in maestros:
                id, nombre, apellidos, email, create_date = row
                objM =  Maestros(
                        id = id,
                        nombre = nombre,
                        apellidos =  apellidos,
                        email = email,
                        create_date = create_date
                        )
                maestro.append(objM)
    except Exception as ex:
        print(ex)
    return render_template("ABCompletoM.html", form = create_form, maestro = maestro)


@maestros.route("/modificarM", methods=["GET", "POST"])
def modificarM():
    create_form = forms.UserForms(request.form)
    if request.method == 'GET':
        id = int(request.args.get('id'))
        maestro = Maestros()
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call CONSULTAR_MAESTRO(%s)', (id,))
                maestros = cursor.fetchall()
                for row in maestros:
                    id, nombre, apellidos, email, create_date = row
                    maestro =  Maestros(
                        id = id,
                        nombre = nombre,
                        apellidos =  apellidos,
                        email = email,
                        create_date = create_date
                        )
                print(maestro)
        except Exception as ex:
            print(ex)

        create_form.id.data = request.args.get('id')
        create_form.nombre.data = maestro.nombre
        create_form.apellidos.data = maestro.apellidos
        create_form.email.data = maestro.email
        
    if request.method == 'POST':
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                
                cursor.execute('call MODIFICAR_MAESTRO(%s, %s, %s, %s)', 
                               (create_form.id.data, 
                                create_form.nombre.data, 
                                create_form.apellidos.data,
                                create_form.email.data))                        

                connection.commit()
                connection.close()
        except Exception as ex:
            print(ex)
        return redirect(url_for('maestros.ABCompletoM'))
    return render_template("modificarM.html", form = create_form)

@maestros.route("/eliminarM", methods=["GET", "POST"])
def eliminarM():
    create_form = forms.UserForms(request.form)
    if request.method == 'GET':
        id = int(request.args.get('id'))
        maestro = Maestros()
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call CONSULTAR_MAESTRO(%s)', (id,))
                maestros = cursor.fetchall()
                for row in maestros:
                    id, nombre, apellidos, email, create_date = row
                    maestro =  Maestros(
                        id = id,
                        nombre = nombre,
                        apellidos =  apellidos,
                        email = email,
                        create_date = create_date
                        )
                print(maestro)
        except Exception as ex:
            print(ex)

        create_form.id.data = request.args.get('id')
        create_form.nombre.data = maestro.nombre
        create_form.apellidos.data = maestro.apellidos
        create_form.email.data = maestro.email
        
    if request.method == 'POST':
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                
                cursor.execute('call ELIMINAR_MAESTRO_POR_ID(%s)', (create_form.id.data,))                        

                connection.commit()
                connection.close()
        except Exception as ex:
            print(ex)
        return redirect(url_for('maestros.ABCompletoM'))
    return render_template("eliminarM.html", form = create_form)


