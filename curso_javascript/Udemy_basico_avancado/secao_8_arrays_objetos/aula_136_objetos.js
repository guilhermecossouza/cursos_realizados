const pessoa = {
    nome: "Guilherme",
    profissao: "Programador",
    idade: 40,
    andar: () => {
        console.log("estou andando");
    },
    parar: function () {
        console.log("Parado")
    }
};

//propriedades
console.log(pessoa.nome);
console.log(pessoa.profissao);
console.log(pessoa.idade);
pessoa.andar();
pessoa.parar();