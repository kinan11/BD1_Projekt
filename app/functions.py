import os
import urllib.parse as up
import psycopg2
from app.form import *

#DB_URL = "postgres://gvenvzai:Ai4So0-MbWLPhHtyT6sstL9p_qlTrybY@kandula.db.elephantsql.com:5432/gvenvzai"
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
                #cursor.execute("set search_path to wiezienie;")
                #cursor.execute(f"{what};")
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
               # cursor.execute("set search_path to wiezienie;")
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
    for field in form:
        if is_filled(field.data) and field.name not in ["submit","csrf_token"]:
            names.append(field.name)
            values.append("'" + str(field.data) + "'")
    names = ",".join(names)
    values = ",".join(values)
    #print(names)
    #print(values)
    try:
        conn = psycopg2.connect(DB_URL)
        with conn:
            with conn.cursor() as cursor:
                #cursor.execute("set search_path to wiezienie;")
                cursor.execute(f"INSERT INTO {table}({names}) VALUES ({values});")
                #cursor.execute(f"INSERT INTO Napoje (id_napoje,id_kino, nazwa, cena, ilosc) VALUES (1,1,'sok', 5.50, 30);")
    except (Exception, psycopg2.Error) as error:
        print ("Error while fetching data from PostgreSQL", error)
    finally:
        conn.close()
        print("conn closed")

def Forms_tuple():
    Forms = {
        "Napoje":napoje(),
        "Przekaski":przekaski(),
        # "wizyta":wizyta(),
        # "wizytator":wizytator(),
        # "wyrok":wyrok(),
        # "wyrok_wieznia":wyrok_wieznia(),
        # "wiezien":wiezien(),
        # "praca_wieznia":praca_wieznia(),
        # "praca":praca(),
        # "cela":cela(),
        # "blok":blok(),
        # "pomieszczenie":pomieszczenie(),
        # "pracownik":pracownik(),
        # "zmiana":(),
        # "zawod":zawod(),
    }
    return Forms

def handling_forms(form, form_name):
    if form_name == "wizyta":
        tmp = select_all("termin")
        form.id_termin.choices= [(row[0],f"id: {row[0]} ; data: {row[1]}") for row in tmp]
        tmp = select_all("wiezien")
        form.id_wiezien.choices= [(row[0],f"id: {row[0]} ; imie: {row[1]}; nazwisko: {row[2]}") for row in tmp]
        tmp = select_all("wizytator")
        form.id_wizytator.choices= [(row[0],f"id: {row[0]} ; imie:{row[1]}; nazwisko: {row[2]}") for row in tmp]
    
    if form_name == "wykroczenie":
        tmp = select_all("wiezien")
        form.id_wiezien.choices= [(row[0],f"{row[1]} {row[2]}") for row in tmp]

    if form_name == "Napoje":
        tmp = select_all("Kino")
        form.id_kino.choices = [(row[0], f"{row[1]} {row[2]}") for row in tmp]

    if form_name == "Przekąski":
        tmp = select_all("Kino")
        form.id_kino.choices = [(row[0], f"{row[1]} {row[2]}") for row in tmp]

    if form_name == "wyrok_wieznia":
        tmp = select_all("wyrok")
        form.id_wyrok.choices= [(row[0],f"id: {row[0]} ; nazwa: {row[1]}") for row in tmp]
        tmp = select_all("wiezien")
        form.id_wiezien.choices= [(row[0],f"id: {row[0]} ; imie: {row[1]}; nazwisko: {row[2]}") for row in tmp]

    if form_name == "wiezien":
        tmp = select_all("cela")
        form.id_cela.choices= [(row[0],f"id: {row[0]} ; id bloku:{row[1]}; numer: {row[2]}") for row in tmp]

    if form_name == "praca_wieznia":
        tmp = select_all("wiezien")
        form.id_wiezien.choices= [(row[0],f"id: {row[0]} ; imie: {row[1]}; nazwisko: {row[2]}") for row in tmp]
        tmp = select_all("praca")
        form.id_praca.choices= [(row[0],f"id: {row[0]} ; opis: {row[1]}") for row in tmp]
    
    if form_name == "cela":
        tmp = select_all("blok")
        form.id_blok.choices= [(row[0],f"id: {row[0]} ; id bloku: {row[1]}") for row in tmp]

    if form_name == "pomieszczenie":
        tmp = select_all("blok")
        form.id_blok.choices= [(row[0],f"id: {row[0]} ; nazwa bloku: {row[1]}") for row in tmp]
    
    if form_name == "pracownik":
        tmp = select_all("zawod")
        form.id_zawod.choices= [(row[0],f"id: {row[0]} ; opis: {row[1]}") for row in tmp]
        tmp = select_all("zmiana")
        form.id_zmiana.choices= [(row[0],f"id: {row[0]} ; nazwa: {row[1]}") for row in tmp]
        tmp = select_all("pomieszczenie")
        form.id_pomieszczenie.choices = [(0,'brak')]+[(row[0],f"id: {row[0]} ; id bloku: {row[1]}; numer: {row[2]}") for row in tmp]
        