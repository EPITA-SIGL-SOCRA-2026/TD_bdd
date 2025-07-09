import pandas as pd
import random
from pathlib import Path

annees = [2022, 2023, 2024]
saisons = {
    1: "hiver",
    2: "hiver",
    3: "printemps",
    4: "printemps",
    5: "printemps",
    6: "été",
    7: "été",
    8: "été",
    9: "automne",
    10: "automne",
    11: "automne",
    12: "hiver",
}

plantes = [
    "menthe",
    "tomate",
    "basilic",
    "romarin",
    "courgette",
    "fraise",
    "ail",
    "persil",
]


def generate_cultures_recoltes(nb_jardins, output_dir):

    mois = list(range(1, 13))

    recoltes_par_jardin = []
    recoltes_par_plante = []
    for jardin_id in range(1, nb_jardins + 1):
        for annee in annees:
            for mois_i in mois:
                for plante in random.sample(plantes, random.randint(2, len(plantes))):
                    quantite = random.randint(5, 80)
                    recoltes_par_jardin.append(
                        {
                            "jardin_id": jardin_id,
                            "annee": annee,
                            "mois": mois_i,
                            "plante": plante,
                            "quantite": quantite,
                            "saison": saisons[mois_i],
                        }
                    )
                    recoltes_par_plante.append(
                        {
                            "jardin_id": jardin_id,
                            "plante": plante,
                            "annee": annee,
                            "mois": mois_i,
                            "quantite": quantite,
                            "saison": saisons[mois_i],
                        }
                    )

    Path(output_dir).mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(recoltes_par_jardin)
    df_2 = pd.DataFrame(recoltes_par_plante)
    output_path = Path(output_dir) / "cultures_recoltes_par_jardin_cassandra.csv"
    output_path_2 = Path(output_dir) / "cultures_recoltes_par_plante_cassandra.csv"
    df.to_csv(output_path, index=False)
    df_2.to_csv(output_path_2, index=False)
    print(
        f"✅ Données générées dans {output_path.resolve()} et {output_path_2.resolve()}"
    )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Générer des données de cultures et récoltes."
    )
    parser.add_argument(
        "--nb_jardins", type=int, required=True, help="Nombre de jardins à générer."
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default="../data",
        help="Répertoire de sortie pour les données générées.",
    )
    args = parser.parse_args()
    generate_cultures_recoltes(nb_jardins=args.nb_jardins, output_dir=args.output_dir)
