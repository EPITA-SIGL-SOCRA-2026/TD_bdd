USE so_close;

CREATE TABLE IF NOT EXISTS cultures_par_jardin (
  jardin_id INT,
  annee INT,
  mois INT,
  plante TEXT,
  quantite INT,
  saison TEXT,
  PRIMARY KEY ((jardin_id), annee, mois, plante)
);

CREATE TABLE IF NOT EXISTS cultures_par_plante (
  jardin_id INT,
  plante TEXT,
  annee INT,
  mois INT,
  quantite INT,
  saison TEXT,
  PRIMARY KEY ((jardin_id, plante), annee, mois)
);

