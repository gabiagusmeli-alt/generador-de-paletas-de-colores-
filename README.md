# Generador de Paletas de Colores

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Estado](https://img.shields.io/badge/Estado-Desarrollo-orange.svg)]()
[![Demo](https://img.shields.io/badge/Demo-Enlace%20pr%C3%B3ximamente-lightgrey.svg)]()

Resumen

Aplicación web desarrollada con Flask para generar paletas de colores armoniosas y exportables. Pensada como proyecto de portafolio: interfaz limpia, resultados visuales y opciones de exportación para uso en diseño y frontend.

Captura / Presentación

Incluye una captura o GIF del sitio para darle presencia en tu portafolio. Sugerencia de ruta y marcado para añadir una imagen:

```markdown
![Captura de ejemplo](static/screenshot.png)
```

Características principales

- Generación de paletas aleatorias y por reglas de color (monocromático, análogo, complementario, etc.).
- Copiado con un clic de valores HEX y preview en tiempo real.
- Exportación en formatos útiles (CSS, JSON, SCSS, Tailwind).
- Interfaz responsive, estilo moderno y enfoque en usabilidad para diseñadores.

Tecnologías

- Backend: Flask
- Frontend: HTML5, CSS3, JavaScript (vanilla)
- Plantillas: Jinja2

Instalación (entorno local)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Ejecución local

```bash
# Ejecuta la app directamente
python app.py

# O con Flask en modo desarrollo
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Uso rápido

- Abre `http://127.0.0.1:5000/` en tu navegador.
- Haz clic en "Generar" para obtener una nueva paleta.
- Copia valores HEX con los botones de la interfaz.

Personalización para tu portafolio

- Ajusta `static/style.css` para adaptar tipografías, colores y espaciado.
- Añade una captura en `static/screenshot.png` y descomenta su referencia arriba para que se muestre en el README.

Estructura del proyecto

```
generador-de-paletas-de-colores/
├── app.py
├── requirements.txt
├── static/
│   ├── style.css
│   └── app.js
└── templates/
	└── index.html
```

Despliegue

Esta guía no incluye `gunicorn` ni `Procfile` ya que el despliegue previsto será en PythonAnywhere. Si más adelante deseas desplegar en otro servicio, puedo añadir instrucciones específicas.

Agregar el enlace del proyecto en vivo

Deja un espacio en el README para el enlace en vivo. Cuando tengas la URL, reemplaza el badge "Demo: Enlace próximamente" por el enlace directo:

```markdown
[Demo en vivo](https://tu-app.pythonanywhere.com)
```

Contribuciones

- Issues y pull requests bienvenidos. Describe claramente el cambio y mantén los PRs pequeños.

Contacto

- Añade tu email o enlace a tu portafolio si quieres que los visitantes te contacten.

Licencia

Indica la licencia del proyecto (por ejemplo, MIT) si procede.
