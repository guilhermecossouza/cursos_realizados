export{}

// ==> Exemplo 01: Propriedade estatica
class Funcionario {
    static contratacoes: number = 0;
    private nome: string;
    private sobreNome: string;
    private titulo: string;

    constructor(nome: string, sobreNome: string, titulo: string) {
        this.nome = nome;
        this.sobreNome = sobreNome;
        this.titulo = titulo;
        Funcionario.contratacoes++;
    }    
}

const funcionario = new Funcionario("Guilherme", "Costa", "Programador");
const funcionario2 = new Funcionario("Kenia", "Costa", "Programador");
const funcionario3 = new Funcionario("Gabriel", "Costa", "Programador");

//console.log(Funcionario.contratacoes);

// ==> Exemplo 02: metodo estatico
class Funcionario02 {
    static contratacoes: number = 0;
    private nome: string;
    private sobreNome: string;
    private titulo: string;

    constructor(nome: string, sobreNome: string, titulo: string) {
        this.nome = nome;
        this.sobreNome = sobreNome;
        this.titulo = titulo;
        Funcionario02.contratacoes++;
    } 
    
    public static retornaContratacoes(): number {
        return Funcionario02.contratacoes;
    }
}

const func01 = new Funcionario02("Guilherme", "Costa", "Programador");
const func02 = new Funcionario02("Kenia", "Costa", "Programador");
const func03 = new Funcionario02("Gabriel", "Costa", "Programador");

//console.log(Funcionario02.retornaContratacoes());


//exemplo 03
type Raca = "Vira-lata" | "Poodle" | "Labrador";

class Cachorro {
    public nome: string;
    public idade: number;
    public racas: Raca[];
    public static QTD_CACHORROS_VENDIDOS: number = 0;

    constructor(nome: string, idade: number, racas: Raca[]) {
        this.nome = nome;
        this.idade = idade;
        this.racas = racas;
        Cachorro.QTD_CACHORROS_VENDIDOS++;
    }

    public exibeInformacao(): void {
        console.log(`O cachorro ${this.nome} tem ${this.idade} anos e sua raca é ${this.racas}`);
    }
}

const cachorro_01 = new Cachorro("Rex", 5, ['Labrador']);
const cachorro_02 = new Cachorro("Pipoca", 3, ['Labrador']);
const cachorro_03 = new Cachorro("Toto", 1, ['Vira-lata']);
const cachorro_04 = new Cachorro("Paçoca", 1, ['Vira-lata']);
const cachorro_05 = new Cachorro("Chico", 1, ['Vira-lata']);

console.log(Cachorro.QTD_CACHORROS_VENDIDOS);
