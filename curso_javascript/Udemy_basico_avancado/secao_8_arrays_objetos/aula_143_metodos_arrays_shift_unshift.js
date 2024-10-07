let frutas = ["Maçã", "Melão", "Melancia"]
console.log(frutas)
console.log("==shift-> Remove o primeiro elemento==")
let frutaRemovida = frutas.shift()
console.log(frutas);
let frutas2 = frutas
console.log("==unshift-> Adiciona na primeira posição do array==")
frutas2.unshift("Maçã")
console.log(frutas2)