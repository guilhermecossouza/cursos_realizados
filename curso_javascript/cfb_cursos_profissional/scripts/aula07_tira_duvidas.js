/**
 * difereça entre
 * ==
 * ===
 */

let num1 = 1 
let num2 = '1'
console.log(num1 == num2) //aqui ele vai comparar somente o caracter 1 não ligando se é inteiro ou string ou float e etc
//resultado true
console.log(num1 === num2)// já nesse caso ele vai comparar o caracter 1 eo tipo da variável se é string ou inteiro e etc
//resultado false

/** UTILIZANDO OBJETO  */
// Quando se trata de objeto ele avalia endereço de memória para os dois casos nesno o objeto sendo igual
let v1 = {nome: "guilherme"}
let v2 = {nome: "guilherme"}
console.log(v1 == v2) // fase
console.log(v1 === v2) // false
// Agora se fizer assim:
v2 = v1
console.log(v1 == v2) // true
console.log(v1 === v2) // true
//OBS: nesse caso a v2 agora em vez de endereço de memória ele tem é a referência do enderço de memória da v1

/** ENTRADA DE DADOS
 * no java scripit é diferente das linguagens convêncionais porque no Python temos o input() que recebe os dados no prompt 
 * e outras linguagens também tem.
 * Já no javascript ele também tem entrada de dados porêm ele precisa da parte gráfica ou browser
 */

let nome = prompt("Informe seu nome: ") // se rodar o codigo via terminal vai dar pau, más se rodar no browser ele vai abrir um prompt tipo o alert();
console.log(nome);

/**CURIOSIDADE 
 * Para ver em qual dispositivo o browser está sendo usado
 * console.log(navigator.userAgent.match(/nome_dispositico/));
*/
