// ==> Exemplo 01 - Functions (Named function)
function somarNumeros(num1:number=0, num2:number=0): number {
    return num1 + num2;
}

console.log(somarNumeros());
console.log(somarNumeros(2));
console.log(somarNumeros(3,3));


// ==> Exemplo 02 - Função Anônima (Function Expression)

let somarNumeros2 = function (num1:number=0, num2:number=0): number {
    return num1 + num2;
}
console.log(somarNumeros2());
console.log(somarNumeros2(5));
console.log(somarNumeros2(5,5));

// ==> Exemplo 03 - (Arrow Function Expression)
 let somarNumeros3 = (num1:number=0, num2:number=0, num3?:number): number => {
    if(num3 === undefined) num3 = 0;
    return num1 + num2 + num3;
 }
console.log(somarNumeros3());
console.log(somarNumeros3(1));
console.log(somarNumeros3(10,10));
console.log(somarNumeros3(10,10,10));

// ==> Exemplo 04 - (Function constructor)
const saudar = new Function("mensagem", "return `olá ${mensagem}`;");
console.log(saudar("Guilherme"));