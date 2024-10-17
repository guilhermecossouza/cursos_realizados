/**Tipos de declarações de arrays 
 * let numeros = [20,30,40];
 * let numeros:number[] = [20,30,40];
 * let numeros:Array<number>=[20,30,40];
 * let numeros:Array<number|string>=[20,30,40, "Guilherme"];
 * let numeros:Array(number|string)=[20,30,40, "Guilherme"];
*/
let numeros:Array<any>=[];
numeros.push(20,30,40);
numeros.push(50); //-> adiciona no final do array
numeros.unshift(10); //-> adiciona no iníco do array
console.log(numeros);

numeros.pop(); //-> retira o último elemento do array
numeros.shift(); //-> retira o primeiro elemento do array
console.log(numeros);


//Declaração array somente de leitura
//Não terá os métodos de de adicionar e remover no array
let numeros_read:ReadonlyArray<number>=[100,200,300];
console.log(numeros);
numeros_read.forEach((element) => {
    console.log(element)
})

