export{}

// ==> Exemplo 01 - Type Guards: typeof
type alfanumerico = string | number;

function exibeTipo(a: alfanumerico, b: alfanumerico) {
    if(typeof a === "number" && typeof b === "number") {
        return a + b;
    }

    if (typeof a === "string" && typeof b === "string") {
        return a.concat(b);
    }

    throw new Error("Os valores devem ser do mesmo tipo");
}

console.log(exibeTipo(1, 2));
console.log(exibeTipo("1", "2"));
//console.log(exibeTipo("1", 2));



// ==> Exemplo 02 - Type Guards: instanceof
class Carro {
    public nome: string;
    public marca: string;

    constructor(nome: string, marca: string) {
        this.nome = nome;
        this.marca = marca;
    }
}

class Moto {
    public nome: string;
    public ano: number;

    constructor(nome: string, ano: number) {
        this.nome = nome;
        this.ano = ano;
    }
}

class Caminhao {
    public nome: string;
    public capacidade: number;

    constructor(nome: string, capacidade: number) {
        this.nome = nome;
        this.capacidade = capacidade;
    }
}

function detalheVeiculo(veiculo: Carro | Moto | Caminhao) {
    if(veiculo instanceof Carro) {
        return `Carro: ${veiculo.nome} - ${veiculo.marca}`;
    }else if(veiculo instanceof Moto) {
        return `Moto: ${veiculo.nome} - ${veiculo.ano}`;
    }else {
        //throw new Error("Esse veiculo não existe");
    }
}


const carro = new Carro("Palio", "Fiat");
const moto = new Moto("Honda", 2010);
const caminhao = new Caminhao("Caminhão", 10);

console.log(detalheVeiculo(carro));
console.log(detalheVeiculo(moto));
console.log(detalheVeiculo(caminhao));

// ==> Exemplo 03 - Type Guards: in
interface Animal {
    grupo: string;
}

class Peixe implements Animal {
    public grupo: string;
    public corPeixe: string;

    constructor(grupo: string, corPeixe: string) {
        this.grupo = grupo;
        this.corPeixe = corPeixe;
    }
}

class Passaro implements Animal {
    public grupo: string;
    public corPena: string;

    constructor(grupo: string, corPeixe: string) {
        this.grupo = grupo;
        this.corPena = corPeixe;
    }
}


function nadar(grupo: String) {
    console.log(`O grupo ${grupo} pode nadar`);
}

function voar(grupo: String) {
    console.log(`O grupo ${grupo} pode voar`);
}

function mover(animal: Animal) {
    if("corPeixe" in animal) {
        nadar((animal as Peixe).grupo)
    }else if("corPena" in animal) {
        voar((animal as Passaro).grupo);
    }
}


const peixe = new Peixe("Peixe", "Cinza");
const passaro = new Passaro("Passaro", "Verde");

mover(peixe);
mover(passaro);