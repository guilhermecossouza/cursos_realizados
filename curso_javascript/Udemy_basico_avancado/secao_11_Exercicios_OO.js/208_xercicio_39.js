class Carro {
    constructor(marca, cor, gasolina, restante) {
        this.marca = marca;
        this.cor = cor;
        this.gasolina = gasolina;
        this.restante = restante;
    }

    dirigir() {
        let contador = 0
        for(let y = 650; y >= 0; y--) {
            if(contador === 13) {
                contador = 0;
                this.gasolina -= 1;
            }

            if (this.gasolina === 10 ) {
                console.log("Precisa abastecer o carro");
            }
            
            contador += 1 
        }
    }
}

let palio = new Carro("Palio", "Azul", 48, 0);
palio.dirigir()