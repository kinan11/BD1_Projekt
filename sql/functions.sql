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



