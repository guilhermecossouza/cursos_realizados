/**Criando variável array e definido um tipo 
 * let cursos:String[]=[];
 * cursos.push("Python");
*/

//Especificando tipos de variáveis, ou seja pode receber somente os tipos definidos
//let vTeste:String|Number|boolean;
//Para definir todos os tipos a uma variável
let vTeste:any;
vTeste = "Guilherme";
console.log(`vTeste-> ${vTeste}`)
vTeste = 2024;
console.log(`vTeste-> ${vTeste}`)
vTeste = true;
console.log(`vTeste-> ${vTeste}`)

let cursos = ["JavaScript", "TypeScript"];
let valores = [10, 2, 21];

cursos.push("Python");
console.log(cursos)

valores.push(50);
console.log(valores)

vTeste = valores;
console.log(`vTeste-> ${vTeste}`)

const multTypes = ["Guilherme", 10, true]
console.log(multTypes)
multTypes.push(false)
multTypes.push("Kenia");
multTypes.push(30);
console.log(multTypes)

