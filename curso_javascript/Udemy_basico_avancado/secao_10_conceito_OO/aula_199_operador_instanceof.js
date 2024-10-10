class Mamifero {
    constructor(patas) {
        this.patas = patas
    }
}

class Passaro {
    constructor(voua) {
        this.voua = voua
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


console.log(new Cachorro instanceof Mamifero)
console.log(new Cachorro instanceof Passaro)