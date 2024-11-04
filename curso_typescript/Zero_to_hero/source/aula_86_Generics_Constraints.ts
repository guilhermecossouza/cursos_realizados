export {}

//=> exemplo 01 Generics Constraints

interface Pessoa {
    nome: string;
    idade: number;
}

function obterPessoaIdadeMaiorQue<T extends Pessoa>(pessoa: T[], idade: number): T[] {
    return pessoa.filter((pessoa) => pessoa.idade > idade)
}

const pessoa: Pessoa[] = [
    {nome: "Guilherme", idade: 40},
    {nome: "Joaquim", idade: 30},
    {nome: "Joana", idade: 10},
    {nome: "Ana", idade: 50},
    {nome: "Maria", idade: 33},
    {nome: "Maria vit", idade: 11},
]

const dadosPessoa: Pessoa[] = obterPessoaIdadeMaiorQue<Pessoa>(pessoa, 49);
//console.log(dadosPessoa)



//=> exemplo 02 Generics Constraints

function juntarObjetos<U, V>(objeto1: U, objeto2: V) {
    return {...objeto1, ...objeto2}
}

const pessoa1 = juntarObjetos(
    {nome: "Guilherme",},
    {idade: 40, }
)
console.log(pessoa1)

//A baixo temos um erro que o type script aceita teme cuidao
const pessoa2 = juntarObjetos(
    {nome: "Guilherme",},
    40
)
console.log(pessoa2)

//solução
function juntarObjetos2<U extends object, V extends object>(objeto1: U, objeto2: V) {
    return {...objeto1, ...objeto2}
}

// Assim é validato o objeto a linha 55 não é um objeto
// const pessoa3 = juntarObjetos2(
//     {nome: "Guilherme",},
//     40
// )

const pessoa4 = juntarObjetos2(
    {nome: "Guilherme",},
    {idade: 40, }
)

console.log(pessoa4)





