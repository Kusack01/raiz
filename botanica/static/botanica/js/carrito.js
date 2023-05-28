$(document).ready(function() {
	// Cuando el usuario cambia la cantidad de un producto
	$("input[type='number']").change(function() {
		var precio = parseFloat($(this).parent().prev().text().replace("$", ""));
		var cantidad = parseInt($(this).val());
		var subtotal = precio * cantidad;
		$(this).parent().next().text("$" + subtotal.toFixed(2));
	});

	// Cuando el usuario actualiza el carrito
	$(".btn-primary").click(function() {
		var total = 0;
		$("tbody tr").each(function() {
			var subtotal = parseFloat($(this).find("td:last").text().replace("$", ""));
			total += subtotal;
		});
		$(".total").text("$" + total.toFixed(2));
	});

	// Cuando el usuario compra los productos//
