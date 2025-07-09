# Générateur de données So-Close

Ce script Python permet de générer des données réalistes pour simuler l'activité de jardins comestibles urbains dans le cadre du projet **So-Close**.

---

## 📦 Fichiers générés

- `jardins.csv` : coordonnées et nom des jardins
- `jardiniers.csv` : noms et rattachement à un jardin (1 à 5 par jardin)
- `cultures.csv` : plantes cultivées par jardin avec un âge simulé

Tous les fichiers sont enregistrés dans le dossier `so_close_data/`.

---

## ▶️ Utilisation

### 1. Pré-requis

#### Installez python3

Nous vous conseillons d'installer:

- [Pyenv (github.com/pyenv/pyenv)](https://github.com/pyenv/pyenv) pour gérer vos versions de Python sur vos machines.
- [Pyenv Virtualenv (github.com/pyenv/pyenv-virtualenv) plugin](https://github.com/pyenv/pyenv-virtualenv) pour gérer les environnements virtuels.

Une fois Pyenv installé, vous pouvez installer Python 3.11 avec la commande suivante :

```bash
pyenv install 3.13
```

Vous pouvez ensuite créer un environnement virtuel avec :

```bash
pyenv virtualenv 3.13 so-close
```

Ensuite, activez l'environnement virtuel :

```bash
pyenv activate so-close
```

Vérifiez que vous utilisez bien la bonne version de Python :

```bash
python --version
# devrait afficher Python 3.13.x
```

#### Installez les dépendances

Installez les dépendances nécessaires avec pip :

```bash
# assurez-vous d'être dans l'environnement virtuel
pyenv activate so-close
# installez les dépendances
pip3 install -r requirements.txt
```

### 2. Exécution

#### Génération des données pour PostgreSQL: `generate_so_close_data.py`

Pour générer les données, exécutez le script Python avec les paramètres souhaités. Par exemple, pour créer 10 000 jardins dans un rayon de 50 km autour du centre de Paris :

```bash
python generate_so_close_data.py --nb_jardins 10000 --rayon_km 50
```

Le script va :

- Créer 10 000 jardins dans un rayon de 50 km autour du centre de Paris
- Générer des jardiniers pour chaque jardin
- Attribuer aléatoirement des plantes (entre 10 et 156) avec un âge simulé

#### Génération de données pour MongoDB: `generate_cultures_comments.py`

Pour générer des données pour MongoDB, exécutez le script Python avec les paramètres souhaités. Par exemple, pour créer 1000 documents avec 100 jardins, 156 plantes et 500 jardiniers :

```bash
python generate_cultures_comments.py --nb_jardins 10000 --nb_plantes 156 --nb_jardiniers 500
```

Le script va :

- Créer n \* 10_000 documents de commentaires sur les plantes cultivées (n varie en fonction du nombre de plantes cutlivées dans un jardin)
- Générer des commentaires aléatoires pour chaque plante cultivée
- Enregistrer les données dans un fichier JSON `commentaires.json` dans le dossier `data/`

#### Génération de données pour Cassandra: `generate_cultures_recoltes.py`

Pour générer des données pour Cassandra, exécutez le script Python avec les paramètres souhaités. Par exemple, pour créer 10_000 jardins:

```bash
python generate_cultures_recoltes.py --nb_jardins 10000
```

Le script va :

- Créer un fichier CSV `cultures_recoltes_par_jardin_cassandra.csv` dans le dossier `data/`
- Créer un fichier CSV `cultures_recoltes_par_plante_cassandra.csv` dans le dossier `data/`
- Ces fichiers contiennent les récoltes par jardin et par plante au cours de mois pour 3 années

#### Génération et insertion de données pour Neo4j: `seed_neo4j_so_close.py`

Pour générer et insérer des données dans Neo4j, exécutez le script Python avec les paramètres souhaités. Par exemple, pour créer 1000 jardiniers :

```bash
python seed_neo4j_so_close.py --nb_users 1000
```

Le script va :

- Créer 1000 jardiniers avec des plantes cultivées aléatoires
- Insérer les données dans la base de données Neo4j
