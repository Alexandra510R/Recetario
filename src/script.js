const API_URL = "http://127.0.0.1:8000";

document.addEventListener('DOMContentLoaded', function() {
    const formulario = document.getElementById('registroForm');
    const btnLimpiar = document.getElementById('btnLimpiar');
    const listaDatos = document.getElementById('listaDatos');

    formulario.addEventListener('submit', async function(e) {
        e.preventDefault();

        const nombre = document.getElementById('nombre').value;
        const email = document.getElementById('email').value;
        const telefono = document.getElementById('telefono').value;
        const edad = document.getElementById('edad').value;
        const genero = document.getElementById('genero').value;
        const interes = document.getElementById('interes').value;
        const mensaje = document.getElementById('mensaje').value;

        if (!nombre || !email) {
            alert('Por favor, complete los campos obligatorios: Nombre y Email');
            return;
        }

        try {
            const response = await fetch(`${API_URL}/usuarios/registro`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    nombre,
                    email,
                    password: telefono || "default123",
                    telefono,
                    edad: edad ? parseInt(edad) : null,
                    genero,
                    interes,
                    mensaje
                })
            });

            const data = await response.json();

            if (response.ok) {
                alert('¡Registro exitoso!');
                formulario.reset();
                listaDatos.innerHTML = '<p>Registros guardados en la base de datos ✅</p>';
            } else {
                alert('Error: ' + (data.detail || 'No se pudo registrar'));
            }
        } catch (error) {
            alert('Error conectando con el servidor');
            console.error(error);
        }
    });

    btnLimpiar.addEventListener('click', function() {
        formulario.reset();
    });

    listaDatos.innerHTML = '<p>Registros guardados en la base de datos ✅</p>';
});