import os
from PIL import Image
import logging
from datetime import datetime

# Configuration des logs
log_file = r"C:\Users\j.tresfield-exterieu\Documents\02 - Dev\python\projects\eps-to-jpg\eps_to_jpg_log.log" + datetime.now().strftime('eps_to_jpg_log_%Y_%m_%d_%H_%M_.log')

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file, mode="a", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

# Dossier contenant les fichiers EPS à convertir
source_base = r"C:\Temp\A vérifier par Cindy"
source_folder_name = r"\EPS"
source_folder = source_base + source_folder_name

# Dossier cible dans lequel les fichiers EPS seront convertis en JPG
target_folder_name = r"\JPG"
target_folder = source_base + target_folder_name

# Configuration du chemin Ghostscript
base_path = os.path.dirname(__file__)
ghostscript_path = os.path.join(base_path, 'ghostscript', 'App')

# Définir les variables d'environnement pour Ghostscript
os.environ['GS_LIB'] = os.path.join(ghostscript_path, 'lib')
os.environ['PATH'] = os.path.join(ghostscript_path, 'bin') + os.pathsep + os.environ['PATH']

# Vérification du dossier source
if not os.path.exists(source_folder):
    logging.error(f"Le dossier source n'existe pas : {source_folder}")
    exit(1)

# Vérification du dossier cible et création si besoin
if not os.path.exists(target_folder):
    try:
        os.mkdir(target_folder_name)
        logging.info(f"Le dossier cible n'existe pas - Création du dossier : {target_folder_name}")
    except FileExistsError:
        print(f"Le dossier '{target_folder_name}' existe déjà.")
    except PermissionError:
        print(f"Permission denied: Impossible de créer le dossier '{target_folder_name}'.")
    except Exception as e:
        print(f"Une erreur est survenue: {e}")


# Parcourir le dossier cible et convertir les fichiers EPS
for file_name in os.listdir(source_folder):
    if file_name.lower().endswith('.eps'):
        eps_path = os.path.join(source_folder, file_name)
        jpg_filename = os.path.splitext(file_name)[0] + '.jpg'
        jpg_path = os.path.join(target_folder, jpg_filename)

        try:
            logging.info(f"Tentative de conversion de {file_name} en JPG...")

            # Ouvrir le fichier EPS avec Pillow
            img = Image.open(eps_path)
            
            # Convertir en JPG et sauvegarder
            img.convert('CMYK').save(jpg_path, 'JPEG')

            logging.info(f"Conversion réussie : {jpg_path}")

        except Exception as e:
            logging.error(f"Erreur lors de la conversion de {file_name} : {e}")

logging.info("Traitement terminé.")
