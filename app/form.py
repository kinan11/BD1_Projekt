from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    BooleanField,
    IntegerField,
    DateField,
    SelectField, DecimalField, TimeField, PasswordField
)
from wtforms.validators import InputRequired

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

class rezyser(FlaskForm):
    imie = StringField("Imię", validators=[InputRequired()])
    nazwisko = StringField("Nazwisko", validators=[InputRequired()])
    submit = SubmitField("Dodaj")

class sala(FlaskForm):
    id_kino = SelectField("Kino",coerce=int, validators=[InputRequired()])
    liczba_miejsc = IntegerField("Liczba miejsc", validators=[InputRequired()])
    submit = SubmitField("Dodaj")

class film(FlaskForm):
    imie_rez = StringField("Imię reżysera", validators=[InputRequired()])
    Nazwisko_rez = StringField("Nazwisko reżysera", validators=[InputRequired()])
    tytul = StringField("Tytuł", validators=[InputRequired()])
    rok = IntegerField("Rok produkcji", validators=[InputRequired()])
    czas = IntegerField("Czas trwania (w minutach)", validators=[InputRequired()])
    ocena = DecimalField("Ocena (w skali od 0 do 10)", validators=[InputRequired()])
    submit = SubmitField("Dodaj")

class kino(FlaskForm):
    nazwa = StringField("Nazwa kina", validators=[InputRequired()])
    miasto = StringField("Miasto", validators=[InputRequired()])
    submit = SubmitField("Dodaj")

class seans(FlaskForm):
    id_kino = SelectField("Kino", coerce=int, validators=[InputRequired()])
    id_sala = IntegerField("Numer sali", validators=[InputRequired()])
    id_film = SelectField("Film", coerce=int, validators=[InputRequired()])
    data = DateField("data rozpoczecia (YYYY-MM-DD)", validators=[InputRequired()])
    godzina = TimeField("godzina rozpoczecia (HH-MM)", validators=[InputRequired()])
    cena = DecimalField("Cena biletu", validators=[InputRequired()])
    submit = SubmitField("Dodaj")

class rejestracja(FlaskForm):
    login = StringField("Login", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired()])
    haslo = PasswordField("Hasło", validators=[InputRequired()])
    submit = SubmitField("Zarejestruj się")

class rezerwacja(FlaskForm):
    id_osoba = SelectField("Login", coerce=int, validators=[InputRequired()])
    id_seans = SelectField("Seans", coerce=int, validators=[InputRequired()])
    id_bilet = SelectField("Rodzaj biletu", coerce=int, validators=[InputRequired()])
    id_napoje = SelectField("Napój", coerce=int, validators=[InputRequired()])
    id_przekaski = SelectField("Przekąska", coerce=int, validators=[InputRequired()])
    submit = SubmitField("Rezerwuj")

class select_table(FlaskForm):
    nazwa = SelectField("nazwa tabeli",coerce=str)
    submit = SubmitField("wybierz")