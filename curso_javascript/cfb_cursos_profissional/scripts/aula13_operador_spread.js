/**
 * spread (espalhar) em uma array [1,2,3]
 * [...array] -> 1,2,3
 */


let n1 = [10, 11, 20, 30]
let n2 = [11, 21, 31, 41, 51, 61]

//copiando um array
let n3 = n1
console.log(n3);
let n4 = [...n1]
console.log(n4);

//concatenção de arrays
let n5 = [n1,n2] //-> ele vai gerar um array, com dois arrys dentro
console.log(n5);
let n6 = [...n1,...n2] // Agora sim um concatenação de arrays, ou seja um array com todos os valores de 
console.log(n6);


// somando valores de uma array
const soma=(v1,v2,v3)=>{
    return v1 + v2 + v3
}

console.log(soma(1,2,3));

const n7 = [5, 5, 5]
console.log(soma(...n7));

const n8 = [5, 5, 5, 1]
console.log(soma(...n8));
