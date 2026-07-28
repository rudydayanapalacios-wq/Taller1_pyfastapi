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