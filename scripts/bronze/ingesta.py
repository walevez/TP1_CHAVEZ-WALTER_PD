import os
import pandas as pd

def capa_bronze(source_path: str, bronze_path: str):
    print('-------------------------Iniciando Capa Bronze-------------------------')

    if not os.path.exists(source_path):
        raise FileNotFoundError(f'No se encontro el archivo en: {source_path}')

    df_bronze = pd.read_csv(source_path)

    if df_bronze.empty:
        raise ValueError(f'El DataFrame esta vacio')

    print(f'\nEl DataFrame cargado tiene: {df_bronze.shape[0]} filas y {df_bronze.shape[1]} columnas.')

    print('\n-------------Explorando los tipos de datos en las columnas-------------')

    print(f'{df_bronze.dtypes}')

    print('\n-------------Columnas relevantes cumplir con las consignas-------------')

    columnas_r = ['Year',
                  'Start Year',
                  'Start Month',
                  'Start Day',
                  'Disaster Group',
                  'Disaster Subgroup',
                  'Disaster Type',
                  'Disaster Subtype',
                  'Continent',
                  'Region',
                  'Country',
                  'Total Deaths',
                  'Total Affected',
                  "Total Damages ('000 US$)"
                  ]

    resumen_columnas_r = pd.DataFrame({
        'tipo_dato': df_bronze[columnas_r].dtypes,
        'nulos_suma': df_bronze[columnas_r].isna().sum(),
        'nulos_promedio': (df_bronze[columnas_r].isna().mean()*100).round(2),
        'valores_unicos': df_bronze[columnas_r].nunique()
    })

    print(resumen_columnas_r)

    ruta_bronce = f'{bronze_path}/disasters_bronze.csv'
    df_bronze.to_csv(ruta_bronce, index=False)

    print(f'\nDatos crudos guardados en Bronze: {ruta_bronce}')

    return ruta_bronce