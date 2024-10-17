const lista = document.createElement("ul");
for(let i = 0; i < 5; i++) {
    const item = document.createElement("li");
    item.textContent = `Algum item ${i}`;
    lista.appendChild(item);
}

const containerPrincipal = document.getElementById("container-principal");
containerPrincipal.appendChild(lista);