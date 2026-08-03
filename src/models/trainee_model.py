import json
import os
import csv

# Base de datos en archivo JSON
DATABASE_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'trainees.json'))
trainees = []

CSV_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'trainees.csv'))
trainees = []



# Crear la carpeta data/ y el archivo trainees.json si no existen
def ensure_datafile_exists():
    """Asegura que el archivo de datos exista, creándolo si es necesario."""
    if not os.path.exists(DATABASE_FILE):
        os.makedirs(os.path.dirname(DATABASE_FILE), exist_ok=True)
        with open(DATABASE_FILE, "w", encoding="utf-8") as file:
            json.dump([], file)  # Inicializa con una lista vacía

def load_data():
    """Carga los datos de aprendices desde el archivo JSON."""
    global trainees
    ensure_datafile_exists()
    with open(DATABASE_FILE, "r", encoding="utf-8") as file:
        try:
            trainees = json.load(file)
        except json.JSONDecodeError:
            trainees = []

def save_data():
    """Guarda los datos de aprendices en el archivo JSON."""
    ensure_datafile_exists()
    with open(DATABASE_FILE, "w", encoding="utf-8") as file:
        json.dump(trainees, file, ensure_ascii=False, indent=4)

def get_all():
    """Obtiene todos los aprendices registrados."""
    return trainees

def search_by_document(document):
    """Busca un aprendiz por su número de documento."""
    for a in trainees:
        if a["documento"] == document:
            return a
    return None


def search_by_name(name):
    """Busca aprendices cuyo nombre contiene el texto indicado."""
    query = name.strip().casefold()
    if not query:
        return []
    return [trainee for trainee in trainees if query in trainee["nombre"].casefold()]


def search_by_ficha(ficha):
    """Busca aprendices por ficha, admitiendo coincidencias parciales."""
    query = ficha.strip()
    if not query:
        return []
    return [trainee for trainee in trainees if query in trainee["ficha"]]

def register_trainee(new_trainee):
    """Registra un nuevo aprendiz si no existe previamente en la lista."""
    if search_by_document(new_trainee["documento"]):
        return False 
    trainees.append(new_trainee)
    save_data()  # Guardar los datos después de registrar un nuevo aprendiz 
    return True

def update_trainee(documento, update_data):
    """Actualiza un aprendiz identificado por su documento actual."""
    aprendiz = search_by_document(documento)

    if not aprendiz:
        return False

    new_document = update_data.get("documento", documento)
    existing_trainee = search_by_document(new_document)
    if existing_trainee and existing_trainee is not aprendiz:
        return False

    aprendiz.update(update_data)
    save_data()
    return True


def delete_trainee(documento):
    """Elimina el aprendiz asociado al documento y guarda el cambio."""
    aprendiz = search_by_document(documento)
    if not aprendiz:
        return False

    trainees.remove(aprendiz)
    save_data()
    return True


def export_to_csv():
    """Exporta los datos de aprendices a un archivo CSV."""
    with open(CSV_FILE, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "tipo_doc",
                "documento",
                "nombre",
                "ficha",
                "programa",
                "correo",
            ],
        )
        writer.writeheader()
        writer.writerows(trainees)
    return CSV_FILE

    