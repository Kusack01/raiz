// Código de jQuery

$(function() {
	$('form').on('submit', function(event) {
		event.preventDefault();
		var email = $('#email').val();
		var password = $('#password').val();
		// Aquí se puede agregar la lógica de validación de inicio de sesión
		// por ejemplo, enviar los datos a un servidor y verificar si son correctos
		// si son correctos, redirigir al usuario a la página principal
		// si no son correctos, mostrar un mensaje de error
	});
});
