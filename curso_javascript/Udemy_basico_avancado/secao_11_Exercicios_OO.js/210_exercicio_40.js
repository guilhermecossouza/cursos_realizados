class Banco {
    constructor(saldoContaCorrente, saldoPolpanca, jurosPoupaca) {
        this.saldoContaCorrente = saldoContaCorrente;
        this.saldoPolpanca = saldoPolpanca;
        this.jurosPoupaca = jurosPoupaca;
    }

    depositar(valor=0) {
        if(valor > 0) {
            this.saldoPolpanca += valor - this.jurosPoupaca;
        }
    }

    transferir(valor=0) {
        if (valor > 0) {
            this.saldoContaCorrente += valor;
        }
    }

    saque(valor=0) {
        if (valor <= this.saldoContaCorrente) {
            const valorReal = new Intl.NumberFormat('pt-BR', {style: "currency", currency: "BRL"});
            console.log(`Valor autorizado no valor R$ ${valorReal.format(valor)}`);
        }
    }
}

class ContaEspecial extends Banco () {
    constructor(saldoContaCorrente, saldoPolpanca, jurosPoupaca) {
        super(saldoContaCorrente, saldoPolpanca, jurosPoupaca * 2)
    }
}