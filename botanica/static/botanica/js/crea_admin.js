$(document).ready(function() {
    // Acción al hacer clic en el botón "Registrar"
    $(".botons").click(function(event) {
        event.preventDefault(); // Evitar que se envíe el formulario por defecto

        // Obtener los valores de los campos de entrada
        var nombres = $("#nombres").val();
        var apellidos = $("#apellidos").val();
        var correo = $("#correo").val();
        var contraseña = $("#passwords").val();

        // Realizar la lógica de validación y envío de datos aquí
        // ...

        // Ejemplo de mostrar los valores ingresados en la consola
        console.log("Nombres: " + nombres);
        console.log("Apellidos: " + apellidos);
        console.log("Correo: " + correo);
        console.log("Contraseña: " + contraseña);
    });
});
