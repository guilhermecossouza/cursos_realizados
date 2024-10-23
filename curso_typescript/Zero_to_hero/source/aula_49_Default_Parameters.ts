export {}

// ==> Exemplo 01 - Default Parameters
function descontoProduto(price: number, discount: number = 0.08): number{
    return price - (price * discount);
}
console.log(descontoProduto(50));
console.log(descontoProduto(100));

// ==> Exemplo 02
const saudar = (nome: string, mensagem: string = "Bem vindo(a),"): string => {
    return `${mensagem} ${nome}!`
}

console.log(saudar("Guilherme"));