const novoElemento = document.createElement("p");
novoElemento.textContent = "Algum texto";

const elementoPai = document.querySelector("#container-principal");
const elementoAlvo = document.querySelector("#titulo-principal");

elementoPai.insertBefore(novoElemento, elementoAlvo);
