from models import trainee_model


def make_trainee(documento, nombre, ficha):
    return {
        "tipo_doc": "CC",
        "documento": documento,
        "nombre": nombre,
        "ficha": ficha,
        "programa": "Analisis",
        "correo": f"{documento}@gmail.com",
    }


def setup_trainees(monkeypatch):
    monkeypatch.setattr(
        trainee_model,
        "trainees",
        [make_trainee("1", "Ana Gomez", "3406204"), make_trainee("2", "Juan Perez", "3406205")],
    )
    monkeypatch.setattr(trainee_model, "save_data", lambda: None)


def test_update_trainee_changes_data_and_rejects_duplicate_document(monkeypatch):
    setup_trainees(monkeypatch)

    assert trainee_model.update_trainee("1", {"nombre": "Ana Maria Gomez", "documento": "3"})
    assert trainee_model.search_by_document("3")["nombre"] == "Ana Maria Gomez"
    assert not trainee_model.update_trainee("3", {"documento": "2"})


def test_delete_trainee_removes_existing_record(monkeypatch):
    setup_trainees(monkeypatch)

    assert trainee_model.delete_trainee("1")
    assert trainee_model.search_by_document("1") is None
    assert not trainee_model.delete_trainee("999")


def test_search_trainees_by_name_or_ficha(monkeypatch):
    setup_trainees(monkeypatch)

    assert [trainee["documento"] for trainee in trainee_model.search_by_name("GOMEZ")] == ["1"]
    assert [trainee["documento"] for trainee in trainee_model.search_by_ficha("340620")] == ["1", "2"]
