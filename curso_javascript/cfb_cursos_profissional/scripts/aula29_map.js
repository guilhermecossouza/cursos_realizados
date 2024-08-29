/**
 * O método map recebe dois parametros
 * 1° elemento que são os elementos do array no caso html, css e etc..
 * 2° é o indice ou seja 0,1,2 e etc..
 */
const cursos = ["html", "css", "javascript", "react", "python"];

cursos.map((ele, pos)=> {
    console.log("Curso:" + ele + ", que está na posição: "+ pos);
});

console.log("");
console.log("");

const c = cursos.map((el, po)=>{
    return el
});

console.log(c);