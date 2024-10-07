const carros = ["Civic", "Fiat", "Palio", "Uno", "Audi", "BMW"]

//Para localizar algo denro do array lembrando que é válido o camelcase
console.log(carros.includes("Palio")) // -> true
console.log(carros.includes("palio")) // -> false
console.log(carros.includes("Chevette")) // -> false