class Cachorro {
    constructor(raca) {
        this.raca = raca
    }
}
const viraLata = new Cachorro("Vira-lata");

const patas = Symbol()
Cachorro.prototype["patas"] = 4

console.log(Cachorro.prototype["patas"]);
