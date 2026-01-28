# Pipeline ETL de ventas retail con Pandas, SQLAlchemy y Docker
## Descripción

Proyecto que implementa un pipeline de extracción, transformación y carga (ETL) utilizando Python. Consume datos de un archivo CSV, transforma los datos a través de pandas y los guarda en una tabla SQL creada a través de SQLAlchemy. Además, se aplica un control de errores mientras transcurre el proceso de ETL.

## Características

- **Separación de responsabilidades:** Creación de métodos en distintos archivos `.env` para separar la lógica y mejor mantenimiento del código del modelo ORM, conexión, transformación de datos y ejecución de pipeline. 

- **Extracción dinámica:** Implementación de lectura inteligente de archivos CSV desde la carpeta de datos, para evitar adjuntar el archivo CSV en una carpeta específica.

- **Seguridad:** Gestión de credenciales mediante variables de entorno `.env` para evitar el hardcodeo de información sensible en el código fuente.

- **Logging:** Sistema de logs con niveles de seguridad (INFO, ERROR, DEBUG) para gestión de trazabilidad del pipeline.

- **Integración robusta a SQL:** Manejo de SQLAlchemy ORM para la creación y gestión de tablas eficiente.

- **Integración a Docker:** Creación de contenedores aislados para garantizar la ejecución del pipeline desde cualquier entorno.

## Arquitectura del Pipeline

El pipeline sigue el procedimiento ETL estándar:

```
Entrada (CSV) → Extracción → Transformación → Carga (SQL Server)
```

### Flujo de datos:

1. **Extracción**: Lee datos del archivo `data/retail_store_sales.csv`
2. **Transformación**: 
   - Normalización de columnas
   - Conversión de tipo de datos
   - Limpieza de valores nulos
   - Normalización de textos
   - Relleno de valores faltantes según tipo de dato
3. **Carga**: Carga de datos a tabla SQL Server

## Tecnologías Utilizadas

- **Python 3.13**
- **Pandas**: Para carga, limpieza y transformación de datos
- **SQLAlchemy**: Para la gestión de base de datos (ORM)
- **Python-dotenv**: Para la gestión de configuraciones de entorno
- **Docker**: Para aislar la base de datos y pipeline en contenedores.
- **SQL Server**: Para la gestión de base de datos relacionales

## Estructura del Proyecto

```
retail-csv-cleaner/
├── data/
│   └── retail_store_sales.csv          # Datos fuente (CSV)
├── notebooks/
│   └── script.ipynb                    # Notebook de pruebas para análisis
├── src/
│   ├── main.py                         # Script principal
│   ├── config.py                       # Configuración de variables de entorno
│   ├── database.py                     # Conexión y gestión a la BD
│   ├── models.py                       # Modelos ORM de tablas
│   └── etl_logic.py                    # Lógica ETL
├── Dockerfile                          # Configuración de contenedor
├── docker-compose.yaml                 # Orquestación de servicios
├── requirements.txt                    # Archivo para instalar librerias Python
└── README.md                           # Este archivo
```

## Prerequisitos

- Python 3.11 o superior
- SQL Server 2019 o superior instalado
- Git para clonar el repositorio
- Docker y Docker Compose (En caso desee la ejecución en contenedores)
- Acceso a línea de comandos (PowerShell, CMD o Terminal)
- Pip (Gestor de paquetes de Python)

## Configuración e Instalación

### Opción 1: Ejecución a nivel local

#### Requisitos previos:
- Python 3.11+
- SQL Server en ejecución
- pip (gestor de paquetes)

#### Instalación:

1. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

2. **Configurar variables de entorno (reemplazar `.env.example` por `.env`):**
```
DB_SERVER="Nombre del servidor (SELECT @@SERVERNAME)"
DB_NAME="Nombre de la base de datos"
DB_USER="Usuario de base de datos"
DB_PASSWORD="Contraseña del usuario de base de datos"
DB_DRIVER="Driver de DB, puede ser: ODBC Driver 17 for SQL Server"
```

3. **Ejecutar el pipeline:**
```bash
python src/main.py
```

### Opción 2: Ejecución con Docker

#### Requisitos:
- Docker y Docker Compose instalados

### Puntos a tomar en cuenta:
- El programa Python se inicia automáticamente tras la disponibilidad de SQL Server
- SQL Server en Docker se ejecutará en el puerto `1434` (internamente 1433)

#### Pasos:

1. **Configurar variables de entorno (reemplazar `.env.example` por `.env`):**
```
DB_SERVER=mssql_server,1433
DB_NAME="Nombre de la base de datos"
DB_USER=sa
DB_PASSWORD="Contraseña del usuario de base de datos"
DB_DRIVER=ODBC Driver 17 for SQL Server
```

2. **Construir e iniciar los contenedores:**
```bash
docker-compose up --build
```

3. **Detener los servicios:**
```bash
docker-compose down
```