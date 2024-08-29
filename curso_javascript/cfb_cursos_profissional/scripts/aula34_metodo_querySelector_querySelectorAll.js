const query_primeira_div = document.querySelector("div") // vai pegar a primeira ocorrência
console.log(query_primeira_div);

const query_todas_divs = document.querySelectorAll("div") // vai pegar a todas ocorrência
console.log(query_todas_divs);

console.log("");
console.log("");
console.log("Convertendo o query selector em array");

const arrQuery_todas_divs = [...document.querySelectorAll("div")]
console.log(arrQuery_todas_divs);
console.log("");
console.log("");
//Para pegar de uam classe expecifica usa o .(ponto)
const todos_elementos_classe_curso = [...document.querySelectorAll(".curso")]
console.log(todos_elementos_classe_curso);

const todos_elementos_classe_c1 = [...document.querySelectorAll(".c1")]
console.log(todos_elementos_classe_c1);

const todos_elementos_classe_c2 = [...document.querySelectorAll(".c2")]
console.log(todos_elementos_classe_c2);

// Pegando o elemento pelo id
const elemento_pelo_id = document.querySelector("#c1");
console.log(elemento_pelo_id);

// Para pegar 2 elementos
const mais_elementos_diferentes = document.querySelectorAll("div, p");
console.log(mais_elementos_diferentes);

//pegando todos os elementos que contêm class
const comente_quem_tem_class = document.querySelectorAll("div[class]")
console.log(comente_quem_tem_class);

//pegando todos os elementos que contêm id
const comente_quem_tem_id = document.querySelectorAll("div[id]")
console.log(comente_quem_tem_id);

//Pegar elementos dento de elementos
const pegando_elementos_dentro_de_elementos = document.querySelectorAll("div > p")
console.log(pegando_elementos_dentro_de_elementos);
