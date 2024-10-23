export {}


// ==> Exemplo 01 - Propriedade readonly
class Funcionaro {
    readonly dataNascimento: Date;

    constructor(dataNascimento: Date) {
        this.dataNascimento = dataNascimento
    }
}

const funcionario = new Funcionaro(new Date(1984, 1, 28));
console.log(funcionario.dataNascimento.toLocaleDateString("pt-BR"));
//funcionario.dataNascimento = new Date(1988, 1, 28); -> erro propriedade somente de leitura


// ==> Exemplo 01 - Propriedade readonly (Interface)

interface Funcionaro01 {
    nome: string;
    email: string;
}

const funcionario01: Readonly<Funcionaro01> = {
    nome: "Guilherme",
    email: "pKsZk@example.com"
}

// funcionario01.email = "pKsZk@example.com";
// funcionario01.nome = "Guilherme";


const funcionario02: Funcionaro01 = {
    nome: "Guilherme",
    email: "pKsZk@example.com"
}

console.log(funcionario02);

funcionario02.nome = "zaca"
funcionario02.email = "zaca@zaca.com"

console.log(funcionario02);