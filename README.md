# 📒 Titulo y descripcion.

Nombre:Rudy Dyana Placios Ayala
Ficha:3406204
* Competencia:Elaboración de la propuesta técnica para la solución de software.
* Implantación del del software

## **Sistema de Registro de Aprendices SENA**

Proyecto en Python para la gestion de aprendices SENA mediante interfaz por consola.

1.Registrar la siguiente informacion mediante una funcion
*   Tipo doc
*   Documento
*   Nombres
*   Apellidos
*   Ficha
*   Programa

# 📁 Estructura del proyecto

```markdown
Taller1_pyfastapi/
│
├── data/
│   └── aprendices.json     # Fuente de datos persistente
│
├── src/
│   ├── models/             # capa MODEL: Datos, esquemas y logica de persistencia
│   │   └── aprendiz_model.py
│   │
│   ├── templates/          # Capa TEMPLATE: Formato de salida / Interfaces / Consola
│   │   └── aprendiz_template.py
│   │
│   ├── views/              # Capa VIEW: Logica de negocio y manejo de peticiones
│   │   └── aprendiz_view.py
│   │
│   └── main.py             # Punto de entrada de la aplicacion
│
├── tests/
│   ├── test_models.py      # Pruebas para la capa de modelos
│   └── test_views.py       # Pruebas para la logica de vistas
│
├── .gitignore              # Archivos ignorados por Git
├── Prueba.ipynb            
├── README.md               # Documentacion del proyecto
└── requirements.txt        # Dependencia (FastAPI, Uvicorn, Pydantic, etc.)
```
# ℹ️ TAREA

# **Taller 1: Proyecto Python + Fastapi+Github**

# Requerimientos 29/07/2026

#1. Refactorizar ruta del archivo JSON en la carpeta data/✅
#2. Refactorizar validaciones de los datos de entrada(incluir el correo electrónico) en la vista para que sean más robustas y claras.(Númerica, alfabética, correo electrónico, etc.)✅
#3. Implementar el editar de aprendices para permitir modificar los datos de un aprendiz existente.✅
#4. Implementar la eliminación de aprendices para permitir borrar un aprendiz existente de la lista.✅
#5. Implementar la búsqueda de aprendices por nombre o ficha para facilitar la localización de registros específicos.✅
#6.Implementar la exportación de la lista de aprendices a un archivo CSV para facilitar el manejo de datos fuera del programa. ✅
#7. Implementar un menú principal para que el usuario pueda elegir entre registrar, editar, eliminar, buscar o exportar aprendices, en lugar de solo registrar uno tras otro.✅
