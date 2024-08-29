
// nessa função não há obrigatoriedade de informar o return
let resultado = (v1, v2)=>{return v1 + v2}
console.log(resultado(1, 1));

let resultado1 = (v1, v2) => v1 + v2
console.log(resultado1(2, 2));

//OBS: Neste caso é obrigatório
let resultado3 = (...valores) => {
    let resposta = 0
    for(num of valores) {
        resposta+= num
    }
    return resposta
}
console.log(resultado1(1, 2, 3, 5));



// /**
//  * Caso for passar um parâmetro só não precisa o ()
//  */

let nome = n => {return n}
console.log(nome("guilherme"));

// //também não há necessidade de adicionar o return
let add = num => num+10
console.log(add(1));

