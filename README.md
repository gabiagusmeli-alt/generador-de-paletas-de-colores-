# Generador de Paletas — Despliegue

Instrucciones rápidas para desplegar esta aplicación Flask en producción.

Requisitos:

- Python 3.10+
- `pip` instalado

Instalar dependencias:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Ejecutar localmente con Gunicorn:

```bash
export FLASK_SECRET_KEY="tu-secreto"
export PORT=5000
gunicorn wsgi:application --workers 3 --bind 0.0.0.0:5000
```

Despliegue rápido (Heroku):

```bash
heroku create
git push heroku main
heroku config:set FLASK_SECRET_KEY="tu-secreto"
heroku ps:scale web=1
```

Notas de seguridad:

- Mantén `FLASK_SECRET_KEY` en variables de entorno.
- Usa HTTPS en producción.
- Considera añadir un reverse proxy (NGINX) y configurar cabeceras adicionales.
