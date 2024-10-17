let dados = {
    nome: "Guilherme",
    idade: 30,
    status: true,
    ola:() => console.log("ola"),
    info: (p:string) => console.log(p)
}
console.log(typeof(dados));
console.log(dados.nome);
dados.nome = "Kenia"
console.log(dados.nome);
dados.ola();
dados.info("teste");
