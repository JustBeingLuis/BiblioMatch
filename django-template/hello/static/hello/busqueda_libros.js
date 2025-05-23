document.querySelectorAll('.btn-detalles').forEach(btn => {
    btn.addEventListener('click', function() {
        const libroId = this.getAttribute('data-libro-id');
        fetch(`/hello/libro/${libroId}/modal/`)
            .then(response => response.text())
            .then(html => {
                document.getElementById('modal-info').innerHTML = html;
                document.getElementById('modal-detalles').style.display = 'block';
            });
    });
});

document.getElementById('cerrar-modal').onclick = function() {
    document.getElementById('modal-detalles').style.display = 'none';
};