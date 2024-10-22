/**
 * doc referência: https://www.typescriptlang.org/docs/handbook/2/objects.html
 */

// ==> Exemplo 01 -> Exemplo básico do uso do Type Object
const usuario = {
    nome: "Guilherme",
    sobreNome: "Costa",
    idade: 34,
}
//console.log(usuario);

// ==> Exemplo 02 -> object como parâmetros de função (eles podem ser anônimos)
function onbording01(funcionario: {nome: string, cargo: string}) {
    return `Seja bem vindo ${funcionario.nome}`
}
onbording01({nome: "Guilherme", cargo: 'Programador'});

// ==> Exemplo 03 -> object nomeados
interface Pessoa {
    nome:string,
    profissao: string,
    cargo?: string
}

function onbording02(pessoa: Pessoa) {
    return `Seja bem vindo ${pessoa.nome}, e sua profissão é ${pessoa.profissao}`;
}
onbording02({nome: "Guilherme", profissao: 'Programador'});

// ==> Exemplo 04 -> object como type alias
type Pessoa03 = {
    nome:string,
    profissao: string,
    linguagem: string,
}
function onbording03(pessoa: Pessoa03) {
    return `Seja bem vindo ${pessoa.nome}, e sua profissão é ${pessoa.profissao}, e trabalhará coma a linguagem ${pessoa.linguagem}`;
}
onbording03({nome: "Guilherme", profissao: 'Programador', linguagem: "Python"});

// ==> Exemplo 05 -> usando optional no object
interface Pessoa04 {
    nome:string,
    profissao: string,
    linguagem: Array<string>,
    email?: string
}
function onbording04(pessoa: Pessoa04) {
    return `Seja bem vindo ${pessoa.nome}, e sua profissão é ${pessoa.profissao}, e trabalhará coma a linguagem ${pessoa.linguagem} e o se e-mail ${pessoa.email}`;
}

onbording04({nome: "Guilherme", profissao: 'Programador', linguagem: ["Python", "Javascript"]});
onbording04({nome: "Guilherme", profissao: 'Programador', linguagem: ["Python", "Javascript"], email: "pKsZk@example.com"});

// ==> Exemplo 06 -> Propriedade 'readonly' (se deseja proibir que os devs não modifiquem um determinado objeto use o '
//readonly)

interface Pessoa05 {
    nome: string,
    profissao: string,
    linguagem: Array<string>,
    readonly email: string,
}

function onbording05(pessoa: Pessoa04) {
    return `Seja bem vindo ${pessoa.nome}, e sua profissão é ${pessoa.profissao}, e trabalhará coma a linguagem ${pessoa.linguagem} e o se e-mail ${pessoa.email}`;
}
//console.log(onbording05({nome: "Guilherme", profissao: 'Programador', linguagem: ["Python", "Javascript"], email: "pKsZk@example.com"}));

// ==> Exemplo 07 -> tipos de extensões (heranças)
interface Mae {
    nome: string
}

interface Pai {
    sobreNome: string;
}

interface Filho extends Mae, Pai {
    idade: number
}

const filho: Filho = {
    nome: "Guilherme",
    sobreNome: "Costa",
    idade: 34
}

//console.log(filho);

// ==> Exemplo 08 -> Tipos de Interseções
interface Cachorro {
    tipo: string;
}

interface Gato {
    tipo: string;
}

type Animal = Cachorro & Gato;


// Exemplo 09 - Generic Objects
type Usuario = {
    nome: string;
    email: string;
    cargo: string
}

type Admin = {
    nome: string;
    email: string;
    admin: boolean;
}

const usuarioSistema: Usuario = {
    nome: "Guilherme",
    email: "pKsZk@example.com",
    cargo: "Programador"
}

const AdminSistema: Admin = {
    nome: "Guilherme",
    email: "pKsZk@example.com",
    admin: true
}

function acessoSistema<T>(usuario: T): T {
    return usuario    
}


console.log(acessoSistema<Usuario>(usuarioSistema))
console.log(acessoSistema<Admin>(AdminSistema))



