const pessoa = {
    "nome": "Guilherme",
    "idade": 40,
    "profissao": "Programador",
    "hobbies": ["ler", "jogar", "programar"]
}

console.log(`Nome: ${pessoa.nome}`);
console.log(`Idade: ${pessoa.idade}`);
console.log(`Profissão: ${pessoa.profissao}`);
pessoa.hobbies.map((elementos) => {
    console.log(`Hobbies: ${elementos}`)
})
