
let data = new Date();

enum dias{
    domingo = 0,
    segunda = 1,
    terca = 2,
    quarta = 3,
    quinta = 4,
    sexta = 5,
    sabado = 6,
}

// console.log(dias.domingo);
// console.log(dias["domingo"]);
// console.log(dias[1]);
// console.log(dias[data.getDay()]);

enum cores {
    branco = "#fff",
    preto = "#000",
    vermelho = "#f00",
    azul = "#00f",
    verde = "#0f0",
    amarelo = "#ff0",
}

// console.log(cores.branco);
// console.log(cores["branco"]);

enum tipoUsuario {
    USER,
    ADMIN,  
    SUPER,
}

// console.log(tipoUsuario.USER);
// console.log(tipoUsuario.ADMIN);
// console.log(tipoUsuario.SUPER);
// console.log(tipoUsuario[tipoUsuario.USER]);

let usuario:tipoUsuario;
usuario = tipoUsuario.USER;
console.log(tipoUsuario[usuario]);