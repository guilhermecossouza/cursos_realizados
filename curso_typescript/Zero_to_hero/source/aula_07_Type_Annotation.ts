/* eslint-disable prettier/prettier */
/**
 * arquivo: typeAnnotation.ts
 * descrição: arquivo responsável por ensinar conceitos básicos sobre 'Type Annotation'
 * data: 16/02/2021
 * author: Glaucia Lemos <@glaucia_lemos86>
 * doc referência: https://www.typescriptlang.org/docs/handbook/2/everyday-types.html
 * Transpilação do arquivo: <Windows> CTRL + SHIFT + B -> tsc: build/watch
 */



// ==> Variáveis [Type Annotations]
let nome: string = "Guilherme";
console.log(nome);

// ==> Arrays [Type Annotations]
let animais: string[] = ["Cachorro", "Gato", "Cavalo", "Papagaio", "Tartaruga", "Elefante", "Panda"];
console.log(animais);      

// ==> Objetos [Type Annotations]
let carro: {
    nome:string;
    ano: number;
    valor:number
}
carro = {nome: "Palio", ano: 2010, valor: 10000}
console.log(carro);

// ==> Functions [Type Annotation]
function multiplicaNumeros(x:number, y:number):number {
    return x * y;
}

let resultado = multiplicaNumeros(10, 20);
console.log(`O resultado da multiplicação dos dois números e: ${resultado}`);

