# TFM — Estudio predictivo del porcentaje de llenado de embalses en la cuenca del Miño-Sil

Trabajo Fin de Máster del Máster Universitario en Análisis y Visualización de Datos Masivos (UNIR).

**Autora:** Sheila González Rodríguez  
**Fecha estimada de entrega:** septiembre 2026

## Descripción

Desarrollo de modelos predictivos del porcentaje de llenado de los embalses de la cuenca hidrográfica del Miño-Sil, integrando datos meteorológicos, hidrológicos y de calidad del agua procedentes de SAIH, Anuario de Aforos y AEMET.

## Estructura del proyecto

- `data/`: datos originales, intermedios y procesados.
- `notebooks/`: análisis exploratorio y experimentación.
- `src/`: código reutilizable.
- `outputs/`: figuras, tablas y resultados.
- `docs/`: documentación auxiliar.

## Reproducibilidad

Para reproducir el entorno de trabajo:

    conda env create -f environment.yml
    conda activate tfm-embalses

## Fuentes de datos

- Sistema Automático de Información Hidrológica (SAIH) del Miño-Sil.
- Anuario de Aforos del Centro de Estudios y Experimentación de Obras Públicas (CEDEX).
- API OpenData de la Agencia Estatal de Meteorología (AEMET).