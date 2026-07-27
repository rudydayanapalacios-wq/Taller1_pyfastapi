# Base de datos en memoria (Lista vacia al inicio)
trainee = []

def get_all():
    """Obtiene todos los aprendices registrados."""
    return trainee

def search_by_document(document):
    """Busca un aprendiz por su número de documento."""
    for a in trainee:
        if a["documento"] == document:
            return a
    return None

def register_trainee(new_trainee):
    """Registra un nuevo aprendiz si no existe previamente en la lista."""
    if search_by_document(new_trainee["documento"]):
        return False 
    trainee.append(new_trainee)
    return True