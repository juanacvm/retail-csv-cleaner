import os
import pandas as pd

#Extrae los datos del archivo sales.csv existente en la carpeta data
def extract_retail_sales_file() -> pd.DataFrame:
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__)) #busca la direccion actual del script main
        file_path = os.path.join(script_dir,'../data/retail_store_sales.csv') #busca la direccion del archivo .csv
        df = pd.read_csv(file_path) #Lee el documento csv
        print('File load completed succesfully.')

        return df

    except FileNotFoundError:
        raise FileNotFoundError('File not found')
    
#Metodo que normaliza la información y transforma los datos sucios
def transform_retail_sales_file(df: pd.DataFrame) -> pd.DataFrame:
    
    #Normaliza las columnas a snake_case
    df.columns = df.columns.str.lower().str.strip().str.replace(' ','_')

    #Convierte a DateTime, en caso de error retorna NaT
    df['transaction_date'] = pd.to_datetime(df['transaction_date'], errors = 'coerce')

    #Reemplaza los valores na por valores funcionales
    fill_na_dict = {
        'item': 'Unknown', #Desconocido
        'price_per_unit': df['price_per_unit'].mean().round(2), #La media de precios
        'quantity': df['quantity'].mean().round(2), #La media de cantidad
        'discount_applied': False #Falso por defecto
    }

    df = df.fillna(fill_na_dict)

    #Reemplaza el valor gastado na por la multiplicacion del precio y cantidad
    df['total_spent'] = df['total_spent'].fillna(df['price_per_unit']*df['quantity'])

    #Normaliza espacios y convierte los textos en minusculas
    text_columns = df.select_dtypes(include=['str']).columns
    df[text_columns] = df[text_columns].apply(lambda x: x.str.strip().str.lower())
    
    return df