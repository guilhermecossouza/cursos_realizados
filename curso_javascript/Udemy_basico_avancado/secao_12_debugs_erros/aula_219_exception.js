const saudacao = (nome) => {
    if(typeof nome !== "string") {
        throw new Error("Informe uma string")
    }

    console.log(`Seja bem vindo(a) ${nome}`);
}

saudacao("Guilherme");
saudacao(5);
