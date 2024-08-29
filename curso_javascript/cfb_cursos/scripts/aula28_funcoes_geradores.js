"use script"

/**
 * O Yield é o retorno está função é uma função controladora, ou seja ela conrola a saída
 */

function* cores() {
    yield "Vermelho"
    yield "Verde"
    yield "Azul"
}

const itc = cores()

console.log(itc);
console.log(itc.next().value); // Vermelho
console.log(itc.next().value); // Verder
console.log(itc.next().value); // Azul
console.log(itc.next().value); // undefined

console.log("");
console.log("");


function* perguntas() {
    let nome = yield "Qual seu nome? "
    let esporte = yield "Qual o seu esporte favorito? "
    return "Seu nome é "+ nome + ", e seu esporte favorito é "+ esporte
}

const itp = perguntas()

console.log(itp.next().value);
console.log(itp.next("zaca").value);
console.log(itp.next("zacazaca").value);



function* contador() {
    let i = 0
    while(true) {
        yield i++
    }
}

const it_contador = contador()

console.log(it_contador.next().value);// 0
console.log(it_contador.next().value);// 1
console.log(it_contador.next().value);// 2

console.log("");
console.log("");

for(let i = 0; i < 10; i++) {
    //aqui vai dar a sequência
    console.log(it_contador.next().value); // 3, 4, 5, 6 e etc...
}
