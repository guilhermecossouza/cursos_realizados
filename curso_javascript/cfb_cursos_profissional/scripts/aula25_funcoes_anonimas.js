/**
 * funcção anonima não precisa ter um nome a sua declaração
 * más precisa estar associada a uma variável
 */

let resulatdo = function(v1=0, v2=0) {return v1 + v2}

console.log(resulatdo(3+3));

let resultado2 = function(...valores){
    let resposta = 0
    for(num of valores) {
        resposta+=num
    }
    return resposta
}

console.log(resultado2(1,2,3,4));

/**
 * funcção contrutor para oprações simples
 * tem que ser passado os parametro e o corpo da função
 */

let resultado3 = new Function("v1", "v2", "return v1 + v2")
console.log(resultado3(5, 6));