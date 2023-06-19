$(document).ready(function() {
    $('#myForm').submit(function(event) {
      event.preventDefault();
  
      var rut = $('#rut').val();
      var nombre = $('#nombre').val();
      var apellido = $('#apellido').val();
      var telefono = $('#telefono').val();
      var correo = $('#correo').val();
      var clave = $('#clave').val();
  
      // Aquí puedes realizar cualquier acción que desees con los datos del formulario
      // Por ejemplo, puedes enviar los datos a un servidor mediante AJAX
  
      // Ejemplo de envío de datos por AJAX usando jQuery
      $.ajax({
        url: 'guardar_datos.php', // Ruta al archivo PHP que procesará los datos
        method: 'POST',
        data: {
          rut: rut,
          nombre: nombre,
          apellido: apellido,
          telefono: telefono,
          correo: correo,
          clave: clave
        },
        success: function(response) {
          // La respuesta del servidor en caso de éxito
          console.log(response);
        },
        error: function(xhr, status, error) {
          // Manejo de errores
          console.log(error);
        }
      });
    });
  });
  