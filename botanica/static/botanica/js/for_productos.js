// Script para enviar el formulario mediante AJAX
$(document).ready(function() {
    $('#productForm').submit(function(e) {
        e.preventDefault(); // Prevenir el envío del formulario

        // Obtener los valores de los campos
        var idProducto = $('#idProducto').val();
        var nombre = $('#nombre').val();
        var precio = $('#precio').val();
        var stock = $('#stock').val();
        var idCategoria = $('#idCategoria').val();

        // Aquí puedes realizar las operaciones necesarias con los datos (por ejemplo, enviarlos al servidor)

        // Ejemplo de impresión en la consola del navegador
        console.log('ID Producto: ' + idProducto);
        console.log('Nombre: ' + nombre);
        console.log('Precio: ' + precio);
        console.log('Stock: ' + stock);
        console.log('ID Categoría: ' + idCategoria);

        // Limpiar los campos del formulario
        $('#productForm')[0].reset();
    });
});
