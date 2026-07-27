from views import aprendiz_view as trainee_view
from templates import trainee_template

def main():

  while True:
    # registar un aprendiz
    trainee_view.register_trainee_view()

    # muestra como va quedando
    trainee_view.status_view()

    # preguntar si desea registar otro aprendiz
    if not trainee_template.display_confirm_next():
      print("saliendo del programa hasta luego. ¡Hasta luego!")
      break


if __name__ == "__main__":
    main()