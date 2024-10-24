export {}


// ==> Exemplo 01: Interface Simples
interface Pessoa {
    nome: string;
    sobreNome: string;
    idade: number;
}

const exibeNome = (pessoa: Pessoa): string =>  {
    return `${pessoa.nome} ${pessoa.sobreNome}, ${pessoa.idade}`
}

// function exibeNome(pessoa: Pessoa): string {
//     return `${pessoa.nome} ${pessoa.sobreNome}, ${pessoa.idade}`
// }

const guilherme = {
    nome: "Guilherme",
    sobreNome: "Cossouza",
    idade: 40
}

console.log(exibeNome(guilherme));

// ==> Exemplo 02: Interface com Propriedades Opcionais

interface Livro {
    titulo: string;
    autor: string;
    paginas?: number;
}

const livro: Livro = {
    titulo: "Livro 1",
    autor: "Autor 1"
}

console.log(livro);

const livro2: Livro = {
    titulo: "Livro 2",
    autor: "Autor 2",
    paginas: 100
}

console.log(livro2);

// ==> Exemplo 03: Interface com Propriedades de Somente Leitura e Opcionais
interface Carro {
    readonly modelo: string; //=> Somente de leitura
    ano: number;
    valor?: number;
}

const palio: Carro = {
    modelo: "Fiat",
    ano: 1997,
}

console.log(palio);

palio.ano = 2010;

console.log(palio);

const ferrai: Carro = {
    modelo: "Ferrari",
    ano: 2019,
    valor: 100000
}

console.log(ferrai);
//ferrai.modelo = "Ferrari Reborn"; -> Não pode ser modificar uma propriedade de somente leitura

const lamborini: Carro = {
    modelo: "Lamborghini",
    ano: 2017
}

console.log(lamborini);


// ==> Exemplo 04: Interface com implements Class

interface Animal {
    nome: string;
    idade: number;
    estaVivo: boolean;
    comer(tipoComida: string): void;
}

class Gato implements Animal {
    nome: string;
    idade: number;
    estaVivo: boolean;
    
    constructor(nome: string, idade: number, estaVivo: boolean) {
        this.nome = nome;
        this.idade = idade;
        this.estaVivo = estaVivo;
    }

    comer(tipoComida: string): void {
        console.log(`O ${this.nome} come ${tipoComida}`);
    }
}

const gato = new Gato("Gato", 2, true);
gato.comer("Ração");

// ==> Exemplo 05: Interfaces vs Alias Type