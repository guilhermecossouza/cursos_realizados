const pessoa = {
    "nome": "Guilherme",
    "idade": 40,
    "profissao": "Programador",
    "hobbies": ["jogar", "ler", "filmes"]
}

console.log(typeof pessoa);
console.log(typeof JSON.stringify(pessoa)); 

let jsonTexto = JSON.stringify(pessoa)
console.log(jsonTexto); //convert json para string

let jsonObject = JSON.parse(jsonTexto)
console.log(jsonObject);



