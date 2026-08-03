def get_trainee_input(validate_field):
    """Solicita cada dato y no avanza hasta que sea válido."""
    fields = (
        ("tipo_doc", "Tipo de documento (CC/TI/CE): ", str.upper),
        ("documento", "Número de documento: ", str),
        ("nombre", "Nombre completo: ", str.title),
        ("ficha", "Ficha: ", str),
        ("programa", "Programa: ", str.title),
        ("correo", "Correo electrónico: ", str.lower),
    )
    data = {}

    for field, prompt, formatter in fields:
        while True:
            value = formatter(input(prompt).strip())
            error = validate_field(field, value)
            if not error:
                data[field] = value
                break
            display_message({"type": "error", "text": error})

    return data


def get_document_input(prompt):
    """Solicita el documento usado para identificar a un aprendiz."""
    return input(prompt).strip()


def get_trainee_update_input(current_trainee, validate_field):
    """Solicita los nuevos datos; una entrada vacia conserva el valor actual."""
    fields = (
        ("tipo_doc", "Tipo de documento (CC/TI/CE)", str.upper),
        ("documento", "Numero de documento", str),
        ("nombre", "Nombre completo", str.title),
        ("ficha", "Ficha", str),
        ("programa", "Programa", str.title),
        ("correo", "Correo electronico", str.lower),
    )
    data = {}

    for field, label, formatter in fields:
        while True:
            value = input(f"{label} [{current_trainee[field]}]: ").strip()
            if not value:
                data[field] = current_trainee[field]
                break

            value = formatter(value)
            error = validate_field(field, value)
            if not error:
                data[field] = value
                break
            display_message({"type": "error", "text": error})

    return data


def display_message(message):
    icons = {
        "success": "✅",
        "error": "⚠️",
        "info": "ℹ️"
    }
    print(f"{icons.get(message['type'], '')} {message['text']}")


def display_trainee(trainee):
    """Muestra la lista de aprendices registrados."""
    if not trainee:
        print("No hay aprendices registrados.")
        return

    print("\n--- Lista de Aprendices Registrados ---")

    for trai in trainee:
        print(
            f"Documento: {trai['documento']}, "
            f"Nombre: {trai['nombre']}, "
            f"Ficha: {trai['ficha']}, "
            f"Programa: {trai['programa']}, "
            f"Correo: {trai['correo']}"
        )


def display_confirm_next():
    """Pregunta al usuario si desea registrar otro aprendiz."""
    continuar = input("\n¿Deseas registrar otro aprendiz? (s/n): ").strip().lower()
    return continuar == "s"
