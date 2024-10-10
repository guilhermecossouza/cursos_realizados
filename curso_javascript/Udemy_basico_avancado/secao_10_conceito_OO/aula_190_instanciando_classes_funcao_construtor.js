function criarCachorro(raca, patas, cor) {
    let cachorro = Object.create({});
    cachorro.raca = raca;
    cachorro.patas = patas;
    cachorro.cor = cor
    cachorro.latir = function() {
        console.log("AU AU");
    }
    return cachorro;
}

let viraLara = criarCachorro("Vira-lata", 4, "Caramelo");

viraLara.latir()
console.log(viraLara.cor)
