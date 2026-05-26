import os
from flask import Flask, render_template, request, jsonify
import random
import colorsys
import datetime

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'dev-secret-key-use-env')
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
    PREFERRED_URL_SCHEME='https'
)

@app.after_request
def set_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    response.headers['Permissions-Policy'] = 'geolocation=(), microphone=(), camera=()'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains; preload'
    response.headers['Content-Security-Policy'] = (
        "default-src 'self'; "
        "script-src 'self'; "
        "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
        "font-src 'self' https://fonts.gstatic.com; "
        "img-src 'self' data:; "
        "connect-src 'self'; "
        "frame-ancestors 'none';"
    )
    return response


def hsv_to_hex(h, s, v):
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return "#{:02x}{:02x}{:02x}".format(int(r*255), int(g*255), int(b*255))

def generate_palette(scheme="random", seed=None):
    if seed is not None:
        random.seed(seed)
        
    palette = []
    base_h = random.random()
    base_s = random.uniform(0.6, 0.9)
    base_v = random.uniform(0.7, 0.9)

    if scheme == "monochromatic":
        # Desde muy claro y poco saturado hasta muy oscuro y muy saturado
        for i in range(5):
            v = 0.95 - (i * 0.18) # Brillo desciende
            s = 0.20 + (i * 0.17) # Saturación aumenta
            palette.append(hsv_to_hex(base_h, s, v))
            
    elif scheme == "analogous":
        # Desplazamiento muy sutil (aprox 12 grados = 0.033 en la rueda)
        for i in range(5):
            h = (base_h + (i * 0.033)) % 1.0
            # Variar s y v ligeramente para dar profundidad
            s = base_s if i % 2 == 0 else max(0.4, base_s - 0.2)
            v = base_v if i % 2 != 0 else max(0.4, base_v - 0.2)
            palette.append(hsv_to_hex(h, s, v))
            
    elif scheme == "complementary":
        # Base, Base Claro, Complemento, Complemento Claro, Base Oscuro
        comp_h = (base_h + 0.5) % 1.0
        
        palette.append(hsv_to_hex(base_h, base_s, base_v)) # 1. Base
        palette.append(hsv_to_hex(base_h, max(0.2, base_s - 0.4), min(1.0, base_v + 0.2))) # 2. Base claro (Highlight)
        palette.append(hsv_to_hex(comp_h, base_s, base_v)) # 3. Complemento
        palette.append(hsv_to_hex(comp_h, max(0.2, base_s - 0.4), min(1.0, base_v + 0.2))) # 4. Complemento claro
        palette.append(hsv_to_hex(base_h, min(1.0, base_s + 0.2), max(0.1, base_v - 0.5))) # 5. Base muy oscuro (Sombra)
        
    else: # random
        # Usamos la "Proporción Áurea" (Golden Ratio Conjugate) para distribuir los tonos equitativamente
        h = base_h
        for i in range(5):
            h = (h + 0.618033988749895) % 1.0
            s = random.uniform(0.5, 0.8) # Mantenemos saturación controlada
            v = random.uniform(0.6, 0.9) # Mantenemos brillo alto
            palette.append(hsv_to_hex(h, s, v))
            
    # Resetear seed si se usó uno
    if seed is not None:
        random.seed()
            
    return palette

@app.route('/')
def index():
    # 1. Paleta Diaria (consistente todo el día usando la fecha)
    today = datetime.date.today().strftime("%Y-%m-%d")
    
    # Decidimos un scheme para el día
    random.seed(today)
    daily_scheme = random.choice(["monochromatic", "analogous", "complementary", "random"])
    random.seed() # Volvemos a aleatorio real
    
    daily_palette = {
        "title": "Paleta Diaria",
        "scheme": daily_scheme,
        "colors": generate_palette(daily_scheme, seed=today)
    }
    
    # 2. Generar múltiples paletas para explorar
    schemes_list = ["monochromatic", "analogous", "complementary", "random"]
    explore_palettes = []
    
    nombres = {
        "monochromatic": "Monocromático",
        "analogous": "Análogo",
        "complementary": "Complementario",
        "random": "Aleatorio"
    }

    for idx in range(30):
        sch = random.choice(schemes_list)
        explore_palettes.append({
            "title": f"Paleta {idx + 1}",
            "scheme": sch,
            "colors": generate_palette(sch)
        })
        
    return render_template('index.html', daily_palette=daily_palette, explore_palettes=explore_palettes)

@app.route('/api/palette')
def api_palette():
    scheme = request.args.get('scheme', 'random')
    palette = generate_palette(scheme)
    return jsonify({"palette": palette, "scheme": scheme})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', '0') == '1'
    app.run(host='0.0.0.0', port=port, debug=debug)
