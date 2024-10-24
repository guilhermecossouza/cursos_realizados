export{}

// ==> Exemplo 01 - Interfaces com extends
// interface Animal {
//     nome: string;
//     idade: number;
//     porte: string;
// }

// interface Cachorro extends Animal {
//     raca: string;
// }

// const chico: Cachorro = {
//     nome: "Chico",
//     idade: 3,
//     porte: "Pequeno",
//     raca: "Vira-lata"
// }

// console.log(chico)

// ==> Exemplo 02 - Extensão de Múltiplas Interfaces
interface Cachorro_01 {
    nome: string;   
}

interface Gato_01 {
    nome: string;   
}

interface Animal extends Cachorro_01, Gato_01 {
    idade: number;
    carnivoros: boolean;
}


const chico_01: Animal = {
    nome: "Chico",
    idade: 3,
    carnivoros: false
}

console.log(chico_01)

// ==> Exemplo 03 - Uso do Omit
interface Funcionario {
    id: number;
    nome: string;
    salario: number;
}

interface Desenvolvedor extends Omit<Funcionario, "id"> {
    id: string;
    linguagem: string;    
}

const programador: Desenvolvedor = {
    id: "r3@j.6qL0{$=",
    nome: "Guilherme",
    salario: 1000,
    linguagem: "Python"
}
console.log(programador)



// Exemplo 04 - Uso do pipe
