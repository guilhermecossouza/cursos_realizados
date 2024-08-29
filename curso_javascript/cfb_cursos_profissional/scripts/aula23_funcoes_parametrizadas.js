
"use script"

let valor = 10

function soma(v1) {
    return valor + v1;
}

console.log(soma(10));


function soma(v1, v2, v3) {
    let par_impar
    let res_soma = v1 + v2 + v3 
    if(res_soma % 2 === 0) {
        par_impar = "par"
    }else {
        par_impar = "impar"
    }    
    return par_impar
}

let resultado1 = soma(1, 2, 4);
console.log(resultado1);

let numeros = [3, 4, 5]
let resultado2 = soma(...numeros)
console.log(resultado2);


function get_nome(nome="Kenia") {
    return nome
}

console.log(get_nome("Guilherme"));
console.log(get_nome());