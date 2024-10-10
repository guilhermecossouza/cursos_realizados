class Banco {
    constructor() {
        this.saldo = 0 ;
    }

    saque(valor=0) {
        if (this.saldo === 0) {
            console.log(`Não pode efetuar saque saldo R$ ${this.saldo}`);        
        }

        if (valor > this.saldo) {
            console.log(`Saldo insuficiente. Vloe em conta R$ ${this.saldo}`);
        }

        this.saldo = this.saldo - valor

        console.log(`Saque autorizado no valor R$ ${valor}`);
    }

    deposito(valor=0) {
        if (valor === 0) {
            console.log(`Informe um vlor maior que 0`);
        }
        
        this.saldo = this.saldo + valor

        console.log(`Depósito aprovado no valor de R$ ${valor}`);
    }
}

let bancoInter = new Banco();
console.log(bancoInter.saldo);
bancoInter.deposito(333.50);
console.log(bancoInter.saldo);
bancoInter.saque(100.40);
console.log(bancoInter.saldo);

