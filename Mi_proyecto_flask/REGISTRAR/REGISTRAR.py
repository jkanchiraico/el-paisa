from flask import Flask, render_template_string

app = Flask(__name__)

# --- TU CÓDIGO HTML INTEGRADO (Ajustado con imágenes estables de internet) ---
html_paisa = """
<!DOCTYPE html>
<html lang="es">
<head>

</head>
<body>
<section id="registro-clientes"
        style="max-width: 500px; margin: 60px auto; background-color: #161616; border: 1px solid #222; padding: 40px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);">
        <h1
            style="font-size: 22px; text-transform: uppercase; letter-spacing: 2px; text-align: center; margin-bottom: 10px; color: white;">
            Registro de Personas</h1>
        <p id="mensaje-sistema"
            style="text-align: center; color: #ff4d4d; font-size: 14px; min-height: 20px; margin-bottom: 20px; letter-spacing: 1px;">
        </p>
    
        <form onsubmit="event.preventDefault();">
            <div style="margin-bottom: 20px;">
                <label
                    style="display: block; font-size: 12px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px; color: #aaa;">Código:</label>
                <input type="text" id="codigo"
                    style="width: 100%; padding: 12px; background-color: #0b0b0b; border: 1px solid #333; color: #ffffff; font-size: 14px; box-sizing: border-box;">
            </div>
    
            <div style="margin-bottom: 20px;">
                <label
                    style="display: block; font-size: 12px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px; color: #aaa;">Nombres:</label>
                <input type="text" id="nombres"
                    style="width: 100%; padding: 12px; background-color: #0b0b0b; border: 1px solid #333; color: #ffffff; font-size: 14px; box-sizing: border-box;">
            </div>
    
            <div style="margin-bottom: 20px;">
                <label
                    style="display: block; font-size: 12px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px; color: #aaa;">Apellidos:</label>
                <input type="text" id="apellidos"
                    style="width: 100%; padding: 12px; background-color: #0b0b0b; border: 1px solid #333; color: #ffffff; font-size: 14px; box-sizing: border-box;">
            </div>
    
            <!-- Panel de Botones CRUD -->
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 25px;">
                <button type="button" onclick="ejecutarAccion('guardar')"
                    style="grid-column: span 2; padding: 12px; font-weight: bold; text-transform: uppercase; font-size: 11px; letter-spacing: 1px; cursor: pointer; background-color: #ffffff; color: #0b0b0b; border: none;">Guardar</button>
                <button type="button" onclick="ejecutarAccion('buscar')"
                    style="padding: 12px; font-weight: bold; text-transform: uppercase; font-size: 11px; letter-spacing: 1px; cursor: pointer; background-color: #222; color: #ffffff; border: 1px solid #333;">Buscar</button>
                <button type="button" onclick="ejecutarAccion('modificar')"
                    style="padding: 12px; font-weight: bold; text-transform: uppercase; font-size: 11px; letter-spacing: 1px; cursor: pointer; background-color: #222; color: #ffffff; border: 1px solid #333;">Modificar</button>
                <button type="button" onclick="ejecutarAccion('eliminar')"
                    style="grid-column: span 2; padding: 12px; font-weight: bold; text-transform: uppercase; font-size: 11px; letter-spacing: 1px; cursor: pointer; background-color: transparent; color: #ff4d4d; border: 1px solid #ff4d4d;">Eliminar</button>
    
                <!-- Botón Sorpresa para el Profesor -->
                <button type="button" onclick="descargarTxt()"
                    style="grid-column: span 2; padding: 10px; font-weight: bold; text-transform: uppercase; font-size: 10px; background-color: #2b2b2b; color: #999; border: none; margin-top: 10px; cursor: pointer;">↓
                    Descargar archivo personas.txt</button>
            </div>
        </form>
    </section>

    <script>
        // Simulador de base de datos en memoria local
        var bdPersonas = [];

        function ejecutarAccion(accion) {
            var msgEl = document.getElementById("mensaje-sistema");
            var cod = document.getElementById("codigo").value.trim();
            var nom = document.getElementById("nombres").value.trim();
            var ape = document.getElementById("apellidos").value.trim();

            if (!cod) {
                msgEl.innerText = "Por favor, introduce un Código.";
                return;
            }

            // GUARDAR
            if (accion === 'guardar') {
                if (!nom || !ape) {
                    msgEl.innerText = "Completa nombres y apellidos.";
                    return;
                }
                // Evitar duplicados
                var existe = bdPersonas.find(p => p.codigo === cod);
                if (existe) {
                    msgEl.innerText = "El código ya existe.";
                    return;
                }
                bdPersonas.push({ codigo: cod, nombres: nom, apellidos: ape });
                msgEl.innerText = "Registro guardado.";
                limpiarCampos();
            }

            // BUSCAR
            else if (accion === 'buscar') {
                var persona = bdPersonas.find(p => p.codigo === cod);
                if (persona) {
                    document.getElementById("nombres").value = persona.nombres;
                    document.getElementById("apellidos").value = persona.apellidos;
                    msgEl.innerText = "Registro encontrado.";
                } else {
                    msgEl.innerText = "Código no encontrado.";
                }
            }

            // MODIFICAR
            else if (accion === 'modificar') {
                var index = bdPersonas.findIndex(p => p.codigo === cod);
                if (index !== -1) {
                    if (!nom || !ape) {
                        msgEl.innerText = "Completa los nuevos datos.";
                        return;
                    }
                    bdPersonas[index] = { codigo: cod, nombres: nom, apellidos: ape };
                    msgEl.innerText = "Registro modificado.";
                } else {
                    msgEl.innerText = "Código no encontrado.";
                }
            }

            // ELIMINAR
            else if (accion === 'eliminar') {
                var index = bdPersonas.findIndex(p => p.codigo === cod);
                if (index !== -1) {
                    bdPersonas.splice(index, 1);
                    msgEl.innerText = "Registro eliminado.";
                    limpiarCampos();
                } else {
                    msgEl.innerText = "Código no encontrado.";
                }
            }
        }

        function limpiarCampos() {
            document.getElementById("codigo").value = "";
            document.getElementById("nombres").value = "";
            document.getElementById("apellidos").value = "";
        }

        // FUNCIÓN MÁGICA: Crea y descarga el archivo personas.txt real en tu PC
        function descargarTxt() {
            if (bdPersonas.length === 0) {
                alert("No hay registros creados para descargar.");
                return;
            }
            var contenidoTxt = "";
            bdPersonas.forEach(function(p) {
                contenidoTxt += `${p.codigo},${p.nombres},${p.apellidos}\n`;
            });

            var blob = new Blob([contenidoTxt], { type: "text/plain;charset=utf-8" });
            var elemento = document.createElement("a");
            elemento.href = URL.createObjectURL(blob);
            elemento.download = "personas.txt";
            document.body.appendChild(elemento);
            elemento.click();
            document.body.removeChild(elemento);
        }
    </script>
</body>
</html>
"""

@app.route("/")
def inicio():
    # Renderizamos el string que contiene todo tu diseño de El Paisa
    return render_template_string(html_paisa)

if __name__ == "__main__":
    # Arranca en el puerto 8080 que es el que te funciona de forma nativa
    app.run(host="0.0.0.0", port=8080)