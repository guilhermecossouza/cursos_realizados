const capacidadeTexto = (texto="") => {
    if (texto.length >= 10) {
        console.log("texto muito longo");
    }else {
        console.log("texto dentro do limite");
    }
}

capacidadeTexto("Meu nome é Guilherme");