export {}

const nome: unknown = "João";
console.log((nome as string).toLowerCase());


const carro: string = "Palio";
const qtdCaracter: number = (<string> carro).length;
//const qtdCaracter: number = carro.length
console.log(qtdCaracter)