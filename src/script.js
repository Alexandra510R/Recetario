// Esperar a que el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', function() {
    // Obtener referencias a los elementos del formulario
    const formulario = document.getElementById('registroForm');
    const btnLimpiar = document.getElementById('btnLimpiar');
    const listaDatos = document.getElementById('listaDatos');
    
    // Cargar datos guardados al iniciar
    cargarDatosGuardados();
    
    // Manejar el evento de envío del formulario
    formulario.addEventListener('submit', function(e) {
        e.preventDefault(); // Prevenir el envío tradicional del formulario
        
        // Obtener los valores del formulario
        const nombre = document.getElementById('nombre').value;
        const email = document.getElementById('email').value;
        const telefono = document.getElementById('telefono').value;
        const edad = document.getElementById('edad').value;
        const genero = document.getElementById('genero').value;
        const interes = document.getElementById('interes').value;
        const mensaje = document.getElementById('mensaje').value;
        
        // Validar campos obligatorios
        if (!nombre || !email) {
            alert('Por favor, complete los campos obligatorios: Nombre y Email');
            return;
        }
        
        // Crear objeto con los datos
        const datos = {
            nombre,
            email,
            telefono,
            edad,
            genero,
            interes,
            mensaje,
            fecha: new Date().toLocaleString()
        };
        
        // Guardar los datos
        guardarDatos(datos);
        
        // Actualizar la lista de datos mostrados
        cargarDatosGuardados();
        
        // Limpiar el formulario
        formulario.reset();
        
        // Mostrar mensaje de éxito
        alert('¡Registro exitoso! Sus datos han sido guardados.');
    });
    
    // Manejar el evento de limpiar formulario
    btnLimpiar.addEventListener('click', function() {
        formulario.reset();
    });
    
    // Función para guardar datos en localStorage
    function guardarDatos(datos) {
        // Obtener datos existentes o inicializar array vacío
        let datosGuardados = JSON.parse(localStorage.getItem('formData')) || [];
        
        // Agregar nuevos datos
        datosGuardados.push(datos);
        
        // Guardar en localStorage
        localStorage.setItem('formData', JSON.stringify(datosGuardados));
    }
    
    // Función para cargar y mostrar datos guardados
    function cargarDatosGuardados() {
        // Obtener datos de localStorage
        const datosGuardados = JSON.parse(localStorage.getItem('formData')) || [];
        
        // Limpiar lista actual
        listaDatos.innerHTML = '';
        
        // Verificar si hay datos guardados
        if (datosGuardados.length === 0) {
            listaDatos.innerHTML = '<p>No hay datos guardados todavía.</p>';
            return;
        }
        
        // Mostrar solo los últimos 5 registros
        const ultimosRegistros = datosGuardados.slice(-5);
        
        // Mostrar cada conjunto de datos
        ultimosRegistros.forEach((dato, index) => {
            const datoElement = document.createElement('div');
            datoElement.classList.add('dato-item');
            
            datoElement.innerHTML = `
                <p><strong>Nombre:</strong> ${dato.nombre}</p>
                <p><strong>Email:</strong> ${dato.email}</p>
                <p><strong>Interés:</strong> ${dato.interes || 'No especificado'}</p>
                <p><strong>Fecha:</strong> ${dato.fecha}</p>
            `;
            
            listaDatos.appendChild(datoElement);
        });
        
        // Agregar enlace para ver todos los registros si hay más de 5
        if (datosGuardados.length > 5) {
            const verTodos = document.createElement('p');
            verTodos.innerHTML = `<a href="registros.html" style="color: #3498db; text-decoration: none;">Ver todos los registros (${datosGuardados.length})</a>`;
            listaDatos.appendChild(verTodos);
        }
    }
});