const novoElemento = document.createElement("p");
novoElemento.textContent = "Algum texto zaca";

const paragrafoPrincipal = document.querySelector("#paragrafo-principal");
const elementoPai = paragrafoPrincipal.parentNode;
elementoPai.appendChild(novoElemento);