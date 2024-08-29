/**OPERADORES 
 * | + -> soma
 * | - -> subitração
 * | / -> divisão
 * | * -> Multipicação
 * | % -> resto da divisão
 * | ++ -> operador de atribuição ou incremento poder ser assim também +=
 * | -- -> operador de decremento pode ser assim também -= 
 * OBS:
 *  sempre será somado o que esta dentro do () primeiro 
 * Ordem de precedência nas operações:
 *  1 -> *
*/

/**
 * podemos declarar variáveis de 2 geitos
 * assim:
 *  let num1 = 0;
 *  let num2 = 0;
 * ou assim:
 *  let num1 = 0, num2 = 0;
 */

let num1 = 0;
let num2 = 0;
let resp = 0;

num1 = 10
num2 = 5
resp = num1 + num2
console.log(resp);
resp = (num1 - num2) * 2
console.log(resp);
resp = num1 + num2 * 2
console.log(resp);
num1 *= 2
console.log(num1);
