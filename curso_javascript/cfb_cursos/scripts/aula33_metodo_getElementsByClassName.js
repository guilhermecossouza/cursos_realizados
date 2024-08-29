console.log("Classe curso");
const cursosElementos = document.getElementsByClassName("curso");
console.log(cursosElementos);
console.log("clase c1")
const c1Elementos = document.getElementsByClassName("c1");
console.log(c1Elementos);
console.log("clase c2")
const c2Elementos = document.getElementsByClassName("c2");
console.log(c2Elementos);

console.log("");
console.log("");
console.log("Convertendo os elementos html em array");

const arrElementoCurso = [...document.getElementsByClassName("curso")]
const arrElementoC1 = [...document.getElementsByClassName("c1")]
const arrElementoC2 = [...document.getElementsByClassName("c2")]

arrElementoC1.map((el) => {
    el.classList.add("destaque");
});
