function aluno(nome, nota) {
    this.nome = nome
    this.nota = nota

    this.dados = function() {
        setTimeout(function(){
            /**
             * Saída undefined porque ao declarar essa função o this
             * passou a reprentar está função e não a função pai
             * solução está na função a baixo usando arrow function
             */
            console.log(this.nome);// undefined 
            console.log(this.nota);// undefined
        }, 3000);
    }

    this.dados1 = function() {
        setTimeout(() => {
            /**
             * Usando arrow function conseguimos com que o this represente a classe pai
             */
            console.log(this.nome);
            console.log(this.nota);     
        }, 3000);
    }
}

const dados_alunos = new aluno("guilherme", 7.5);

dados_alunos.dados();
dados_alunos.dados1();