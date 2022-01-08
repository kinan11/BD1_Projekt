CREATE OR REPLACE FUNCTION validate_litery()
   RETURNS TRIGGER
    LANGUAGE plpgsql
    AS $$
    BEGIN
        NEW.nazwa :=initcap(NEW.nazwa);
    RETURN NEW;                                                          
    END;
    $$;
    
CREATE TRIGGER person_norma
    BEFORE INSERT OR UPDATE ON Napoje
    FOR EACH ROW EXECUTE PROCEDURE validate_litery();