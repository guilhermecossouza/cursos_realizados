"use script"
const caixa1 = document.querySelector("#caixa1");
const cursos = [...document.querySelectorAll(".curso")];
const btn_c1 = document.querySelector("c1");
const c1_2 = document.querySelector("#c1_2");



console.log(caixa1.children[0]);
console.log(caixa1.children[caixa1.children.length - 1]);
console.log(caixa1.firstElementChild);
console.log(caixa1.firstElementChild);
console.log(caixa1.children);
console.log(caixa1.hasChildNodes());
console.log(cursos[0].hasChildNodes());
console.log(cursos[0].children); // return htmlCollection

if(cursos[0].children.length > 0) {
    console.log("possui filhos");    
}else {
    console.log("Não possui filhos");    
}

const possui_filhos = caixa1.children.length > 0 ? "possui flihos sim" : "Possui filhos não"
console.log(possui_filhos);

caixa1.firstElementChild.innerHTML = "HTML" //retona a div completa do primeiro filho
caixa1.children[1].innerHTML = "CSS"  

console.log("Pegando a div pai");
console.log(c1_2.parentNode);

console.log("Pegando a div avô");
console.log(c1_2.parentNode.parentNode);












