export { }

class Estudantes<T, U> {
    private id : T;
    private nome: U;

    constructor() {
        this.id = <T>0;
        this.nome = <U>"Guilherme";
    }

    setValor(id: T, nome: U): void {
        this.id = id;
        this.nome = nome
    }

    retornaValor(): void {
        console.log(`Identificação ${this.id}, nome ${this.nome}`)
    }
}

const estudante = new Estudantes<number, string>();
const estudanteSecundario = new Estudantes<string, string>();

estudante.setValor(1, "Guilherme");
estudanteSecundario.setValor("1", "Guilherme");

estudante.retornaValor();
estudanteSecundario.retornaValor();