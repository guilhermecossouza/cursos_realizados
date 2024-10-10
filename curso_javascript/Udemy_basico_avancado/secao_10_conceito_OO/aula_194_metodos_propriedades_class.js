class Cachorro {
    constructor (raca){
        this.raca = raca;
    }

    latir() {
        console.log("AU AU");
    }
}

Cachorro.prototype.patas = 4;

let viraLata = new Cachorro("Vira-lata");

console.log(viraLata.patas);
viraLata.latir()