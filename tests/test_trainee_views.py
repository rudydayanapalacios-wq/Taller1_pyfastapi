from unittest.mock import patch

from views import trainee_view

@patch("templates.trainee_template.display_message")
@patch("templates.trainee_template.get_trainee_input")
@patch("models.trainee_model.register_trainee")
@patch("models.trainee_model.search_by_document")

def test_register_trainee_view_success(mock_search, mock_register, mock_input, mock_display):

    # Arrange
    trainee_data = {
        "tipo_doc": "CC",
        "documento": "123456789",
        "nombre": "Juan Perez",
        "ficha": "12345",
        "programa": "Programación",
        "correo": "juan.perez@gmail.com"
    }

    mock_input.return_value = trainee_data # Simula la entrada del usuario
    mock_search.return_value = None  # Simula que el documento no está registrado

    # Act
    trainee_view.register_trainee_view()

    # Assert
    mock_input.assert_called_once()  # Verifica que se solicitó la entrada del usuario
    mock_search.assert_called_once_with(trainee_data["documento"])  # Verifica que se buscó el documento
    mock_register.assert_called_once_with(trainee_data)  # Verifica que se intentó registrar el aprendiz
    mock_display.assert_called_once_with(
        {"type": "success", "text": f"Aprendiz {trainee_data['nombre']} registrado exitosamente en la ficha {trainee_data['ficha']}.", }
    )  # Verifica que se mostró el mensaje de éxito
