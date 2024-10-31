function abrirModal(src) {
    document.getElementById("modalImagen").style.display = "block";
    document.getElementById("imagenAmpliada").src = src;
}

function cerrarModal() {
    document.getElementById("modalImagen").style.display = "none";
}
