let nome = ["Guilherme", "Kenia", "MariaVitória"]

console.log(nome)
console.log("======for======")
for (let index = 0; index < nome.length; index++) {
    console.log(nome[index] +" - "+ index)    
}
console.log("======forEach======")
nome.forEach((valor, chave) => console.log(valor+" - "+ chave))
console.log("======map======")
nome.map((valor, chave) => console.log(valor +" - "+ chave))
