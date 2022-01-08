
CREATE TABLE public.Bilet (
                id_bilet INTEGER NOT NULL,
                opis VARCHAR NOT NULL,
                CONSTRAINT id_bilet PRIMARY KEY (id_bilet)
);


CREATE TABLE public.Osoba (
                id_osoba INTEGER NOT NULL,
                login VARCHAR NOT NULL,
                email VARCHAR NOT NULL,
                haslo VARCHAR NOT NULL,
                CONSTRAINT id_osoba PRIMARY KEY (id_osoba)
);


CREATE TABLE public.Rezyser (
                id_rezyser INTEGER NOT NULL,
                imie VARCHAR NOT NULL,
                nazwisko VARCHAR NOT NULL,
                CONSTRAINT id_rezyser PRIMARY KEY (id_rezyser)
);


CREATE TABLE public.Film (
                id_film INTEGER NOT NULL,
                id_rezyser INTEGER NOT NULL,
                tytul VARCHAR NOT NULL,
                ocena DOUBLE PRECISION NOT NULL,
                CONSTRAINT id_film PRIMARY KEY (id_film)
);


CREATE TABLE public.Kino (
                id_kino INTEGER NOT NULL,
                nazwa VARCHAR NOT NULL,
                miasto VARCHAR NOT NULL,
                CONSTRAINT id_kino PRIMARY KEY (id_kino)
);


CREATE TABLE public.Napoje (
                id_napoje INTEGER NOT NULL,
                id_kino INTEGER NOT NULL,
                nazwa VARCHAR NOT NULL,
                cena DOUBLE PRECISION NOT NULL,
                ilosc INTEGER NOT NULL,
                CONSTRAINT id_napoje PRIMARY KEY (id_napoje)
);


CREATE TABLE public.Przekaski (
                id_przekaski INTEGER NOT NULL,
                id_kino INTEGER NOT NULL,
                nazwa VARCHAR NOT NULL,
                cena DOUBLE PRECISION NOT NULL,
                ilosc INTEGER NOT NULL,
                CONSTRAINT id_przekaski PRIMARY KEY (id_przekaski)
);


CREATE TABLE public.Sala (
                id_sala INTEGER NOT NULL,
                id_kino INTEGER NOT NULL,
                numer INTEGER NOT NULL,
                liczba_miejsc INTEGER NOT NULL,
                CONSTRAINT id_sala PRIMARY KEY (id_sala)
);


CREATE TABLE public.Seans (
                id_seans INTEGER NOT NULL,
                id_film INTEGER NOT NULL,
                id_sala INTEGER NOT NULL,
                id_kino INTEGER NOT NULL,
                data DATE NOT NULL,
                godzina TIME NOT NULL,
                cena DOUBLE PRECISION NOT NULL,
                liczba_miejsc INTEGER NOT NULL,
                CONSTRAINT id_seans PRIMARY KEY (id_seans)
);



CREATE TABLE public.Rezerwacja (
                id_rezerwacja INTEGER NOT NULL,
                id_napoje INTEGER NOT NULL,
                id_przekaski INTEGER NOT NULL,
                id_osoba INTEGER NOT NULL,
                id_seans INTEGER NOT NULL,
                id_bilet INTEGER NOT NULL,
                CONSTRAINT id_rezerwacja PRIMARY KEY (id_rezerwacja)
);


ALTER TABLE public.Rezerwacja ADD CONSTRAINT bilet_rezerwacja_fk
FOREIGN KEY (id_bilet)
REFERENCES public.Bilet (id_bilet)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.Rezerwacja ADD CONSTRAINT osoba_rezerwacja_fk
FOREIGN KEY (id_osoba)
REFERENCES public.Osoba (id_osoba)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.Film ADD CONSTRAINT id_film_film_fk
FOREIGN KEY (id_rezyser)
REFERENCES public.Rezyser (id_rezyser)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.Seans ADD CONSTRAINT film_seans_fk
FOREIGN KEY (id_film)
REFERENCES public.Film (id_film)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.Sala ADD CONSTRAINT kino_sala_fk
FOREIGN KEY (id_kino)
REFERENCES public.Kino (id_kino)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.Przekaski ADD CONSTRAINT kino_przekaski_fk
FOREIGN KEY (id_kino)
REFERENCES public.Kino (id_kino)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.Napoje ADD CONSTRAINT kino_napoje_fk
FOREIGN KEY (id_kino)
REFERENCES public.Kino (id_kino)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.Seans ADD CONSTRAINT kino_seans_fk
FOREIGN KEY (id_kino)
REFERENCES public.Kino (id_kino)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.Rezerwacja ADD CONSTRAINT napoje_rezerwacja_fk
FOREIGN KEY (id_napoje)
REFERENCES public.Napoje (id_napoje)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.Rezerwacja ADD CONSTRAINT przekaski_rezerwacja_fk
FOREIGN KEY (id_przekaski)
REFERENCES public.Przekaski (id_przekaski)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.Seans ADD CONSTRAINT sala_seans_fk
FOREIGN KEY (id_sala)
REFERENCES public.Sala (id_sala)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.Rezerwacja ADD CONSTRAINT seans_rezerwacja_fk
FOREIGN KEY (id_seans)
REFERENCES public.Seans (id_seans)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;
