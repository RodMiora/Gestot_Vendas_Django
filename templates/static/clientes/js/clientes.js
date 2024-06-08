$(document).ready(function() {
    $('.editar-cliente').click(function() {
        var clienteId = $(this).data('cliente-id');
        $('#formulario-edicao-' + clienteId).toggleClass('hidden');
    });

    $('.cancelar-edicao').click(function() {
        $(this).closest('form').addClass('hidden');
    });
});
