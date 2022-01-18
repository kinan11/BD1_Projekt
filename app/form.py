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

class Napoje(FlaskForm):
    id_kino = SelectField("Kino",coerce=int, validators=[InputRequired()])
    nazwa = StringField("Nazwa", validators=[InputRequired()])
    cena = DecimalField("Cena", validators=[InputRequired()])
    ilosc = IntegerField("Ilość", validators=[InputRequired()])
    submit = SubmitField("Dodaj")

class Przekąski(FlaskForm):
    id_kino = SelectField("Kino",coerce=int, validators=[InputRequired()])
    nazwa = StringField("Nazwa", validators=[InputRequired()])
    cena = DecimalField("Cena", validators=[InputRequired()])
    ilosc = IntegerField("Ilość", validators=[InputRequired()])
    submit = SubmitField("Dodaj")

class Reżyser(FlaskForm):
    imie = StringField("Imię", validators=[InputRequired()])
    nazwisko = StringField("Nazwisko", validators=[InputRequired()])
    submit = SubmitField("Dodaj")

class Sala(FlaskForm):
    id_kino = SelectField("Kino",coerce=int, validators=[InputRequired()])
    liczba_miejsc = IntegerField("Liczba miejsc", validators=[InputRequired()])
    submit = SubmitField("Dodaj")

class Film(FlaskForm):
    imie_rez = StringField("Imię reżysera", validators=[InputRequired()])
    Nazwisko_rez = StringField("Nazwisko reżysera", validators=[InputRequired()])
    tytul = StringField("Tytuł", validators=[InputRequired()])
    rok = IntegerField("Rok produkcji", validators=[InputRequired()])
    czas = IntegerField("Czas trwania (w minutach)", validators=[InputRequired()])
    ocena = DecimalField("Ocena (w skali od 0 do 10)", validators=[InputRequired()])
    submit = SubmitField("Dodaj")

class Kino(FlaskForm):
    nazwa = StringField("Nazwa kina", validators=[InputRequired()])
    miasto = StringField("Miasto", validators=[InputRequired()])
    submit = SubmitField("Dodaj")

class Seans(FlaskForm):
    id_kino = SelectField("Kino", coerce=int, validators=[InputRequired()])
    id_sala = IntegerField("Numer sali", validators=[InputRequired()])
    id_film = SelectField("Film", coerce=int, validators=[InputRequired()])
    data = DateField("data rozpoczecia (YYYY-MM-DD)", validators=[InputRequired()])
    godzina = TimeField("godzina rozpoczecia (HH:MM)", validators=[InputRequired()])
    cena = DecimalField("Cena biletu", validators=[InputRequired()])
    submit = SubmitField("Dodaj")

class Rejestracja(FlaskForm):
    login = StringField("Login", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired()])
    haslo = PasswordField("Hasło", validators=[InputRequired()])
    submit = SubmitField("Zarejestruj się")

class Rezerwacja(FlaskForm):
    id_seans = SelectField("Seans", coerce=int, validators=[InputRequired()])
    id_bilet = SelectField("Rodzaj biletu", coerce=int, validators=[InputRequired()])
    id_napoje = SelectField("Napój", coerce=int, validators=[InputRequired()])
    id_przekaski = SelectField("Przekąska", coerce=int, validators=[InputRequired()])
    submit = SubmitField("Rezerwuj")

class select_table(FlaskForm):
    nazwa = SelectField("Wybierz co chcesz dodać:",coerce=str)
    submit = SubmitField("wybierz")