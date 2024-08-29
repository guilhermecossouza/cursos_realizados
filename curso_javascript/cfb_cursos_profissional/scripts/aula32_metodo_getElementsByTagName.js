const dc1 = document.getElementById("c1");
const dc2 = document.getElementById("c2");
const dc3 = document.getElementById("c3");
const dc4 = document.getElementById("c4");
const dc5 = document.getElementById("c5");
const dc6 = document.getElementById("c6");

const arrElementosDiv = [dc1, dc2, dc3, dc4, dc5, dc6]

const colecaoHtml = document.getElementsByTagName("div")

console.log(arrElementosDiv);
console.log(colecaoHtml);

console.log("");
console.log("");
console.log("Convertendo coloção para array");

const arrColecaoHtml = [...document.getElementsByTagName("div")] //Usando o spret
console.log(arrColecaoHtml);