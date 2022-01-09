from app import app
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from app.form import *
from app.functions import *

@app.route('/')
def index():
    return render_template('index.html')

#creating form to add row into the table "form_name"
@app.route('/add/<form_name>', methods=["GET", "POST"])
def add(form_name):
    Forms = Forms_tuple()

    if form_name == 'none':
        return redirect(url_for('select_form', function='add'))

    form = Forms[form_name]

    handling_forms(form,form_name)
    if form.is_submitted():
        pow=insert(form_name,form)
        if pow=='ok':
            flash('Dodanie powiodło się!')
        else:
            flash('Dodanie nie powiodło się: '+ str(pow).split('CONTEXT')[0])
        return redirect(url_for('index'))

    return render_template('form.html', form = form)

@app.route('/select/<form_name>', methods=["GET", "POST"])
def select(form_name):
    Forms = Forms_tuple()

    if form_name == 'none':
        return redirect(url_for('select_form', function='select'))
    
    form = Forms[form_name]
    records = select_all(form_name)

    return render_template('select.html', form = form, records= records)

@app.route('/select_form/<function>', methods=["GET", "POST"])
def select_form(function):
    form = select_table()
    Forms= Forms_tuple()
    x = [key for key,value in Forms.items()]
    form.nazwa.choices = x
    if form.is_submitted():
        result = request.form['nazwa']
        return redirect(url_for(function, form_name=result))
    return render_template('form.html', form = form)

@app.route('/data', methods=["GET", "POST"])  
@app.route('/data/<function>', methods=["GET", "POST"])
def data(function=0):
    names = []
    show = False
    records = []
    if function:
        show = True

        if function == '1':
            names = ['Tytuł','Reżyser','Rok produkcji', 'Czas trwania [m]', 'Ocena']
            records =myselect("SELECT tytul,imie||' '||nazwisko, rok, czas, ocena FROM Film JOIN Rezyser ON Film.id_rezyser=Rezyser.id_rezyser")

        if function == '2':
            names = ['Nazwa', 'Miasto', 'Liczba sal']
            records= myselect("SELECT nazwa, miasto,COUNT(id_sala) FROM Kino JOIN Sala ON Kino.id_kino=Sala.id_kino  GROUP BY sala.id_kino, kino.nazwa , kino.miasto ORDER BY nazwa;")

        if function == '3':
            names = ['Nazwa', 'Cena']
            records = myselect("SELECT nazwa, cena FROM Przekaski ORDER BY nazwa")
            records += myselect("SELECT nazwa, cena FROM Napoje ORDER BY nazwa")

    return render_template('data.html', records=records, names=names, show=show)


@app.route('/repertuar', methods=["GET", "POST"])
#@app.route('/repertuar/<function>', methods=["GET", "POST"])
def repertuar():
    show = True
    records = []
    records = myselect("SELECT id_kino, nazwa,miasto FROM Kino")
    names=[[records[i][0],records[i][1]+' '+records[i][2]] for i in range(len(records))]

    return render_template('repertuar.html', names=names, show=show)

@app.route('/sel', methods=["GET", "POST"])
@app.route('/sel/<function>', methods=["GET", "POST"])
def sel(function=0):
    select = request.form.get("sel_rep")
    names = ['Tytuł', 'Data', 'Godzina']
    records = []
    records = myselect("SELECT tytul, data,godzina FROM Seans JOIN Film ON Film.id_film= Seans.id_film WHERE id_kino="+select+"ORDER BY data, godzina")

    return render_template('sel.html', records=records, names=names)