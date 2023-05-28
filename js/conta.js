$(document).ready(function() {
    $("#contact-form").submit(function(e) {
      e.preventDefault();
      var name = $("#name").val();
      var email = $("#email").val();
      var message = $("#message").val();
      $.ajax({
        type: "POST",
        url: "send_email.php", // Reemplaza esto con la URL de tu archivo html que enviará el correo electrónico
        data: {name: name, email: email, message: message},
        success: function() {
          alert("Mensaje enviado correctamente");
          $("#contact-form")[0].reset();
        },
        error: function() {
          alert("Ha ocurrido un error al enviar el mensaje");
        }
      });
    });
  });