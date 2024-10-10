class Cachorro {
    constructor(raca, patas, cor) {
        this.raca = raca;
        this.patas = patas;
        this.cor = cor;
    }
}

let viraLata = new Cachorro("Vira-lata", 4, "Caramelo");

console.log(viraLata.raca);
console.log(viraLata.patas);
console.log(viraLata.cor);
