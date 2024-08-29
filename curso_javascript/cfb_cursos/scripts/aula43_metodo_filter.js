/**
 * O Filter recebe 3 parâmetro opcionais:
 * 1° valor
 * 2° indice
 * 3° array
 */

// function maior_idade(valor) {
//     if(valor >= 18) {
//         return valor
//     }
// }

const idade = [15,20,13,25,13,95,100,80];

const maior = idade.filter((valor, indice, idade) => {
    if(valor >= 18) {
        return valor
    }
});


const menor = idade.filter((valor) => {
    if(valor < 18) {
        return valor
    }
});

console.log(idade);
console.log(maior);
console.log(menor);



