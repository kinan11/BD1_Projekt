from app import app
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from app.form import *

from app.form import *
from app.functions import *
DB_URL = "postgres://miwsxyxa:oeMo_2pOyETz6pJlzspi-CHR7uPbWrPn@castor.db.elephantsql.com:5432/miwsxyxa"

@app.route('/')
def index():
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('index.html', username=session['username'])
    return render_template('index.html')

#creating form to add row into the table "form_name"
@app.route('/add/<form_name>', methods=["GET", "POST"])
def add(form_name):
    Forms = Forms_tuple()

    if form_name == 'none':
        return redirect(url_for('select_form', function='add'))

    form = Forms[form_name]

    handling_forms(form,form_name)
    print(form_name, form)
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
def data(function=0, username='none'):
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

@app.route('/rezerwacja', methods=["GET", "POST"])
def rezerwacja():
    show = True
    records = []
    records = myselect("SELECT id_kino, nazwa,miasto FROM Kino")
    names = [[records[i][0], records[i][1] + ' ' + records[i][2]] for i in range(len(records))]

    return render_template('rezerwacja.html', names=names, show=show)

@app.route('/reg', methods=["GET", "POST"])
def reg():
    select = request.form.get("sel_kino")
    Forms = Forms_tuple()
    form = Forms["Rezerwacja"]
    rezerwuj(form, select)
    x = [key for key, value in Forms.items()]
    print(form)
    return render_template('form.html', form = form)

@app.route('/rez', methods=["GET", "POST"])
def rez():
    Forms = Forms_tuple()
    form = Forms["Rezerwacja"]
    if form.is_submitted():
        pow=insert("Rezerwacja",form)
        if pow=='ok':
            flash('Zarezerwowano!')
        else:
            flash('Nie zarezerwowano: '+ str(pow).split('CONTEXT')[0])
        return redirect(url_for('index'))

    return render_template('index')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        conn = psycopg2.connect(DB_URL)
        login = "'" + str(username) + "'"
        haslo = "'" + str(password) + "'"
        try:
            conn = psycopg2.connect(DB_URL)
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(f"SELECT * FROM Osoba WHERE login = {login} AND haslo = {haslo};")
                    account = cursor.fetchone()
                    print(type(account))
                    if account[0]:
                         session['loggedin'] = True
                         session['id'] = account[0]
                         session['username'] = account[1]
                         return redirect(url_for('index'))
                    else:
                         flash('Incorrect username/password')
        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)
        finally:
            conn.close()
            print("conn closed")

    return render_template('login.html')

@app.route('/wyloguj/')
def wyloguj():
    session.clear()
    return redirect(url_for('index'))

@app.route('/bilet', methods=["GET", "POST"])
def bilet():
    names = []
    show = False
    records = []
    names = ['Film','Kino','Data', 'Godzina', 'Przekaska', 'Napój', 'Bilet', 'Cena']
    records =myselect("SELECT tytul,Kino.nazwa||' '||miasto,  data, godzina,przekaski.nazwa, napoje.nazwa, opis, rezerwacja.cena FROM Rezerwacja JOIN Napoje ON rezerwacja.id_napoje = Napoje.id_napoje JOIN Przekaski ON Rezerwacja.id_przekaski = Przekaski.id_przekaski JOIN Seans ON Rezerwacja.id_seans = Seans.id_seans JOIN Film ON Seans.id_film = Film.id_film JOIN Kino ON Seans.id_kino = Kino.id_kino JOIN bilet ON Rezerwacja.id_bilet = Bilet.id_bilet WHERE id_osoba = '"+str(session['id'])+"'; ")

    return render_template('bilet.html', records=records, names=names)

