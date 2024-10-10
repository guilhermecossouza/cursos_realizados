function Cachorro(raca, patas, cor) {
    this.raca = raca;
    this.patas = patas;
    this.cor = cor;
    this.latir = function() {
        console.log("AU AU");
    }
}

let viraLata = new Cachorro("Vira-lata", 4, "Caramelo");
viraLata.latir();
console.log(viraLata.raca);