import csv
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

def insert_recoltes_to_cassandra(csv_file_path):
    # Connexion Cassandra (adapter si besoin)
    cluster = Cluster(['localhost'])
    session = cluster.connect()

    # Créer le keyspace et la table
    session.execute("""
    CREATE KEYSPACE IF NOT EXISTS so_close
    WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1}
    """)

    session.set_keyspace('so_close')

    session.execute("""
    CREATE TABLE IF NOT EXISTS cultures (
        jardin_id int,
        annee int,
        mois int,
        plante text,
        quantite int,
        saison text,
        PRIMARY KEY ((jardin_id), annee, mois, plante)
    )
    """)

    # Lecture CSV et insertion
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            session.execute("""
            INSERT INTO cultures (jardin_id, annee, mois, plante, quantite, saison)
            VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                int(row['jardin_id']),
                int(row['annee']),
                int(row['mois']),
                row['plante'],
                int(row['quantite']),
                row['saison']
            ))

    print("✅ Données insérées avec succès dans Cassandra.")

if __name__ == "__main__":
    insert_recoltes_to_cassandra("cultures_recoltes.csv")
