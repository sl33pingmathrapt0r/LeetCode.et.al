SELECT * FROM Patients
WHERE conditions REGEXP '\\bDIAB1' ;
-- -'\b' represents a non-word character, e.g. ' '
-- -'\' is used to escape another '\'
