INSERT INTO Bilet (id_bilet, opis)
VALUES (1,'ulgowy'), (2, 'normalny');

INSERT INTO Kino (id_kino, nazwa, miasto)
VALUES (1,'Helios', 'Warszawa'), (2, 'Helios', 'Kraków'), (3, 'Helios', 'Wrocław'), (4, 'Multikino', 'Warszawa'), (5, 'Multikino', 'Kraków');

INSERT INTO Sala (id_sala, id_kino, numer, liczba_miejsc)
VALUES (1, 1, 1, 30), (2, 1, 2, 10), (3, 1, 3, 25), (4, 2, 1, 15), (5, 2, 2, 30), (6, 3, 1, 40), (7, 3, 2, 60), (8, 3, 3, 20), (9, 4, 1, 70), (10, 4, 2, 30), (11, 4, 3, 35), (12, 4, 4, 40), (13, 5, 1, 40), (14, 5, 2, 50), (15, 5, 3, 20);

INSERT INTO Przekaski (id_kino, nazwa, cena, ilosc)
VALUES (1, 'Popcorn S',10.50, 30), (2, 'Popcorn S',10.50, 30), (3, 'Popcorn S',10.50, 30),
( 1, 'Popcorn M',13.50, 30), ( 2, 'Popcorn M',13.50, 30), (3, 'Popcorn M',13.50, 30),
( 1, 'Popcorn L',15.00, 30), ( 2, 'Popcorn L',15.00, 30), (3, 'Popcorn L',15.00, 30),
( 1, 'Popcorn S',11.00, 30), ( 2, 'Popcorn S',11.00, 30),
( 1, 'Popcorn M',14.00, 30), ( 2, 'Popcorn M',14.00, 30),
( 1, 'Popcorn L',16.00, 30), ( 2, 'Popcorn L',16.00, 30),
( 1, 'Natchosy S',10.50, 35), (2, 'Natchosy S',10.50, 35), ( 3, 'Natchosy S',10.50, 35),
( 1, 'Natchosy M',13.50, 30), (2, 'Natchosy M',13.50, 30), ( 3, 'Natchosy M',13.50, 30),
( 1, 'Natchosy L',15.00, 25), ( 2, 'Natchosy L',15.00, 25), ( 3, 'Natchosy L',15.00, 25),
( 1, 'Natchosy S',11.00, 35), ( 2, 'Natchosy S',11.00, 35),
( 1, 'Natchosy M',14.00, 30), ( 2, 'Natchosy M',14.00, 30),
( 1, 'Natchosy L',16.00, 25), ( 2, 'Natchosy L',16.00, 25);

INSERT INTO Napoje (id_kino, nazwa, cena, ilosc)
VALUES (1, 'Cola S',5.00, 30), (2, 'Cola S',5.00, 30), (3, 'Cola S',5.00, 30),
(1, 'Cola M',6.50, 30), (2, 'Cola M',6.50, 30), (3, 'Cola M',6.50, 30),
(1, 'Cola L',7.00, 30), (2, 'Cola L',7.00, 30), (3, 'Cola L',7.00, 30),
(1, 'Cola S',5.00, 30), (2, 'Cola S',5.00, 30),
(1, 'Cola M',7.00, 30), (2, 'Cola M',7.00, 30),
(1, 'Cola L',7.50, 30), (2, 'Cola L',7.50, 30),
(1, 'Fanta S',5.00, 35), (2, 'Fanta S',5.00, 35), (3, 'Fanta S',5.00 ,35),
(1, 'Fanta M',6.50, 30), (2, 'Fanta M',6.50, 30), (3, 'Fanta M',6.50 ,30),
(1, 'Fanta L',7.00, 25), ( 2, 'Fanta L',7.00, 25), ( 3, 'Fanta L',7.00, 25),
(1, 'Fanta S',5.00, 35), ( 2, 'Fanta S',5.00, 35),
( 1, 'Fanta M',7.00, 30), ( 2, 'Fanta M',7.00, 30),
( 1, 'Fanta L',7.50, 25), ( 2, 'Fanta L',7.50 ,25),
( 1, 'Sprite S',5.00, 35), ( 2, 'Sprite S',5.00, 35), ( 3, 'Sprite S',5.00, 35),
( 1, 'Sprite M',6.50, 30), ( 2, 'Sprite M',6.50, 30), ( 3, 'Sprite M',6.50, 30),
( 1, 'Sprite L',7.00, 25), ( 2, 'Sprite L',7.00, 25), ( 3, 'Sprite L',7.00, 25),
( 1, 'Sprite S',5.00, 35), ( 2, 'Sprite S',5.00, 35),
( 1, 'Sprite M',7.00, 30), ( 2, 'Sprite M',7.00, 30),
( 1, 'Sprite L',7.50, 25), ( 2, 'Sprite L',7.50, 25);

INSERT INTO Osoba (id_osoba,login, email, haslo)
VALUES (1, 'uzytkownik1', 'usr@onet.pl', 'abc123'),
(2,'usr2', 'usr@gmail.com', '123abc');

INSERT INTO Film (id_rezyser, tytul, ocena ,rok, czas)
VALUES (1, 'Spider-Man: Bez drogi do domu', 8.2, 2021, 148),
(2, 'Matrix Zmartwychwstania"', 5.1, 2021, 148),
(3, 'W 80 dni dookoła świata', 4.2, 2021, 82),
(4, 'Dom Gucci', 6.7, 2021, 157),
(4, 'Ostatni pojedynek', 7.4, 2021, 152),
(4, 'Prometeusz', 6.3, 2012, 124),
(1, 'Spider-Man: Homecoming', 7.2,2017, 148),
(1, 'Spider-Man: Daleko od domu', 7.3, 2019, 130),
(2, 'Jupiter: Intronizacja', 5.3, 2015, 127),
(2, 'Atlas chmur', 7.1, 2012, 172),
(3, 'Banana', 7.3, 2010, 4),
(2, 'Speed Racer', 7.1, 2008, 135);


INSERT INTO Rezyser (imie, nazwisko)
VALUES ('Jon', 'Watts'),
('Lana', 'Wachowski'),
('Samuel', 'Tourneux'),
('Ridley', 'Scott');

INSERT INTO Seans (id_seans, id_film, id_sala, id_kino, data, godzina, cena, liczba_miejsc)
VALUES (1,1,2,1, '2021-02-01', '17:00:00', 20, 10),
(2,2,1,1,'2021-02-03','17:30:00', 20, 30),
(3, 1,5,2,'2021-02-01','15:00:00', 23, 30);

