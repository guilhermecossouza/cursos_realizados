export{}

abstract class Funcionario {
    private nome: string
    private sobreNome: string

    constructor(nome: string, sobreNome: string) {
        this.nome = nome;
        this.sobreNome = sobreNome;
    }

    abstract retornaSalario(): number;

    get nomeCompleto(): string {
        return `${this.nome} ${this.sobreNome}`;
    }

    public emitirContracheque(): string {
        return `${this.nomeCompleto} - Salário: R$${this.retornaSalario()}`
    }
}

class FuncionarioCLT extends Funcionario {
    private salario: number;
    constructor(nome: string, sobreNome: string, salario: number) {
        super(nome, sobreNome);
        this.salario = salario;
    }

    public retornaSalario(): number {
        return this.salario
    }

}


class FuncionarioPJ extends Funcionario {
    private valorHora: number;
    private horasTrabalhadas: number;

    constructor(nome: string, sobreNome: string, valorHora: number, horasTrabalhadas: number) {
        super(nome, sobreNome);
        this.valorHora = valorHora;
        this.horasTrabalhadas = horasTrabalhadas;
    }

    public retornaSalario(): number {
        return this.valorHora * this.horasTrabalhadas
    }
}

const funcionarioCLT = new FuncionarioCLT('Guilherme', 'Costa', 3500.00);
const funcionarioPJ = new FuncionarioPJ('Guilherme', 'Costa', 200.00, 160);

console.log(funcionarioCLT.retornaSalario());
console.log(funcionarioPJ.retornaSalario());
