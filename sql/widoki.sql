----------- LISTA FILMÓW ------
CREATE OR REPLACE VIEW wszystkie_filmy AS SELECT tytul, imie||' '||nazwisko, rok, czas, ocena, COUNT (id_seans) FROM Film LEFT JOIN seans ON film.id_film  = seans.id_film  JOIN Rezyser ON Film.id_rezyser=Rezyser.id_rezyser GROUP BY tytul, rok, imie, nazwisko, czas, ocena;

------ LISTA KIN ------
CREATE OR REPLACE VIEW lista_kin AS (WITH sum_sala AS ( SELECT Kino.id_kino, COUNT (id_sala) AS suma FROM Kino JOIN Sala ON Kino.id_kino=Sala.id_kino GROUP BY Kino.id_kino) SELECT nazwa, miasto ,suma, COUNT (seans.id_kino) FROM sum_sala JOIN Kino ON Kino.id_kino = sum_sala.id_kino LEFT JOIN Seans ON Kino.id_kino  = Seans.id_kino GROUP BY nazwa, miasto, suma);

---- LISTA KIN DO FORMULARZY ---------
CREATE OR REPLACE VIEW form_kino AS SELECT id_kino, nazwa,miasto FROM Kino;

-----LISTA PRZEKĄSEK----
CREATE OR REPLACE FUNCTION bufet_przekaski(id INTEGER)
RETURNS TABLE(nazwa VARCHAR, cena DOUBLE PRECISION)
LANGUAGE plpgsql AS $$
BEGIN
RETURN QUERY SELECT Przekaski.nazwa, Przekaski.cena FROM Przekaski WHERE id_kino = id ORDER BY Przekaski.nazwa;
END;
$$;

-----LISTA NAPOI ---
CREATE OR REPLACE FUNCTION bufet_napoje(id INTEGER)
RETURNS TABLE(nazwa VARCHAR, cena DOUBLE PRECISION)
LANGUAGE plpgsql AS $$
BEGIN
    RETURN QUERY SELECT Napoje.nazwa, Napoje.cena FROM Napoje WHERE id_kino = id ORDER BY Napoje.nazwa;
END;
$$;

----REPERTUAR----
CREATE OR REPLACE FUNCTION repertuar(id INTEGER)
RETURNS TABLE(tytul VARCHAR, data DATE, godzina TIME)
LANGUAGE plpgsql AS $$
BEGIN
    RETURN QUERY SELECT Film.tytul, Seans.data, Seans.godzina FROM Seans JOIN Film ON Film.id_film = Seans.id_film WHERE Seans.id_kino= id ORDER BY Seans.data, Seans.godzina;
END;
$$;

----LISTA REZERWACJI-----
CREATE OR REPLACE FUNCTION bilety(id INTEGER)
RETURNS TABLE(tytul VARCHAR, nazwa TEXT, data DATE, godzina TIME, przekaski VARCHAR, napoje VARCHAR, opis VARCHAR, cena DOUBLE PRECISION)
LANGUAGE plpgsql AS $$
BEGIN
   RETURN QUERY WITH przyg AS(SELECT Film.tytul,Kino.nazwa||' '||Kino.miasto AS kino_nazwa,  Seans.data, Seans.godzina, rezerwacja.id_przekaski, rezerwacja.id_napoje, Bilet.opis, rezerwacja.cena FROM Rezerwacja JOIN Seans ON Rezerwacja.id_seans = Seans.id_seans JOIN Film ON Seans.id_film = Film.id_film JOIN Kino ON Seans.id_kino = Kino.id_kino JOIN bilet ON Rezerwacja.id_bilet = Bilet.id_bilet WHERE id_osoba = id) SELECT przyg.tytul, kino_nazwa, przyg.data, przyg.godzina, Przekaski.nazwa, Napoje.nazwa, przyg.opis, przyg.cena FROM przyg LEFT JOIN PRZEKASKI ON przyg.id_przekaski = Przekaski.id_przekaski LEFT JOIN Napoje ON  przyg.id_napoje = napoje.id_napoje;
END;
$$;

-------LISTA SEANSÓW DO REZERWACJI --------
CREATE OR REPLACE FUNCTION seans(id INTEGER)
RETURNS TABLE(id_s BIGINT, tytul VARCHAR, dt DATE, godz TIME, c DOUBLE PRECISION)
LANGUAGE plpgsql AS $$
BEGIN
    RETURN QUERY Select Seans.id_seans, Film.tytul, Seans.data, Seans.godzina, Seans.cena FROM Seans JOIN Film ON film.id_film = Seans.id_film WHERE id_kino = id;
END;
$$;

-------LISTA NAPOI DLA KINA -----
CREATE OR REPLACE FUNCTION rez_napoje(id INTEGER)
RETURNS TABLE(id_nap BIGINT, nazwa VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    RETURN QUERY SELECT Napoje.id_napoje, Napoje.nazwa FROM Napoje WHERE id_kino = id;
END;
$$;

------LISTA PRZEKĄSEK DLA KINA-----
CREATE OR REPLACE FUNCTION rez_przekaski(id INTEGER)
RETURNS TABLE(id_prz BIGINT, nazwa VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    RETURN QUERY SELECT Przekaski.id_przekaski, Przekaski.nazwa FROM Przekaski WHERE id_kino = id;
END;
$$;

----RANKING REŻYSERÓW--------
CREATE OR REPLACE VIEW rank_rezyser AS SELECT imie, nazwisko, COUNT(*), AVG(ocena) FROM Rezyser JOIN Film ON Rezyser.id_rezyser = Film.id_rezyser GROUP BY imie, nazwisko;



-----------------------------------------
SELECT Film.tytul,Kino.nazwa||' '||Kino.miasto,  Seans.data, Seans.godzina, przekaski.nazwa, napoje.nazwa, Bilet.opis, rezerwacja.cena FROM Rezerwacja JOIN Seans ON Rezerwacja.id_seans = Seans.id_seans JOIN Film ON Seans.id_film = Film.id_film JOIN Kino ON Seans.id_kino = Kino.id_kino JOIN bilet ON Rezerwacja.id_bilet = Bilet.id_bilet JOIN Napoje ON Kino.id_kino = Napoje.id_kino JOIN Przekaski ON Kino.id_kino = Przekaski.id_kino  WHERE id_osoba = 1 AND ((Rezerwacja.id_przekaski = Przekaski.id_przekaski OR Rezerwacja.id_przekaski is null) AND (Rezerwacja.id_napoje = Napoje.id_napoje OR Rezerwacja.id_napoje is null)) AND Rezerwacja.cena is not null;