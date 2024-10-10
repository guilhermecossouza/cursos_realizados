let cachorro = {
    raca: "SRD",
    setRaca: function(raca) {
        this.raca = raca;
    },
    getRaca: function() {
        return `A raça é: ${this.raca}`;
    }
}

let pastorAlemao = Object.create(cachorro);
pastorAlemao.setRaca("Pastor Alemão");
console.log(pastorAlemao.getRaca());

let viraLata = Object.create(cachorro);
viraLata.setRaca("Caramelo")
console.log(viraLata.getRaca())