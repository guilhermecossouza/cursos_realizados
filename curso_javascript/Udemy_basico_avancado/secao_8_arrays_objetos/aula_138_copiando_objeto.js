let carro = {
    marca: "Palio",
    cor: "Preto",
    porta: 4,
    motor: 1
}

let adicionais = {
    arCondicionado: true,
    direcaoHidraulica: true
}


//União de objetos, a orden vai seguir a criação -> herança

Object.assign(carro, adicionais)
console.log(carro);
Object.assign(adicionais, carro)
console.log(carro);


