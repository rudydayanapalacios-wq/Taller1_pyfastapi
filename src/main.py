from views import trainee_view


def main():
    trainee_view.init_app_data()

    while True:
        print("\n=======================")
        print("    MENÚ PRINCIPAL    ")
        print("=======================")
        print("1. Registrar aprendiz")
        print("2. Editar aprendiz")
        print("3. Eliminar aprendiz")
        print("4. Buscar aprendiz")
        print("5. Listar aprendices")
        print("6. Exportar CSV")
        print("0. Salir")
        print("=======================\n")
        option = input("Seleccione una opcion: ").strip()

        actions = {
            "1": trainee_view.register_trainee_view,
            "2": trainee_view.edit_trainee_view,
            "3": trainee_view.delete_trainee_view,
            "4": trainee_view.search_trainee_view,
            "5": trainee_view.status_view,
            "6": trainee_view.export_trainees_view
        }
        if option == "0":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        elif option in actions:
            actions[option]()
        else:
            print("Opcion invalida.")


if __name__ == "__main__":
    main()
