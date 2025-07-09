-- Charge les données dans la base de données PostgreSQL
COPY plantes (
    id,
    nom_commun,
    nom_latin,
    port,
    strate,
    rusticite
)
FROM
    '/data/plantes.csv' WITH (
        FORMAT csv,
        HEADER true,
        DELIMITER ',',
        ENCODING 'UTF8'
    );

-- Load jardins
COPY jardins (jardin_id, nom, latitude, longitude)
FROM
    '/data/jardins.csv' WITH (
        FORMAT csv,
        HEADER true,
        DELIMITER ',',
        ENCODING 'UTF8'
    );

-- Load jardiniers
COPY jardiniers (jardinier_id, nom, jardin_id)
FROM
    '/data/jardiniers.csv' WITH (
        FORMAT csv,
        HEADER true,
        DELIMITER ',',
        ENCODING 'UTF8'
    );

-- Load cultures
COPY cultures (jardin_id, plante_id, age)
FROM
    '/data/cultures.csv' WITH (
        FORMAT csv,
        HEADER true,
        DELIMITER ',',
        ENCODING 'UTF8'
    );

-- Load plantes_ensoleillement
COPY plantes_ensoleillement (plante_id, ensoleillement)
FROM
    '/data/plantes_ensoleillement.csv' WITH (
        FORMAT csv,
        HEADER true,
        DELIMITER ',',
        ENCODING 'UTF8'
    );