-- Creer les tables de la base de données
-- plantes id,nom_commun,nom_latin,port,strate,rusticite
CREATE TABLE plantes (
    id INTEGER PRIMARY KEY,
    nom_commun TEXT NOT NULL,
    nom_latin TEXT NOT NULL,
    port TEXT NOT NULL,
    strate TEXT NOT NULL,
    rusticite INTEGER NOT NULL
);

-- jardins jardin_id,nom,latitude,longitude
CREATE TABLE jardins (
    jardin_id INTEGER PRIMARY KEY,
    nom TEXT NOT NULL,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL
);

-- jardiniers jardinier_id,nom,jardin_id
CREATE TABLE jardiniers (
    jardinier_id INTEGER PRIMARY KEY,
    nom TEXT NOT NULL,
    jardin_id INTEGER NOT NULL,
    FOREIGN KEY (jardin_id) REFERENCES jardins(jardin_id)
);

-- cultures jardin_id,plante_id,age
CREATE TABLE cultures (
    jardin_id INTEGER NOT NULL,
    plante_id INTEGER NOT NULL,
    age INTEGER NOT NULL,
    FOREIGN KEY (jardin_id) REFERENCES jardins(jardin_id),
    FOREIGN KEY (plante_id) REFERENCES plantes(id)
);

-- plantes ensoleillement jardin_id,plante_id,ensoleillement
CREATE TABLE plantes_ensoleillement (
    plante_id INTEGER NOT NULL,
    ensoleillement TEXT NOT NULL,
    FOREIGN KEY (plante_id) REFERENCES plantes(id)
);