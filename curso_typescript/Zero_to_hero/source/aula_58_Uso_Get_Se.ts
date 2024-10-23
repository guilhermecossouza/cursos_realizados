export {}

// ==> Exemplo 01 - Get e Set

class Pessoa {
    private _nome: string;
    private _idade: number;

    get nome(): string {
        return this._nome;
    }

    set nome(nome: string) {
        this._nome = nome;
    }

    get idade(): number {
        return this._idade;
    }

    set idade(idade: number) {
        this._idade = idade;
    }
}

const pessoa = new Pessoa();
pessoa.nome = "Guilherme";
pessoa.idade = 30;
console.log(pessoa);

// ==> Exemplo 02 - Get e Set

class Estudante {
    private _nome: string;
    private _idade: number;

    public get nome(): string {
        return this._nome;
    }

    public set nome(nome: string) {
        this._nome = nome;
    }

    public get idade(): number {
        return this._idade;
    }

    public set idade(idade: number) {
        this._idade = idade;
    }
}

const estudante = new Estudante();
estudante.nome = "Guilherme";
estudante.idade = 30;
console.log(pessoa);


// ==> Exemplo 03 - Get e Set

