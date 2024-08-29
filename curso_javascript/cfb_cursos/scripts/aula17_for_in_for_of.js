let numeros = [10, 20, 30, 40, 50, 60]

for(let i = 0; i < numeros.length; i++){
    console.log("posição "+ i + " = " + numeros[i]);
}

console.log("");
console.log("");

/**
 * A diferença entre for in e for of é
 * O in retorna a posição do array
 * O of traz o valor que está dentro da posição do array
 */

for(nun in numeros) {
    console.log("posição "+ nun + " = " + numeros[nun]);
}

console.log("");
console.log("");

for(num1 of numeros) {
    console.log("Valor da posição do arry = "+ num1);
}
