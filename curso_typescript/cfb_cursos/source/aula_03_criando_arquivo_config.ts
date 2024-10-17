class Curso {

    canal = null;
    curso = null

    constructor(canal:any, curso:any) {
        this.canal = canal;
        this.curso = curso;
    }
}

let cursoMinistrado = new Curso("CFBCurso", "TypeScript");
console.log(`O nome do curso é ${cursoMinistrado.curso}`);
console.log(`O nome do canal é ${cursoMinistrado.canal}`);