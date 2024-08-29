/**
 * 
 * aparâmetro rest são passagem de parametro onde vc não sabe a quantidade de parametro
 */

function soma(...valores) {
    let resulado = 0
    for(n of valores) {
        resulado+=n
    }
    return resulado;
}

console.log(soma(1,2,3));