/**
 * push -> acrescenta mais uma elemento
 * pop -> remove um elemento
 */

let nomes = ["Guilherme", "Kenia", "Hiago"];
let elementoRemovido = nomes.pop();
console.log(elementoRemovido)
console.log(nomes)
nomes.push("Jose")
console.log(nomes)
nomes.splice(1,1)
console.log(nomes)

