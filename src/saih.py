import re

CODIGOS_VAR = [
    # Embalses: volumen, nivel, caudal de salida y aportación (con sus variantes de prefijo)
    "MACVEMBA", "MAIVEMBA", "ACVEMBA",
    "MAINEMBA", "AINEMBA",
    "MACQSALR", "MAIQSALR", "MAIQTSAL", "MACQTSAL", "ACQTSAL",
    "MAIAPORT", "ACAPORT",
    # Hidrología en río
    "AINRIO", "AINRL7S", "ACQRIO", "AIQRIO",
    # Meteorología
    "AIPCINC", "AITEMEX",
    # Calidad del agua
    "AIA3ATS", "AIA6AFS", "AIMPCTS", "AIMPO2S",
    "AIMPPHS", "AIMPTTS", "AITUTUS", "AIMOMOS",
]

# Identificador + separador opcional + código de variable + sufijo numérico opcional.
# Contempla los dos formatos del SAIH: 'A002_AINRIO1' y 'E005AAIPCINC'.
PATRON_COL = re.compile(r"^([A-Z0-9]+?)_?(" + "|".join(CODIGOS_VAR) + r")\d*$", re.IGNORECASE)

def id_estacion(col):
    m = PATRON_COL.match(str(col).strip().split(" ")[0])
    return m.group(1).upper() if m else None

def num_saih(codigo):
    """Parte numérica de un identificador SAIH de embalse.

    Los ficheros del SAIH conviven con dos codificaciones para un mismo embalse:
    'E07A' en las hojas de identificación y 'E007' en el Anuario de Aforos. La parte
    numérica permite establecer la correspondencia entre ambas.

    'E001' -> 1 | 'E07A' -> 7 | 'E350' -> 350 | 'E003-E005' -> 3 | 'A002' -> NaN

    Devuelve NaN si el código no corresponde a un embalse, por lo que conviene
    descartar los nulos antes de cruzar por este campo.
    """
    m = re.match(r"^E(\d+)", str(codigo).strip().upper())
    return int(m.group(1)) if m else float("nan")

def normalizar_id_embalse(codigo):
    """Normaliza un identificador de embalse a la forma usada en las hojas de
    identificación del SAIH.

    Las hojas de datos rellenan el número a tres dígitos ('E005A', 'E016A') mientras
    que las de identificación usan dos cuando hay sufijo de letra ('E05A', 'E16A').
    El sufijo se conserva porque es lo que distingue instalaciones de un mismo embalse
    (E16A presa, E16D central hidroeléctrica).

    'E005A' -> 'E05A' | 'E016A' -> 'E16A' | 'E001' -> 'E001' | 'E03S' -> 'E03S'

    Devuelve None si el código no corresponde a un embalse.
    """
    m = re.match(r"^E(\d+)([A-Z]*)$", str(codigo).strip().upper())
    if not m:
        return None
    numero, sufijo = int(m.group(1)), m.group(2)
    return f"E{numero:02d}{sufijo}" if sufijo else f"E{numero:03d}"