function mostrarDetalhes(titulo, empresa, descricao) {
    document.getElementById("popup-titulo").textContent = titulo;
    document.getElementById("popup-empresa").textContent = "Empresa: " + empresa;
    document.getElementById("popup-descricao").textContent = descricao;

    var popup = document.getElementById("vaga-popup");
    popup.style.display = "block";
}

function fecharPopup() {
    var popup = document.getElementById("vaga-popup");
    popup.style.display = "none";
}
