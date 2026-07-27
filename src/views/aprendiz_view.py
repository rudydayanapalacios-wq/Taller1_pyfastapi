from models import trainee_model
from templates import trainee_template

def register_trainee_view():
    """Logica para procesar el registro de un aprendiz desde la vista."""
    data = trainee_template.get_trainee_input()

    # Validar si el aprendiz ya existe
    if trainee_model.search_by_document(data["documento"]):
        trainee_template.display_message({
            "type": "error",
            "text": "Ya existe un aprendiz registrado con este número de documento."
        })
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
