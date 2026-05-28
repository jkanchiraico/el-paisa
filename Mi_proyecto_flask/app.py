# Importamos la herramienta Flask y la función para procesar texto HTML directo
from flask import Flask, render_template_string

app = Flask(__name__)

# --- TU CÓDIGO HTML INTEGRADO (Ajustado con imágenes estables de internet) ---
html_paisa = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>El Paisa | Inicio</title>
    <style>
        /* --- ESTILOS DE LA BARRA (Idéntica a tu captura) --- */
        body {
            margin: 0;
            padding: 0;
            font-family: 'Arial', sans-serif;
            background-color: #0b0b0b; /* Fondo negro elegante */
            color: #ffffff;
        }

        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 30px 60px;
            background-color: #0b0b0b;
        }

        .logo-central {
            color: #ffffff;
            font-size: 28px;
            font-weight: bold;
            letter-spacing: 4px;
            margin: 0;
            text-transform: uppercase;
        }

        nav ul {
            list-style: none;
            margin: 0;
            padding: 0;
            display: flex;
            gap: 35px;
        }

        nav ul li a {
            text-decoration: none;
            color: #ffffff;
            font-size: 12px;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 2px;
        }

        /* --- CONTENEDOR DE LAS 3 IMÁGENES EN FILA --- */
        .contenedor-tres-imagenes {
            display: flex; /* Ponle las imágenes en fila horizontal */
            justify-content: space-between; /* Distribuye el espacio uniformemente */
            gap: 20px; /* La separación exacta que quieres entre las fotos */
            padding: 20px 60px; /* Alineado con el margen de la barra de arriba */
            box-sizing: border-box;
            width: 100%;
        }

        /* Fuerza a que las 3 fotos tengan exactamente el mismo tamaño */
        .columna-foto {
            flex: 1; /* Hace que las 3 cajas midan exactamente lo mismo */
            overflow: hidden;
        }

        .columna-foto img {
            width: 100%; /* Se adapta al tamaño de la columna */
            height: 350px; /* Ajustado para que luzcan tus platos */
            object-fit: cover; /* Corta la imagen para que no se deforme */
            display: block;
        }
        
        /* --- ESTILOS PARA EL PIE DE PÁGINA --- */
        .pie-pagina {
            background-color: #1a1a1a; /* El color gris oscuro mate */
            padding: 40px 60px;
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            border-top: 1px solid #2b2b2b;
            margin-top: 40px;
        }

        .columna-footer {
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 8px;
            font-size: 13px;
            color: #a3a3a3; /* Gris claro para textos secundarios */
        }

        .columna-footer a {
            color: #ffffff;
            text-decoration: none;
            transition: color 0.3s;
        }

        .columna-footer a:hover {
            color: #e2007a; /* Brillo rosa al pasar el mouse */
        }

        .columna-footer.centro {
            text-align: center;
        }

        .columna-footer.derecha {
            text-align: right;
        }

        .redes, .dias {
            color: #ffffff;
            font-weight: bold;
            margin: 0 0 5px 0;
        }

        .columna-footer p {
            margin: 0;
        }
    </style>
</head>
<body>

    <header>
        <h1 class="logo-central">EL PAISA</h1>
        <nav>
            <ul>
                <li><a href="#">Historia</a></li>
                <li><a href="#">La Carta</a></li>
                <li><a href="#">Reservas</a></li>
                <li><a href="#">Contacto</a></li>
            </ul>
        </nav>
    </header>

    <div class="contenedor-tres-imagenes">
        <div class="columna-foto">
            <img src="https://images.unsplash.com/photo-1626132647523-66f5bf380027?q=80&w=600" alt="Imagen 1">
        </div>
        <div class="columna-foto">
            <img src="https://images.unsplash.com/photo-1546069901-ba9599a7e63c?q=80&w=600" alt="Imagen 2">
        </div>
        <div class="columna-foto">
            <img src="https://images.unsplash.com/photo-1604382354936-07c5d9983bd3?q=80&w=600" alt="Imagen 3">
        </div>
    </div>

    <footer class="pie-pagina">
        <div class="columna-footer">
            <a href="#">Política de Privacidad</a>
            <a href="#">Términos & Condiciones</a>
            <a href="#">Libro de Reclamaciones</a>
        </div>

        <div class="columna-footer centro">
            <p class="redes">@ELPAISAREST</p>
            <p>Av. Principal 123, Miraflores, Lima, Perú.</p>
            <p>+51 1 234-5678 / <a href="mailto:reservas@elpaisa.com.pe">reservas@elpaisa.com.pe</a></p>
        </div>

        <div class="columna-footer derecha">
            <p class="dias">Lunes a Sábado</p>
            <p>Almuerzo: 12:45 - 15:30</p>
            <p>Cena: 19:00 - 23:00</p>
        </div>
    </footer>

</body>
</html>
"""

@app.route("/")
def home():
    # Renderizamos el string que contiene todo tu diseño de El Paisa
    return render_template_string(html_paisa)

if __name__ == "__main__":
    # Arranca en el puerto 8080 que es el que te funciona de forma nativa
    app.run(host="0.0.0.0", port=8080)