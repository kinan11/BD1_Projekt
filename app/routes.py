from app import app
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from app.form import *
from flask_session import Session

from app.form import *
from app.functions import *
DB_URL = "postgres://miwsxyxa:oeMo_2pOyETz6pJlzspi-CHR7uPbWrPn@castor.db.elephantsql.com:5432/miwsxyxa"

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def index():
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('index.html', username=session.get("name"))
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
            flash('Pomyślnie dodano!')
        else:
            flash('Wystapił bład: '+ str(pow).split('CONTEXT')[0])
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
    del x[len(x) - 1]
    del x[len(x) - 1]
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
            names = ['Tytuł','Reżyser','Rok produkcji', 'Czas trwania [m]', 'Ocena', 'Liczba dostępnych kin']
            records = myselect("SELECT * from wszystkie_filmy ORDER BY tytul")

        if function == '2':
            names = ['Nazwa', 'Miasto', 'Liczba sal', 'Ilość wyświetlanych filmów']
            records= myselect("SELECT * from lista_kin ORDER BY miasto")

        if function == '3':
            records = myselect("SELECT * FROM form_kino")
            names = [[records[i][0], records[i][1] + ' ' + records[i][2]] for i in range(len(records))]

            return render_template('menu.html', names=names, show=show)

        if function == '4':
            select = request.form.get("menu_form")
            names = ['Nazwa', 'Cena']
            records = myselect("SELECT * FROM bufet_przekaski("+select+")")
            records += myselect("SELECT * FROM bufet_napoje(" + select + ")")

        if function == '5':
            names = ['Imię', 'Nazwisko', 'Liczba filmów aktualnie granych w kinach', 'Średnia ocena']
            records = myselect("SELECT * from rank_rezyser ORDER BY avg DESC")

    return render_template('data.html', records=records, names=names, show=show)


@app.route('/repertuar', methods=["GET", "POST"])
def repertuar():
    show = True
    records = []
    records = myselect("SELECT * FROM form_kino")
    names=[[records[i][0],records[i][1]+' '+records[i][2]] for i in range(len(records))]

    return render_template('repertuar.html', names=names, show=show)

@app.route('/sel', methods=["GET", "POST"])
@app.route('/sel/<function>', methods=["GET", "POST"])
def sel(function=0):
    select = request.form.get("sel_rep")
    names = ['Tytuł', 'Data', 'Godzina']
    records = []
    records = myselect("SELECT * FROM repertuar("+select+")")

    return render_template('sel.html', records=records, names=names)

@app.route('/rezerwacja', methods=["GET", "POST"])
def rezerwacja():
    show = True
    records = []
    records = myselect("SELECT * FROM form_kino")
    names = [[records[i][0], records[i][1] + ' ' + records[i][2]] for i in range(len(records))]

    return render_template('rezerwacja.html', names=names, show=show)

@app.route('/reg', methods=["GET", "POST"])
def reg():
    select = request.form.get("sel_kino")
    Forms = Forms_tuple()
    form = Forms["Rezerwacja"]
    rezerwuj(form, select)
    x = [key for key, value in Forms.items()]
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
    if request.method == 'POST' and 'login' in request.form and 'haslo' in request.form:
        username = request.form['login']
        password = request.form['haslo']
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
                         #session['loggedin'] = True
                         session['id'] = account[0]
                         #session['username'] = account[1]
                         session["name"] = account[1]
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
    #session.clear()
    session["name"] = None
    return redirect(url_for('index'))

@app.route('/bilet', methods=["GET", "POST"])
def bilet():
    names = []
    show = False
    records = []
    names = ['Film','Kino','Data', 'Godzina', 'Przekaska', 'Napój', 'Bilet', 'Cena']
    records = myselect("SELECT * FROM bilety(" +str(session['id'])+ ")")
    for i in range(len(records)):
        for j in range(len(records[i])):
            if not records[i][j]:
                print(records[i][j])

    return render_template('bilet.html', records=records, names=names)

