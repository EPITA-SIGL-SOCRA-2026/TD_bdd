from neo4j import GraphDatabase
import random


class SoCloseNeo4jSeeder:

    def __init__(
        self, uri="bolt://localhost:7687", user="neo4j", password="so_close_password"
    ):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def seed_data(self, nb_users, nb_plantes):
        plantes = [f"Plante {i}" for i in range(1, nb_plantes + 1)]

        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")  # reset

            for i in range(1, nb_users + 1):
                user_name = f"Jardinier {i}"
                plantes_cultivees = random.sample(
                    plantes, random.randint(2, int(nb_plantes / 2))
                )

                session.run("CREATE (:Utilisateur {nom: $nom})", nom=user_name)

                for plante in plantes_cultivees:
                    session.run(
                        """
                        MERGE (p:Plante {nom: $plante})
                        WITH p
                        MATCH (u:Utilisateur {nom: $user})
                        MERGE (u)-[:CULTIVE]->(p)
                    """,
                        user=user_name,
                        plante=plante,
                    )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Seed Neo4j database with SoClose data"
    )
    parser.add_argument(
        "--nb_users",
        type=int,
        required=True,
        help="Number of users (jardiniers) to create",
    )
    parser.add_argument(
        "--nb_plantes",
        type=int,
        default=120,
        help="Number of unique plants that can be cultivated",
    )
    args = parser.parse_args()
    seeder = SoCloseNeo4jSeeder()
    print("🔄 Chargement des données dans Neo4j...")
    seeder.seed_data(
        nb_users=args.nb_users,
        nb_plantes=args.nb_plantes,
    )
    seeder.close()
    print("✅ Données insérées dans Neo4j")
