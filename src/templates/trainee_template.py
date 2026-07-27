def get_trainee_input():
    """Solicita al usuario los datos del aprendiz y devuelve un diccionario con la información."""
    type_id = input("Tipo de documento (CC/TI/CE): ").strip().upper()
    id = input("Número de documento: ").strip()
    name = input("Nombre completo: ").strip().title()
    group_code = input("Ficha: ").strip()
    program = input("Programa: ").strip().title()

    return {
        "tipo_doc": type_id,
        "documento": id,
        "nombre": name,
        "ficha": group_code,
        "programa": program,
    }


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
        print(f"Documento: {trai['documento']}, Nombre: {trai['nombre']}, Ficha: {trai['ficha']}, Programa: {trai['programa']}")


def display_confirm_next():
    """Pregunta al usuario si desea registrar otro aprendiz."""
    continuar = input("\n¿Deseas registrar otro aprendiz? (s/n): ").strip().lower()
    return continuar == "s"

