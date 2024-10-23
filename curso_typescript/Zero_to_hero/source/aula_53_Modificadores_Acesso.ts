export {}

//=> exemplo private em classes
class Estudante {
    private codigoEstudante: number;
    public nomeEstudante: string;

    constructor(codigoEstudante: number, nomeEstudante: string) {
        this.codigoEstudante = codigoEstudante;
        this.nomeEstudante = nomeEstudante
    }
}

// const estudante = new Estudante(12548, "Guilherme Costa");
// console.log(estudante);
// console.log(estudante.nomeEstudante);
//console.log(estudante.codigoEstudante); => Erro


//=> exemplo private em classes
class Estudante_2{
    private codigoEstudante: number;
    private nomeEstudante: string;
    private loginEstudante: string;
    protected emailEstudante: string;
    protected status: boolean

    constructor(codigoEstudante: number, nomeEstudante: string, loginEstudante: string, emailEstudante: string, status: boolean) {
        this.codigoEstudante = codigoEstudante;
        this.nomeEstudante = nomeEstudante
        this.loginEstudante = loginEstudante
        this.emailEstudante = emailEstudante
        this.status = status
    }
    
    protected getNomeEstudante() {
        return this.nomeEstudante
    }
}

class MatriculaAula extends Estudante_2 {
    
    constructor(codigoEstudante: number, nomeEstudante: string, loginEstudante: string, emailEstudante: string, status: boolean) {
        super(codigoEstudante, nomeEstudante, loginEstudante, emailEstudante, status)    
    }

    public matricular() {
        if(this.status) {
            console.log(`Aluno ${this.getNomeEstudante()} matriculado com sucesso!`)
            console.log(`Enviando e-mail para o aluno ${this.emailEstudante}`)
        }
    }
}

const matricula = new MatriculaAula(12548, "Guilherme Costa", "guilherme123", "Y0W2t@example.com", true)
matricula.matricular()



