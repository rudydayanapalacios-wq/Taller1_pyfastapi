import re

from models import trainee_model
from templates import trainee_template


ALLOWED_DOCUMENT_TYPES = {"CC", "TI", "CE"}


def validate_trainee_field(field, value):
    """Devuelve el error de un campo o una cadena vacía si es válido."""
    if field == "tipo_doc" and value not in ALLOWED_DOCUMENT_TYPES:
        return "El tipo de documento debe ser CC, TI o CE."

    if field == "documento" and not value.isdigit():
        return "El número de documento solo puede contener números."

    if field in {"nombre", "programa"}:
        label = "El nombre" if field == "nombre" else "El programa"

        if not value or not all(part.isalpha() for part in value.split()):
            return f"{label} solo puede contener letras y espacios."

        if len(value) > 30:
            return f"{label} no puede tener más de 30 caracteres."

    if field == "ficha" and not value.isdigit():
        return "La ficha solo puede contener números."

    if field == "correo":
        email_pattern = r"[a-z0-9](?:[a-z0-9._%+-]*[a-z0-9])?@(gmail|hotmail|outlook)\.com"
        if not re.fullmatch(email_pattern, value):
            return "El correo debe incluir @ y usar gmail.com, hotmail.com u outlook.com."

    return ""


def validate_trainee(data):
    """Valida los datos ingresados y devuelve una lista de errores."""
    return [
        error
        for field, value in data.items()
        if (error := validate_trainee_field(field, value))
    ]


def init_app_data():
    """Inicializa los datos de la plicación , creando de la tebla de aprendices si no existe """
    trainee_model.load_data()


def register_trainee_view():
    """Logica para procesar el registro de un aprendiz desde la vista."""
    data = trainee_template.get_trainee_input(validate_trainee_field)

    errors = validate_trainee(data)
    if errors:
        for error in errors:
            trainee_template.display_message({"type": "error", "text": error})
        return

    # Validar si el aprendiz ya existe
    if trainee_model.search_by_document(data["documento"]):
        trainee_template.display_message(
            {
                "type": "error",
                "text": "Ya existe un aprendiz registrado con este número de documento."
            }
        )
        return

    # Registrar aprendiz a través de la capa MODELO
    trainee_model.register_trainee(data)

    # Confirmar en la interfaz
    trainee_template.display_message({
        "type": "success",
        "text": f"Aprendiz {data['nombre']} registrado exitosamente en la ficha {data['ficha']}."
    })


def status_view():
    """Muestra el estado actual de la lista de aprendices."""
    all_trainees = trainee_model.get_all()
    trainee_template.display_trainee(all_trainees)