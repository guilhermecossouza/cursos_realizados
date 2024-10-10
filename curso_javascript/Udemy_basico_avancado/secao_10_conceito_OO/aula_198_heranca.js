class Mamifero {
    constructor(patas) {
        this.patas = patas
    }
}

class Cachorro extends Mamifero {
    constructor(raca, cor, patas) {
        super(patas, patas)
        this.raca = raca;
        this.cor = cor
    }

    latir() {
        console.log("AU AU");
    }
}

let viraLata = new Cachorro("Vira-lata", "Caramelo", 4)

console.log(viraLata.patas)
viraLata.patas = 5
console.log(viraLata.patas)

viraLata.latir()

