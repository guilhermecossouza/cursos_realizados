export { }

// function numeros(): number {
//     return Math.floor(Math.random() * 10);
// }


//=> Exemplo 01 generic

function retornaElementosRandomicos<T>(item: T[]): T {
    let elementoAleatorio = Math.floor(Math.random() * item.length);
    return item[elementoAleatorio];
}

let numero: number = retornaElementosRandomicos<number>([1,4,5,6,2,8,9])
let estado: string = retornaElementosRandomicos<string>(["Minas Gerais", "São Paulo", "Rio de Janeiro", "Bahia", "Ceará"])

console.log(numero);
console.log(estado);


//=> Exemplo 02 generic

function exibirElementos<T>(array: T[]): void {
    console.log(array)
}


exibirElementos<number>([1,2,3,4]);
exibirElementos<string>(["Guilherme", "Joaquim", "Lucas"]);
