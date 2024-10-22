/**
 * doc referência: https://www.typescriptlang.org/docs/handbook/basic-types.html#tuple
 */

// ==> Exemplo 01 - Uso simples de Tuplas em TypeScript
let pessoa: [string, string, number];
pessoa = ["Guilherme", "Programador", 40];
//pessoa = [40, "Programador", "Guilherme"]; Erro! respeite a ordem passada na tupla 
console.log(pessoa);

// ==> Exemplo 02 - Acessando o valor da Tupla
pessoa = ["Guilherme", "Programador", 40];
console.log(pessoa[1]);

// ==> Exemplo 03 - Outra forma de usar Tuplas em TypeScrit (com labels)
let pessoa1:[nome:string, profissao:string, idade:number];
pessoa1 = ["Guilherme", "Programador", 40];
console.log(pessoa1);

// ==> Exemplo 04 - Usando Tuplas com Spread Operator
let listaFrutas:[string, ...string[]];
listaFrutas = ["Maça", "Banana", "Laranja", "Uva", "Abacaxi", "Melancia", "Limão", "Cereja"];
console.log(listaFrutas);
console.log(listaFrutas[4]);

//==> Exemplo 05 - Lista Heterogênea de Tupla:
let listaFrutas1:[number, boolean, ...string[]];
listaFrutas1 = [5, true, ...listaFrutas]
console.log(listaFrutas1);

// ==> Exemplo 06 - Uso de função com Tuplas
function listarPessoas(nomes:string[], idade:number[]) {
    return [...nomes, ...idade]
}
console.log(listarPessoas(["Guilherme", "Kenia"], [40, 39]));

// ==> Exemplo 07 - Labeled Tuples com Spread Operator numa função
type Nome = | [primeiroNome: string, sobreNome: string] | [primeiroNome: string, nomeDoMeio: string, sobreNome: string];
function criarPessoa(...nome: Nome){
    return [...nome];
}
console.log(criarPessoa("Guilherme", "Souza"));
console.log(criarPessoa("Guilherme", "Costa", "Souza"));