"use strict"
/** 
 *  A declaração [var] não importa onde será criada ela será vista, não apresentará um erro e sim um undefined ex:
 * console.log(nome) -> undefined
 * var nome = "guilherme"
 * console.log(nome) -> guilherme
 * if(1 + 1 === 10) {
 *  console.log(nome) -> undefined 
 * }
 * 
 * Já a declaração let segue a premissas das linguagens de programação ela só é vista apartir de sua declaração
 * console.log(nome) -> erro
 * if(1 + 1 === 2) {
 *  console.log(nome) -> erro 
 * }
 * 
 * let nome = "guilherme"
 * console.log(nome) -> guilherme
 *  
 * 
 * const -> a declaração constante garante que o valor da variável não será alterada.
 * caso tente alterar da eero
 */


console.log(nome); //-> undefined
if(true) {
    console.log(nome); //-> undefined
}
var nome = "guilherme"
console.log(nome); //-> guilherme


// console.log(fruta); // -> ReferenceError: Cannot access 'fruta' before
// if (true) {
//     console.log(fruta); // -> ReferenceError: Cannot access 'fruta' before
// }

let fruta = "maça"
console.log(fruta); // -> maça
if (true) {
    console.log(fruta); // -> maça
}

const carro = "Palio"
console.log(carro);

carro = "monza" // ->TypeError: Assignment to constant variable.
console.log(carro); // ->TypeError: Assignment to constant variable.












