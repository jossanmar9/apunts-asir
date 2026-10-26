-- Base de dades d'exemple dels apunts: un institut
-- Ús:  createdb institut  &&  psql -d institut -f institut.sql

DROP TABLE IF EXISTS matricules, moduls, alumnes, professors, cicles CASCADE;

CREATE TABLE cicles (
    codi        VARCHAR(5)   PRIMARY KEY,
    nom         VARCHAR(100) NOT NULL,
    grau        VARCHAR(10)  NOT NULL CHECK (grau IN ('mitja', 'superior'))
);

CREATE TABLE professors (
    id          SERIAL       PRIMARY KEY,
    nom         VARCHAR(50)  NOT NULL,
    cognoms     VARCHAR(100) NOT NULL,
    correu      VARCHAR(100) UNIQUE,
    data_alta   DATE         NOT NULL DEFAULT CURRENT_DATE
);

CREATE TABLE alumnes (
    id          SERIAL       PRIMARY KEY,
    nom         VARCHAR(50)  NOT NULL,
    cognoms     VARCHAR(100) NOT NULL,
    data_naix   DATE,
    poblacio    VARCHAR(50),
    cicle       VARCHAR(5)   REFERENCES cicles(codi)
);

CREATE TABLE moduls (
    codi        VARCHAR(6)   PRIMARY KEY,
    nom         VARCHAR(100) NOT NULL,
    hores       INTEGER      NOT NULL CHECK (hores > 0),
    curs        SMALLINT     NOT NULL CHECK (curs IN (1, 2)),
    cicle       VARCHAR(5)   NOT NULL REFERENCES cicles(codi),
    professor   INTEGER      REFERENCES professors(id)
);

CREATE TABLE matricules (
    alumne      INTEGER      REFERENCES alumnes(id) ON DELETE CASCADE,
    modul       VARCHAR(6)   REFERENCES moduls(codi),
    nota        NUMERIC(4,2) CHECK (nota BETWEEN 0 AND 10),
    PRIMARY KEY (alumne, modul)
);

INSERT INTO cicles VALUES
    ('SMX',  'Sistemes microinformàtics i xarxes',           'mitja'),
    ('ASIR', 'Administració de sistemes informàtics en xarxa', 'superior'),
    ('DAW',  'Desenvolupament d''aplicacions web',             'superior');

INSERT INTO professors (nom, cognoms, correu, data_alta) VALUES
    ('Marta',  'Llorens Soler',   'mllorens@institut.edu', '2015-09-01'),
    ('Jordi',  'Ferrer Gil',      'jferrer@institut.edu',  '2019-09-01'),
    ('Carme',  'Ribes Albert',    'cribes@institut.edu',   '2021-09-01'),
    ('Vicent', 'Mas Peris',       NULL,                    '2024-09-01');

INSERT INTO alumnes (nom, cognoms, data_naix, poblacio, cicle) VALUES
    ('Ana',    'Puig Vidal',     '2004-03-12', 'Castelló',  'ASIR'),
    ('Pep',    'Roig Serra',     '2003-11-02', 'Vila-real', 'ASIR'),
    ('Laura',  'Pons Ferrer',    '2005-06-25', 'Castelló',  'ASIR'),
    ('Marc',   'Sales Bou',      '2002-01-30', 'Borriana',  'DAW'),
    ('Núria',  'Climent Mas',    '2006-09-14', 'Onda',      'SMX'),
    ('Toni',   'Gil Amat',       '2004-12-01', 'Vila-real', 'DAW'),
    ('Sara',   'Beltran Ros',    NULL,         'Castelló',  NULL);

INSERT INTO moduls VALUES
    ('ISO',   'Implantació de sistemes operatius',          224, 1, 'ASIR', 1),
    ('PAR',   'Planificació i administració de xarxes',     192, 1, 'ASIR', 2),
    ('GBD',   'Gestió de bases de dades',                   160, 1, 'ASIR', 3),
    ('ASO',   'Administració de sistemes operatius',        120, 2, 'ASIR', 1),
    ('IAW',   'Implantació d''aplicacions web',             100, 2, 'ASIR', 3),
    ('PROG',  'Programació',                                256, 1, 'DAW',  NULL),
    ('XARX',  'Xarxes locals',                              224, 1, 'SMX',  2);

INSERT INTO matricules VALUES
    (1, 'ISO', 8.5), (1, 'PAR', 7),   (1, 'GBD', 9),
    (2, 'ISO', 4),   (2, 'PAR', 5.5), (2, 'GBD', 6),
    (3, 'ISO', 9.5), (3, 'PAR', 8),   (3, 'GBD', NULL),
    (4, 'PROG', 7.5),
    (5, 'XARX', 3),
    (6, 'PROG', 5);
