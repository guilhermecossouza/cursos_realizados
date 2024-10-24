export{}


// ==> Exemplo 01
class Animal {
    public mover(distancia:number = 0) {
        console.log(`O animal se moveu ${distancia}m.`)
    }
}

class Cachorro extends Animal {
    public latir() {
        console.log("AU AU");
    }
}

const cachorro = new Cachorro();
cachorro.mover(10);
cachorro.latir();


// ==> Exemplo 02
class Pessoa {
    private nome: string;
    private sobreNome: string;

    constructor(nome: string, sobreNome: string) {
        this.nome = nome;
        this.sobreNome = sobreNome;
    }

    get nomeCompleto(): string {
        return `${this.nome} ${this.sobreNome}`;
    }

    get primeiroNome(): string {
        return this.nome;
    }
}

class Funcionario extends Pessoa {
    private funcao: string;

    constructor(nome: string, sobreNome: string, funcao: string) {
        super(nome, sobreNome);
        this.funcao = funcao
    }

    get funcaoTrabalho(): string {
        return this.funcao;
    }
}

const funcionario = new Funcionario("Guilherme", "Costa", "Programador");
console.log(funcionario.nomeCompleto);
console.log(funcionario.primeiroNome);
console.log(funcionario.funcaoTrabalho);