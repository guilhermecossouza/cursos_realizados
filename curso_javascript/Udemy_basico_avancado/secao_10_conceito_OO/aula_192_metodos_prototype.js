function Cachorro(raca, patas, cor) {
    this.raca = raca;
    this.patas = patas;
    this.cor = cor;
}

Cachorro.prototype.latir = function() {
    return "AU AU";
}

const viraLata = new Cachorro("Vira-lata", 4, "Caramelo");

console.log(viraLata.cor);
console.log(viraLata.latir())