from flask import Flask, render_template_string

app = Flask(__name__)

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

        .columna-foto {
            flex: 1; 
            overflow: hidden;
        }

        .columna-foto img {
            width: 100%; 
            height: 350px; 
            object-fit: cover; 
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

        /* --- ESTILOS DE COMBOS Y SERVICIOS --- */
        .seccion-servicios, .seccion-crud {
            padding: 40px 60px;
            background-color: #0b0b0b;
        }

        .titulo-seccion {
            text-align: center;
            font-size: 24px;
            letter-spacing: 3px;
            text-transform: uppercase;
            margin-bottom: 30px;
            color: #ffffff;
            border-bottom: 1px solid #222;
            padding-bottom: 15px;
        }

        .contenedor-combos {
            display: flex;
            gap: 25px;
            justify-content: space-between;
        }

        .tarjeta-combo {
            background-color: #161616;
            border: 1px solid #222;
            padding: 25px;
            flex: 1;
            position: relative;
            transition: transform 0.3s, border-color 0.3s;
        }

        .tarjeta-combo:hover {
            transform: translateY(-5px);
            border-color: #ffffff;
        }

        .tarjeta-combo h3 {
            margin-top: 10px;
            font-size: 18px;
            color: #ffffff;
        }

        .descripcion-combo {
            font-size: 14px;
            color: #aaa;
            line-height: 1.5;
            min-height: 60px;
        }

        .precio-combo {
            font-size: 20px;
            font-weight: bold;
            color: #ffffff;
            margin-top: 15px;
            text-align: right;
        }

        .combo-badge {
            position: absolute;
            top: -10px;
            left: 20px;
            background-color: #ffffff;
            color: #0b0b0b;
            font-size: 11px;
            font-weight: bold;
            text-transform: uppercase;
            padding: 3px 10px;
            letter-spacing: 1px;
        }

        /* --- ESTILOS DEL CRUD --- */
        .formulario-crud {
            display: flex;
            gap: 15px;
            max-width: 700px;
            margin: 0 auto 30px auto;
        }

        .formulario-crud input {
            flex: 1;
            padding: 12px;
            background-color: #161616;
            border: 1px solid #333;
            color: white;
            font-size: 14px;
        }

        .formulario-crud input:focus {
            outline: none;
            border-color: #ffffff;
        }

        .formulario-crud button {
            padding: 12px 24px;
            background-color: #ffffff;
            color: #0b0b0b;
            border: none;
            font-weight: bold;
            cursor: pointer;
            text-transform: uppercase;
            font-size: 12px;
            letter-spacing: 1px;
        }

        .tabla-crud {
            width: 100%;
            max-width: 700px;
            margin: 0 auto;
            border-collapse: collapse;
            background-color: #161616;
        }

        .tabla-crud th, .tabla-crud td {
            padding: 15px;
            text-align: left;
            border-bottom: 1px solid #222;
        }

        .tabla-crud th {
            background-color: #222;
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .btn-borrar {
            background-color: transparent;
            color: #ff4d4d;
            border: 1px solid #ff4d4d;
            padding: 5px 12px;
            cursor: pointer;
            font-size: 12px;
            transition: all 0.3s;
        }

        .btn-borrar:hover {
            background-color: #ff4d4d;
            color: white;
        }
    </style>
<body>

    <header>
        <h1 class="logo-central">EL PAISA</h1>
        <nav>
            <ul>
                <li><a href="https://regester-2ftc.onrender.com">Registrarse</a></li>
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

    <section class="seccion-servicios">
        <h2 class="titulo-seccion">Combos & Servicios Especiales</h2>
        
        <div class="contenedor-combos">
            <div class="tarjeta-combo">
                <div class="combo-badge">Popular</div>
                <h3>Combo Paisa Familiar</h3>
                <p class="descripcion-combo">Lleva 1 Ceviche Clásico + 1 Lomo Saltado Grande + 1 Jarra de Chicha Morada de 1.5L.</p>
                <div class="precio-combo">S/ 85.00</div>
            </div>

            <div class="tarjeta-combo">
                <div class="combo-badge">Recomendado</div>
                <h3>Combo Tradición Dúo</h3>
                <p class="descripcion-combo">Perfecto para dos. 2 Ají de Gallina + 2 Bebidas personales a elección + Postre del día.</p>
                <div class="precio-combo">S/ 55.00</div>
            </div>

            <div class="tarjeta-combo">
                <h3>Servicio Catering Especial</h3>
                <p class="descripcion-combo">¿Tienes un evento? Llevamos lo mejor de nuestra cocina a tu casa o empresa. Buffet criollo completo.</p>
                <div class="precio-combo">Consultar</div>
            </div>
        </div>
    </section>

    <section class="seccion-crud">
        <h2 class="titulo-seccion">Panel de Administración de productos</h2>
        
        <div class="formulario-crud">
            <input type="text" id="crud-nombre" placeholder="Nombre del nuevo plato (Ej: Seco de Res)">
            <input type="text" id="crud-precio" placeholder="Precio (Ej: S/ 35.00)">
            <button onclick="crearPlato()">Agregar a la Carta</button>
        </div>

        <table class="tabla-crud">
            <thead>
                <tr>
                    <th>Plato</th>
                    <th>Precio</th>
                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody id="lista-platos">
                <tr>
                    <td>Ceviche Clásico</td>
                    <td>S/ 38.00</td>
                    <td><button class="btn-borrar" onclick="eliminarPlato(this)">Eliminar</button></td>
                </tr>
                <tr>
                    <td>Lomo Saltado</td>
                    <td>S/ 42.00</td>
                    <td><button class="btn-borrar" onclick="eliminarPlato(this)">Eliminar</button></td>
                </tr>
            </tbody>
        </table>
    </section>

    <footer class="pie-pagina">
        <div class="columna-footer">
            <a href="#">Política de Privacidad</a>
            <a href="#">Términos & Condiciones</a>
            <a href="#">Libro de Reclamaciones</a>
        </div>

        <div class="columna-footer centro">
            <p class="redes">@ELPAISAREST</p>
            <li><a href="#">ENCUENTRANOS AQUI!!</a></li>
            <p>+51 1 234-5678 / <a href="mailto:reservas@elpaisa.com.pe">reservas@elpaisa.com.pe</a></p>
        </div>

        <div class="columna-footer derecha">
            <p class="dias">Lunes a Sábado</p>
            <p>Almuerzo: 12:45 - 15:30</p>
            <p>Cena: 19:00 - 23:00</p>
        </div>
    </footer>

    <script>
        function crearPlato() {
            var nombre = document.getElementById("crud-nombre").value;
            var precio = document.getElementById("crud-precio").value;

            if (nombre === "" || precio === "") {
                alert("Por favor, llena ambos campos para registrar el plato.");
                return;
            }

            var tabla = document.getElementById("lista-platos");
            var nuevaFila = document.createElement("tr");

            // Concatenamos a la antigua usanza con comillas simples para evitar el conflicto con Flask
            nuevaFila.innerHTML = '<td>' + nombre + '</td>' +
                                  '<td>' + precio + '</td>' +
                                  '<td><button class="btn-borrar" onclick="eliminarPlato(this)">Eliminar</button></td>';

            tabla.appendChild(nuevaFila);

            document.getElementById("crud-nombre").value = "";
            document.getElementById("crud-precio").value = "";
        }
        function eliminarPlato(boton) {
            if (confirm("¿Estás seguro de quitar este plato de la lista?")) {
                var fila = boton.closest ? boton.closest("tr") : boton.parentNode.parentNode;
                if (fila && fila.parentNode) {
                    fila.parentNode.removeChild(fila);
                }
            }
        }
    </script>
</body>
</html>
    
</body>
</html>
"""
@app.route("/")
def Index():
    # Renderizamos el string que contiene todo tu diseño de El Paisa
    return render_template_string(html_paisa)

@app.route("/registro")
def registro():
    return """
    <html>
    <body style="background-color:black; color:white; font-family:Arial;">
        <h1>Registro de Personas</h1>

        <form>
            Código:<br>
            <input type="text"><br><br>

            Nombres:<br>
            <input type="text"><br><br>

            Apellidos:<br>
            <input type="text"><br><br>

            <button type="submit">Guardar</button>
        </form>

        <br><br>

        <a href="/" style="color:white;">Volver al inicio</a>
    </body>
    </html>
    """

if __name__ == "__main__":
    # Arranca en el puerto 8080 que es el que te funciona de forma nativa
    app.run(host="0.0.0.0", port=8080)