import pandas as pd
import random
import math
from faker import Faker
from pathlib import Path


def generate_so_close_data(
    nb_jardins, rayon_km, ref_lat, ref_long, output_dir="output"
):
    fake = Faker("fr_FR")

    def random_point_within_radius(lat, lon, radius_km):
        radius_deg = radius_km / 111  # approx conversion
        angle = random.uniform(0, 2 * math.pi)
        distance = random.uniform(0, radius_deg)
        dx = distance * math.cos(angle)
        dy = distance * math.sin(angle)
        return lat + dy, lon + dx

    # Créer le répertoire de sortie
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Jardins
    jardins = []
    for i in range(1, nb_jardins + 1):
        lat, lon = random_point_within_radius(ref_lat, ref_long, rayon_km)
        jardins.append(
            {
                "jardin_id": i,
                "nom": f"Jardin {i}: {fake.first_name()}",
                "latitude": round(lat, 6),
                "longitude": round(lon, 6),
            }
        )
    df_jardins = pd.DataFrame(jardins)
    df_jardins.to_csv(output_path / "jardins.csv", index=False)

    # Jardiniers
    jardiniers = []
    jardinier_id = 1
    for jardin in jardins:
        for _ in range(random.randint(1, 5)):
            jardiniers.append(
                {
                    "jardinier_id": jardinier_id,
                    "nom": f"Jardinier {jardinier_id} - {fake.last_name()} {fake.first_name()[:1].capitalize()}.",
                    "jardin_id": jardin["jardin_id"],
                }
            )
            jardinier_id += 1
    df_jardiniers = pd.DataFrame(jardiniers)
    df_jardiniers.to_csv(output_path / "jardiniers.csv", index=False)

    # Cultures
    plante_ids = list(range(1, 157))
    age_population = list(range(1, 16))
    age_weights = [5] * 5 + [3] * 5 + [1] * 5

    cultures = []
    for jardin in jardins:
        nb_plantes = random.randint(10, 156)
        selected_plantes = random.sample(plante_ids, nb_plantes)
        age = random.choices(age_population, weights=age_weights, k=1)[0]
        for plante_id in selected_plantes:
            cultures.append(
                {"jardin_id": jardin["jardin_id"], "plante_id": plante_id, "age": age}
            )
    df_cultures = pd.DataFrame(cultures)
    df_cultures.to_csv(output_path / "cultures.csv", index=False)


if __name__ == "__main__":
    # Arguments pour la génération des données

    from argparse import ArgumentParser

    parser = ArgumentParser(
        description="Générer des données pour l'application So Close"
    )
    parser.add_argument(
        "--nb_jardins", type=int, required=True, help="Nombre de jardins à générer"
    )
    parser.add_argument(
        "--rayon_km",
        type=float,
        required=True,
        help="Rayon en kilomètres autour du point de référence",
    )
    parser.add_argument(
        "--ref_lat",
        type=float,
        metavar="LATITUDE",
        default=48.8566,
        help="Latitude du point de référence (par défaut Paris 48.8566)",
    )
    parser.add_argument(
        "--ref_long",
        type=float,
        metavar="LONGITUDE",
        default=2.3522,
        help="Longitude du point de référence (par défaut Paris 2.3522)",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        metavar="OUTPUT_DIR",
        default="../data",
        help="Répertoire de sortie pour les données générées (defaut: ../data)",
    )

    args = parser.parse_args()

    generate_so_close_data(
        nb_jardins=args.nb_jardins,
        rayon_km=args.rayon_km,
        ref_lat=args.ref_lat,
        ref_long=args.ref_long,
        output_dir=args.output_dir,
    )
