import os
import shutil
import pandas as pd
import logging

# Configuration des logs
log_file = r"C:\Users\j.tresfield-exterieu\Documents\02 - Dev\python\projects\eps-to-jpg\eps_copy_log.log"
csv_output_file = r"C:\Users\j.tresfield-exterieu\Documents\02 - Dev\python\projects\eps-to-jpg\eps_copy_copied_files_log.csv"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file, mode="a", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

# Chemins d'accès
input_file = r"C:\Users\j.tresfield-exterieu\Documents\02 - Dev\python\projects\eps-to-jpg\CONCATENATION_DATA_jeu données test_07012025.xlsx"
sheet_name = "Sheet 1"
network_folder = r"\\Svlyofic102\stockage\GROUPE\FOS\Marketing\Phototheque\00_ PHOTOS_HD"
destination_folder = r"\\Svlyofic102\stockage\GROUPE\FOS\Marketing\Phototheque\00_PHOTOS_HD_EPS_JPG"

# Vérification de l'existence du fichier Excel
if not os.path.exists(input_file):
    logging.error(f"Le fichier Excel {input_file} est introuvable.")
    exit(1)

# Charger le fichier Excel et lire les codes produits
try:
    df = pd.read_excel(input_file, sheet_name=sheet_name)
    codes_produits = df.iloc[:, 0].dropna().astype(str)  # Supposer que la première colonne contient les codes produits
    logging.info(f"{len(codes_produits)} codes produits chargés depuis le fichier Excel.")
except Exception as e:
    logging.error(f"Erreur lors de la lecture du fichier Excel : {e}")
    exit(1)

# Vérifier si le dossier de destination existe, sinon le créer
if not os.path.exists(destination_folder):
    try:
        os.makedirs(destination_folder)
        logging.info(f"Création du dossier de destination : {destination_folder}")
    except Exception as e:
        logging.error(f"Impossible de créer le dossier de destination : {e}")
        exit(1)

# Initialisation du dictionnaire pour stocker les fichiers copiés
copied_files_data = {}

# Parcourir les codes produits
for code in codes_produits:
    nb_fichiers_copies = 0
    logging.info(f"Recherche des fichiers pour le code produit : {code}")
    found_files = []
    
    for root, _, files in os.walk(network_folder):
        for file in files:
            if code in file:  # Vérifier si le nom du fichier contient le code produit
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_folder, file)
                try:
                    shutil.copy2(source_path, destination_path)  # Copier en conservant les métadonnées
                    logging.info(f"Fichier copié : {source_path} -> {destination_path}")
                    found_files.append(file)
                    nb_fichiers_copies += 1
                except Exception as e:
                    logging.error(f"Erreur lors de la copie de {source_path} : {e}")

    if found_files:
        copied_files_data[code] = found_files
    else:
        logging.warning(f"Aucun fichier trouvé pour le code produit : {code}")
        copied_files_data[code] = ["Aucun fichier trouvé"]

# Sauvegarde des résultats dans un fichier CSV
try:
    copied_files_df = pd.DataFrame.from_dict(copied_files_data, orient="index")
    copied_files_df.index.name = "Code Produit"
    copied_files_df.to_csv(csv_output_file, encoding="utf-8-sig", index=True)
    logging.info(f"Fichier CSV généré avec les fichiers copiés : {csv_output_file}")
except Exception as e:
    logging.error(f"Erreur lors de l'écriture du fichier CSV : {e}")

logging.info("Traitement terminé.")

    
print(f"Nombre de fichiers copiés pour le code {code} : {nb_fichiers_copies} fichier(s)")