CREATE OR REPLACE FUNCTION validate_litery()
   RETURNS TRIGGER
    LANGUAGE plpgsql
    AS $$
    BEGIN
        NEW.nazwa :=initcap(NEW.nazwa);
        IF  NEW.cena<0
            THEN RAISE EXCEPTION 'niepoprawna cena (<0)';
        END IF;
        IF  NEW.ilosc<0
            THEN RAISE EXCEPTION 'niepoprawna ilość (<0)';
        END IF;
    RETURN NEW;                                                          
    END;
    $$;
    
CREATE TRIGGER litery_napoje
    BEFORE INSERT OR UPDATE ON Napoje
    FOR EACH ROW EXECUTE PROCEDURE validate_litery();

CREATE TRIGGER litery_przekaski
    BEFORE INSERT OR UPDATE ON Przekaski
    FOR EACH ROW EXECUTE PROCEDURE validate_litery();


CREATE OR REPLACE FUNCTION sprawdz_film()
RETURNS TRIGGER AS
$$
BEGIN
    IF  NEW.rok<=0
        THEN RAISE EXCEPTION 'niepoprawny rok (musi być dodatni)';
    END IF;
    IF  NEW.czas<=0
        THEN RAISE EXCEPTION 'niepoprawny czas trwania (<0)';
    END IF;
    IF  NEW.ocena<0
        THEN RAISE EXCEPTION 'niepoprawna wratość oceny (<0)';
    END IF;
    IF  NEW.ocena>10
        THEN RAISE EXCEPTION 'niepoprawna wratość oceny (>10)';
    END IF;
RETURN NEW;
END
$$
LANGUAGE plpgsql;

CREATE TRIGGER tr_sprawdz_film
BEFORE INSERT OR UPDATE ON Film
FOR EACH ROW EXECUTE PROCEDURE sprawdz_film();

CREATE OR REPLACE FUNCTION sprawdz_rezyser ( rez_imie VARCHAR, rez_nazwisko VARCHAR)
RETURNS INTEGER AS
$$
DECLARE
    id INTEGER;
BEGIN
    id= (SELECT id_rezyser FROM Rezyser WHERE imie= rez_imie AND nazwisko = rez_nazwisko);
    IF id IS NOT NULL
        THEN RETURN id;
    ELSE
        INSERT INTO Rezyser (imie, nazwisko) VALUES (rez_imie, rez_nazwisko);
        id = (SELECT MAX(id_rezyser) FROM Rezyser);
    END IF;
    RETURN id;
END;
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION dodaj_sale()
RETURNS TRIGGER AS
$$
BEGIN
    IF  NEW.liczba_miejsc<=0
        THEN RAISE EXCEPTION 'niepoprawna liczba miejsc (musi być dodatnia)';
       END IF;
RETURN NEW;
END
$$
LANGUAGE plpgsql;

CREATE TRIGGER tr_dodaj_sale
BEFORE INSERT OR UPDATE ON Sala
FOR EACH ROW EXECUTE PROCEDURE dodaj_sale();

CREATE OR REPLACE FUNCTION spr_sale(kino INTEGER)
RETURNS INTEGER AS
$$
DECLARE
    id INTEGER;
BEGIN
    id= (SELECT (COUNT(id_kino)+1) FROM sala WHERE id_kino = kino);
RETURN id;
END
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION dodaj_kino()
RETURNS TRIGGER AS
$$
BEGIN
    INSERT INTO Sala (id_kino, numer, liczba_miejsc) VALUES (NEW.id_kino, 1, 30);
RETURN NEW;
END
$$
LANGUAGE plpgsql;

CREATE TRIGGER tr_dodaj_kino
AFTER INSERT OR UPDATE ON Kino
FOR EACH ROW EXECUTE PROCEDURE dodaj_kino();

CREATE OR REPLACE FUNCTION spr_liczbe_miejsc(kino_id INTEGER, nr_sali INTEGER)
RETURNS INTEGER AS
$$
DECLARE
    liczba INTEGER;
BEGIN
    liczba= (SELECT liczba_miejsc FROM sala WHERE id_kino = kino_id AND numer = nr_sali);
    IF liczba IS NULL
        THEN RAISE EXCEPTION 'nie ma takiej sali';
    END IF;
RETURN liczba;
END
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION dodaj_seans()
RETURNS TRIGGER AS
$$
BEGIN
    NEW.id_sala := (SELECT id_sala FROM Sala WHERE id_kino = NEW.id_kino AND numer = NEW.id_sala);
    IF New.cena <=0
        THEN RAISE EXCEPTION 'niepoprawna cena (musi być dodatnia)';
    END IF;
RETURN NEW;
END
$$
LANGUAGE plpgsql;

CREATE TRIGGER tr_dodaj_seans
BEFORE INSERT OR UPDATE ON Seans
FOR EACH ROW EXECUTE PROCEDURE dodaj_seans();

CREATE OR REPLACE FUNCTION rejestracja()
RETURNS TRIGGER AS
$$
BEGIN
    IF  NEW.email NOT LIKE '%_@__%.__%'
        THEN RAISE EXCEPTION 'Niepoprawny adres e-mail.';
    END IF;
    IF (SELECT id_osoba FROM Osoba WHERE login = NEW.login OR email = NEW.email OR haslo = NEW.haslo)
        THEN RAISE EXCEPTION 'podany login/email/hasło już istnieje';
    END IF;

RETURN NEW;
END
$$
LANGUAGE plpgsql;

CREATE TRIGGER tr_rejestracja
BEFORE INSERT OR UPDATE ON Osoba
FOR EACH ROW EXECUTE PROCEDURE rejestracja();



