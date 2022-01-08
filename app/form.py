from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    BooleanField,
    IntegerField,
    DateField,
    SelectField, DecimalField
)
from wtforms.validators import InputRequired

class wykroczenie(FlaskForm):
    id_wiezien = SelectField("id_wiezien",coerce=int, validators=[InputRequired()])
    opis = StringField("Nazwa", validators=[InputRequired()])
    data = DecimalField("Cena", validators=[InputRequired()])
    kara = IntegerField("Ilość", validators=[InputRequired()])
    submit = SubmitField("Dodaj")

class napoje(FlaskForm):
    id_kino = SelectField("Kino",coerce=int, validators=[InputRequired()])
    nazwa = StringField("Nazwa", validators=[InputRequired()])
    cena = DecimalField("Cena", validators=[InputRequired()])
    ilosc = IntegerField("Ilość", validators=[InputRequired()])
    submit = SubmitField("Dodaj")

class przekaski(FlaskForm):
    id_kino = SelectField("Kino",coerce=int, validators=[InputRequired()])
    nazwa = StringField("Nazwa", validators=[InputRequired()])
    cena = DecimalField("Cena", validators=[InputRequired()])
    ilosc = IntegerField("Ilość", validators=[InputRequired()])
    submit = SubmitField("Dodaj")

class termin(FlaskForm):
    data = DateField("data (YYYY-MM-DD)", validators=[InputRequired()])
    submit = SubmitField("Dodaj")

class wizyta(FlaskForm):
    id_termin = SelectField("id_termin",coerce=int, validators=[InputRequired()])
    id_wiezien = SelectField("id_wiezien",coerce=int, validators=[InputRequired()])
    id_wizytator = SelectField("id_wizytator",coerce=int, validators=[InputRequired()])
    submit = SubmitField("Dodaj")


class wizytator(FlaskForm):
    imie = StringField("imię", validators=[InputRequired()])
    nazwisko = StringField("nazwisko", validators=[InputRequired()])
    plec = SelectField("płec", choices = ['mężczyzna', 'kobieta', 'inne'] , validators=[InputRequired()])
    submit = SubmitField("Dodaj")

class wyrok(FlaskForm):
    nazwa = StringField("nazwa", validators=[InputRequired()])
    submit = SubmitField("Dodaj")

class wyrok_wieznia(FlaskForm):
    id_wyrok = SelectField("id_wyrok",coerce=int, validators=[InputRequired()])
    id_wiezien = SelectField("id_wiezien",coerce=int, validators=[InputRequired()])
    submit = SubmitField("Dodaj")

class wiezien(FlaskForm):
    imie = StringField("imię", validators=[InputRequired()])
    nazwisko = StringField("nazwisko", validators=[InputRequired()])
    plec = SelectField("płec", choices = ['mężczyzna', 'kobieta', 'inne'] , validators=[InputRequired()])
    id_cela = SelectField("id_cela",coerce=int, validators=[InputRequired()])
    data_rozpoczecia = DateField("data rozpoczecia (YYYY-MM-DD)", validators=[InputRequired()])
    data_zakonczenia = DateField("data zakonczenia (YYYY-MM-DD)", validators=[InputRequired()])
    submit = SubmitField("Dodaj")

class praca_wieznia(FlaskForm):
    id_wiezien = SelectField("id_wiezien",coerce=int, validators=[InputRequired()])
    id_praca = SelectField("id_praca",coerce=int, validators=[InputRequired()])
    submit = SubmitField("Dodaj")

class praca(FlaskForm):
    opis = StringField("opis", validators=[InputRequired()])
    submit = SubmitField("Dodaj")

class cela(FlaskForm):
    id_blok = SelectField("id_blok",coerce=int, validators=[InputRequired()])
    numer = IntegerField("numer", validators=[InputRequired()])
    submit = SubmitField("Dodaj")

class blok(FlaskForm):
    nazwa = StringField("nazwa", validators=[InputRequired()])
    submit = SubmitField("Dodaj")

class pomieszczenie(FlaskForm):
    id_blok = SelectField("id_blok",coerce=int, validators=[InputRequired()])
    numer = IntegerField("numer", validators=[InputRequired()])
    submit = SubmitField("Dodaj")

class pracownik(FlaskForm):
    imie = StringField("imię", validators=[InputRequired()])
    nazwisko = StringField("nazwisko", validators=[InputRequired()])
    plec = SelectField("płec", choices = ['mężczyzna', 'kobieta', 'inne'] , validators=[InputRequired()])
    id_zawod = SelectField("id_zawod",coerce=int, validators=[InputRequired()])
    id_pomieszczenie = SelectField("id_pomieszczenie",coerce=int)
    id_zmiana = SelectField("id_zmiana",coerce=int, validators=[InputRequired()])
    submit = SubmitField("Dodaj")
    
class zmiana(FlaskForm):
    nazwa = StringField("nazwa", validators=[InputRequired()])
    submit = SubmitField("Dodaj")

class zawod(FlaskForm):
    opis = StringField("opis", validators=[InputRequired()])
    submit = SubmitField("Dodaj")

class select_table(FlaskForm):
    nazwa = SelectField("nazwa tabeli",coerce=str)
    submit = SubmitField("wybierz")
