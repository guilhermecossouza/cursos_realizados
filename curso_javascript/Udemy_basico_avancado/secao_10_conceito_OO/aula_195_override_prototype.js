class Cachorro {
    constructor(raca) {
        this.raca = raca
    }
}

const viraLata = new Cachorro("Vira-lata");

Cachorro.prototype.raca = "SRD";

console.log(viraLata.raca);
console.log(Cachorro.prototype.raca);