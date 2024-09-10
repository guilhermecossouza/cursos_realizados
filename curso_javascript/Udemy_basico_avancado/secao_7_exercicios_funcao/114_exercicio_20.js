function permicaoFazerAutoEscola(idade=0) {
    if (idade >= 18) {
        console.log("Pode realizar as aulas");        
    } else {
        console.log("Não pode realizar as aulas");        
    }
}

permicaoFazerAutoEscola(18);
permicaoFazerAutoEscola(20);
permicaoFazerAutoEscola(16);
permicaoFazerAutoEscola();