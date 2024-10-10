const cachorro = {
    raca: "s/r",
    uivar : function() {
        console.log("AUUUUUUUUUUUUUUUUUUUUUU");
    },
    rosnar: function() {
        console.log("GRRRRRRRRRRRRRRRRRRRRRRRR");
    },
    setRaca: function(raca){
        this.raca = raca;
    },
    getRaca: function() {
        return `A raça desse cachorro é ${this.raca}`
    }
}

console.log(cachorro.raca);
cachorro.setRaca("vira-lata");
console.log(cachorro.raca);
cachorro.setRaca("Pitbull");
console.log(cachorro.getRaca());
