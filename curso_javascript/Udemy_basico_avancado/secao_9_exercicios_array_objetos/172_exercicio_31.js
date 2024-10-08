const nomes = ["Guilherme", "Kenia", "Hiago", "Gabriel", "Maria Vitória"];
const carros = ["Palio", "Civic", "Audi"]

totalElementos = (array) => {    
    return array.length < 5 ? "Poucos elementos" : "Muintos elementos"
}

console.log(totalElementos(carros));
console.log(totalElementos(nomes));