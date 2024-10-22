/**
 * doc referência: https://www.typescriptlang.org/docs/handbook/basic-types.html#array
 */

// ==> Exemplo 01 - Uso de Colchetes:
let frutas:string[] = ["Macã","Melão","Melancia"];
console.log(frutas[0]);
console.log(frutas[2]);

// ==> Exemplo 02 - Array Object (Objeto Array):
let frutas1:Array<string> = ["Macã","Melão","Melancia"];
console.log(frutas1[0]);
console.log(frutas1[2]);

let carros:Array<string|number> = ["Palio", 2010, 10000]
console.log(carros);
console.log(carros[1]);

// ==> Exemplo 03 - Adicionando mais strings com método 'push'
let idiomas:Array<string> = ["Português", "Inglês", "Espanhol"]
console.log(idiomas);
idiomas.push("Francez");
console.log(idiomas);
idiomas.unshift("Japão");
console.log(idiomas);

// ==> Exemplo 04 - Identificar tamanho do array - método 'length'
console.log(idiomas.length - 1);

// ==> Exemplo 05 - Exemplo de Array com Spread Operator
let numeros:Array<number> = [1,2,3,4,5,6,7,8,9,10];
let maisNumeros:Array<number> = [13,14,15,16,17,18,19,20];
let numerosCompletos:Array<number> = [...numeros, ...maisNumeros]
console.log(numerosCompletos);
let correcaoArray:Array<number> = [...numeros, 11, 12, ...maisNumeros];
console.log(correcaoArray);

// ==> Exemplo 06 - Exemplo de Array com laço de iteração

let linguagemProgramacao:Array<string> = ["Java", "C#", "Python", "JavaScript"];

function funcaoLinguagem(linguagem:Array<string>) {
    for(let i = 0; i < linguagem.length; i++) {
        console.log(linguagem[i]);
    }

    linguagem.map((element, index) => {
        console.log(element + ' -- ' + index);
    });

    linguagem.forEach((element, index) => {
        if(index === 0) {
            linguagem[0] = "PHP"
        }
    });

    console.log(linguagem);
}

funcaoLinguagem(linguagemProgramacao)