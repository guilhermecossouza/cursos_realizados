const novoelemento = document.createElement("p");
novoelemento.textContent = "H1 substituido pelo parágrafo p";

const tituloPrincipal = document.querySelector("#titulo-principal");
const elementoPai = tituloPrincipal.parentNode;

elementoPai.replaceChild(novoelemento, tituloPrincipal);