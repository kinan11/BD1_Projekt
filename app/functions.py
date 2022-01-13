import os
import urllib.parse as up
import psycopg2
from app.form import *
from flask import flash, session

DB_URL = "postgres://miwsxyxa:oeMo_2pOyETz6pJlzspi-CHR7uPbWrPn@castor.db.elephantsql.com:5432/miwsxyxa"

def execute_command(what):
    try:
        conn = psycopg2.connect(DB_URL)
        with conn:
            with conn.cursor() as cursor:
                cursor.execute("set search_path to wiezienie;")
                cursor.execute(f"{what};")
    except (Exception, psycopg2.Error) as error:
        print ("Error while fetching data from PostgreSQL", error)
    finally:
        conn.close()
        print("conn closed")



def myselect(what):
    try:
        conn = psycopg2.connect(DB_URL)
        with conn:
            with conn.cursor() as cursor:
                cursor.execute(what)
                records = cursor.fetchall()
        return records
    except (Exception, psycopg2.Error) as error:
        print ("Error while fetching data from PostgreSQL", error)
    finally:
        conn.close()
        print("conn closed")

def select_all(table):
    try:
        conn = psycopg2.connect(DB_URL)
        with conn:
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT * from {table};")
                records = cursor.fetchall()
        return records
    except (Exception, psycopg2.Error) as error:
        print ("Error while fetching data from PostgreSQL", error)
    finally:
        conn.close()
        print("conn closed")
        
def is_filled(data):
   if data == None:
      return False
   if data == '':
      return False
   if data == []:
      return False
   if data == 0:
      return False
   return True

def insert(table, form):
    names = []
    values = []
    pow = 'ok'
    for field in form:
        if is_filled(field.data) and field.name not in ["submit","csrf_token"]:
            names.append(field.name)
            values.append("'" + str(field.data) + "'")
    try:
        conn = psycopg2.connect(DB_URL)
        with conn:
            with conn.cursor() as cursor:

                if table == "Film":
                    cursor.execute(f"SELECT sprawdz_rezyser({values[0]}, {values[1]});")
                    id = cursor.fetchone()[0]
                    values[0] = "'" + str(id) + "'"
                    names[0] = 'id_rezyser'
                    names.pop(1)
                    values.pop(1)

                if table=="Sala":
                    cursor.execute(f"SELECT spr_sale({values[0]});")
                    numer = cursor.fetchone()[0]
                    names.append("numer")
                    values.append("'" + str(numer) + "'")

                if table=="Seans":
                    cursor.execute(f"SELECT spr_liczbe_miejsc({values[0]}, {values[1]});")
                    liczba = cursor.fetchone()[0]
                    print(values[0])
                    names.append("liczba_miejsc")
                    values.append("'" + str(liczba) + "'")

                if table=="Rezerwacja":
                    names.append('id_osoba')
                    values.append("'"+str(session['id'])+"'")
                    print(values)
                    print(names)

                print(values)
                print(names)
                names = ",".join(names)
                values = ",".join(values)
                cursor.execute(f"INSERT INTO {table}({names}) VALUES ({values});")
    except (Exception, psycopg2.Error) as error:
        print ("Error while fetching data from PostgreSQL", error)
        pow = error
    finally:
        conn.close()
        print("conn closed")
        return pow

def Forms_tuple():
    Forms = {
        "Napoje": napoje(),
        "Przekaski": przekaski(),
        "Rezyser":rezyser(),
        "Film": film(),
        "Sala":sala(),
        "Kino": kino(),
        "Seans": seans(),
        "Osoba": rejestracja(),
        "Rezerwacja": rezerwacja(),
    }
    return Forms

def handling_forms(form, form_name):
    if form_name == "Napoje":
        tmp = select_all("Kino")
        form.id_kino.choices = [(row[0], f"{row[1]} {row[2]}") for row in tmp]

    if form_name == "Przekaski":
        tmp = select_all("Kino")
        form.id_kino.choices = [(row[0], f"{row[1]} {row[2]}") for row in tmp]

    if form_name == "Sala":
        tmp = select_all("Kino")
        form.id_kino.choices = [(row[0], f"{row[1]} {row[2]}") for row in tmp]

    if form_name == "Seans":
        tmp = select_all("Kino")
        form.id_kino.choices = [(row[0], f"{row[1]} {row[2]}") for row in tmp]
        tmp = select_all("Film")
        form.id_film.choices = [(row[0], f"{row[4]}") for row in tmp]

    if form_name == "Seans":
        tmp = select_all("Kino")
        form.id_kino.choices = [(row[0], f"{row[1]} {row[2]}") for row in tmp]
        tmp = select_all("Film")
        form.id_film.choices = [(row[0], f"{row[4]}") for row in tmp]

def rezerwuj(form, id):
    tmp = myselect("SELECT * FROM seans("+id+");")
    form.id_seans.choices = [(row[0], f"{row[1]} DATA: {row[2]} GODZINA: {row[3]} CENA: {row[4]}zł") for row in tmp]
    tmp = select_all("Bilet")
    form.id_bilet.choices = [(row[0], f"{row[1]}") for row in tmp]
    tmp = myselect("Select * FROM rez_napoje("+id+");")
    form.id_napoje.choices = [(row[0], f"{row[1]}") for row in tmp]
    form.id_napoje.choices.insert(0, (0, 'Brak'))
    tmp = myselect("Select * FROM rez_przekaski("+id+");")
    form.id_przekaski.choices = [(row[0], f"{row[1]}") for row in tmp]
    form.id_przekaski.choices.insert(0, (0, 'Brak'))