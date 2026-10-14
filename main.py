import os
from scripts.bronze.ingesta import capa_bronze

SOURCE_PATH = 'sources/1970-2021_DISASTERS-dataset.csv'
BRONZE_PATH = 'data/1_bronze'
SILVER_PATH = 'data/2_silver'
GOLD_PATH = 'data/3_gold'

def crear_directorios():
    for path in [BRONZE_PATH, SILVER_PATH, GOLD_PATH]:
        os.makedirs(path, exist_ok=True)

if __name__ == '__main__':
    crear_directorios()

    ruta_bronze = capa_bronze(SOURCE_PATH, BRONZE_PATH)

    ruta_plata = capa_plata(ruta_bronze)