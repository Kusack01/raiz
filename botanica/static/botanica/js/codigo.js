$(document).ready(function() {
    $("#cambio-contrasena-form").submit(function(event) {
      event.preventDefault();
  
      var codigo = $("#codigo").val();
  
      alert("El código ingresado es: " + codigo);
    });
  });