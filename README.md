# Estudio predictivo del llenado de embalses en la cuenca del Miño-Sil

TFM del Máster en Análisis y Visualización de Datos Masivos (UNIR).
Autora: Sheila González Rodríguez.

## Descripción

Este repositorio contiene el código desarrollado para predecir el porcentaje de llenado de los embalses de la cuenca hidrográfica del Miño-Sil a 7, 30 y 90 días, evaluando la aportación de las variables de calidad del agua mediante tres modelos de naturaleza distinta: SARIMAX, XGBoost y LSTM.

## Estructura del repositorio
tfm-embalses-mino-sil/
├── data/
│ ├── raw/ # Datos originales descargados de las fuentes
│ ├── external/ # Cartografía (no incluida, ver instrucciones abajo)
│ ├── interim/ # Datos intermedios (generados por el pipeline, no versionados)
│ └── processed/ # Datos procesados finales (generados por el pipeline, no versionados)
├── notebooks/ # Cuadernos Jupyter del pipeline, en orden de ejecución
├── src/ # Funciones auxiliares reutilizadas en los notebooks
├── outputs/
│ ├── figures/ # Figuras generadas
│ └── tables/ # Tablas de resultados generadas
└── README.md


## Datos

### Datos incluidos

La carpeta `data/raw` contiene los datos originales descargados de las fuentes públicas empleadas: sistema SAIH y Confederación Hidrográfica del Miño-Sil, Agencia Estatal de Meteorología (AEMET) y Anuario de Aforos.

### Datos no incluidos: cartografía

Por su volumen, la cartografía del Plan Hidrológico de la demarcación (2022-2027), empleada en la asignación espacial de estaciones a embalses, no se incluye en este repositorio. Para reproducir el pipeline completo:

1. Descargar los datos cartográficos (Cartografía digital asociada al Plan Hidrológico 2022-2027) desde el apartado de Infraestructura de Datos Espaciales Miño-Sil (IDE Miño-Sil)
CARTOGRAFÍA DIGITAL: https://www.chminosil.es/es/ide-mino-sil (enlace directo: https://www.chminosil.es/images/planificacion/cartografia/Datos-Cartograficos-Plan-Hidrologico-2022-2027.zip).
2. Descomprimir el contenido en `data/external/Datos-Cartograficos-Plan-Hidrologico-2022-2027/`, manteniendo la estructura de carpetas original (`Hidrografia/`, `Masas_Agua/`, `Division_Administrativa/`).

### Datos intermedios y procesados

No se incluyen en el repositorio, ya que se generan automáticamente al ejecutar los notebooks en orden (ver más abajo).

## Reproducibilidad

Los notebooks están numerados y deben ejecutarse en orden secuencial, desde `00_construccion_maestro_embalses.ipynb` hasta `12_modelado_lstm.ipynb`. Cada uno lee las salidas del anterior y genera las suyas propias en `data/interim` o `data/processed`.

## Requisitos

El proyecto está desarrollado en Python. Las dependencias principales son: pandas, numpy, geopandas, scikit-learn, xgboost, tensorflow, statsmodels, matplotlib, shap.
