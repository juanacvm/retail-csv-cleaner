import pandas as pd
import logging
from database import engine,engine_master, sql_query, create_database
from models import Base
from etl_logic import *

# Configura logging de alertas
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

#Metodo principal de ejecucion de pipeline
def run_pipeline():
    try:

        logger.info('Iniciando pipeline de ETL...')
        
        # Crea la base de datos en caso no exista
        logger.info('Levantando la base de datos...')
        create_database(engine, sql_query)

        # Informa la eliminación de tablas existentes
        logger.info('Eliminando tablas existentes...')
        Base.metadata.drop_all(engine_master)

        # Crea las tablas
        logger.info('Creando tablas nuevas...')
        Base.metadata.create_all(engine_master)

        # Extrae datos sin procesar
        logger.info('Extrayendo datos del archivo...')
        raw_retail_sales = extract_retail_sales_file()

        # Transforma datos
        logger.info('Transformando datos...')
        final_retail_data = transform_retail_sales_file(raw_retail_sales)

        # Carga datos en la base de datos
        logger.info('Cargando datos en la base de datos...')
        final_retail_data.to_sql(name='sales', con=engine_master, if_exists='append', index=False)
        
        logger.info('Pipeline completado exitosamente.')
        return True

    except FileNotFoundError as e:
        logger.error(f'Error: Archivo no encontrado - {e}')
        return False
    
    except ValueError as e:
        logger.error(f'Error: Problema con los datos - {e}')
        return False
    
    except Exception as e:
        logger.error(f'Error inesperado en el pipeline: {type(e).__name__} - {e}')
        return False

if __name__ == '__main__':
    success = run_pipeline()
    exit(0 if success else 1)