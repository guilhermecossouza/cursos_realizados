export {}

// ==> Exemplo 01 - Classes
class Pessoa {
    nome: string;
    sobreNome: string;

    constructor(nome: string, sobreNome: string) {
        this.nome = nome;
        this.sobreNome = sobreNome;
    }

    nomeCompleto (): string {
        return `${this.nome} ${this.sobreNome}`;
    }
}

const pessoa = new Pessoa('Guilherme', 'Costa');
console.log(pessoa.nomeCompleto())

// ==> Exemplo 02 - Classes (sem construtor)
class Estudante {
    codigoEstudante: number;
    nomeEstudante: string;
}

const estudante = new Estudante();
estudante.codigoEstudante = 12548;
estudante.nomeEstudante = "Guilherme Costa";

console.log(estudante);
console.log(estudante.nomeEstudante);


// ==> Exemplo 03 - Classes (com construtor)
class Estudante_3 {
    codigoEstudante: number;
    nomeEstudante: string;

    constructor(codigoEstudante: number, nomeEstudante: string) {        
        this.codigoEstudante = codigoEstudante; 
        this.nomeEstudante = nomeEstudante;
    }
}

const estudante_3 = new Estudante_3(12548, "Guilherme Costa");
console.log(estudante_3);
console.log(estudante_3.nomeEstudante);


