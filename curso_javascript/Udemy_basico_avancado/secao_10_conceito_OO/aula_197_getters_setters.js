class Cachorro {
    constructor(raca, cor) {
        this.raca = raca
        this.cor = cor;
    }

    get getCor() {
        return `A cor do cachorro é ${this.cor}`;
    }

    set setCor(novaRaca) {
        this.cor = novaRaca
    }

    latir() {
        console.log("AU AU");
    }
}

let viraLata = new Cachorro("Vira-lata", "sem cor");
viraLata.setCor = "Caramelo";
console.log(viraLata.getCor);

