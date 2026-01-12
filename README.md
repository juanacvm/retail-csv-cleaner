# Pipeline de ventas de una empresa Retail

Creación de un proceso pipeline donde se extraen datos de ventas minoristas (a través de un archivo csv), lo transforma y posteriormente lo carga a hacia una base de datos en SQL Server.

## Descripción

El proyecto automatiza el proceso de:
1. **Extracción** de datos del archivo `retail_store_sales.csv`, ubicado en la carpeta "data".
2. **Transformar** los datos limpiando valores faltantes, normalizando columnas y formatos de fecha
3. **Cargar** los datos procesados hacia una tabla SQL Server local.

## Estructura del Proyecto

```
retail-csv-cleaner/
├── data/
│   └── retail_store_sales.csv      # Datos fuente
├── src/
│   ├── main.py                     # Script principal con pipeline ETL
│   ├── config.py                   # Configuración de variables de entorno
│   ├── database.py                 # Conexión a la base de datos
│   ├── models.py                   # Creacion del modelo de tablas mediante ORM
│   └── etl_logic.py                # Lógica de extracción y transformación de datos
├── README.md
└── requirements.txt                # Archivo TXT con las librerías necesarias para ejecutar el programa
```

## Requisitos

- Python 3.8+
- SQL Server
- Variables de entorno configuradas (.env)

## Instalación

1. Instalar dependencias:
```bash
pip install -r requirements.txt
```

2. Crear archivo `.env` con las credenciales:
```
DB_SERVER=Nombre de servidor (En caso desconocerlo usar SELECT @@SERVERNAME)
DB_NAME=Nombre de base de datos
DB_USER=Nombre de usuario
DB_PASSWORD=Contraseña
DB_DRIVER=Driver de base de datos, puede ser: ODBC Driver 17 for SQL Server
```

## Uso

Ejecutar el pipeline:
```bash
python src/main.py
```

El script registrará el progreso y cualquier error mediante el manejo de logging.

## Características

- ✅ Manejo robusto de excepciones
- ✅ Logging detallado de cada paso
- ✅ Manejo de pandas para la normalización de datos y columnas 
- ✅ Manejo de pandas para llenar datos automáticamente
- ✅ Conversión de tipos de datos