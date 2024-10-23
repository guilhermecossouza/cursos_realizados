export {}

// ==> Exemplo 01
function somar_numeros(...numeros: Array<number>): number {
    let total = 0;
    numeros.forEach((numero) => total += numero);  
    return total
}
console.log(somar_numeros(1,2,3))

// ==> Exemplo 02
function lista_compras(mensagem: string, ...frutas: Array<string>): string {   
    return `${mensagem}, ${frutas.join(', ')}`
}
console.log(lista_compras("Guilherme! Você precisa comprar as frutas:", "macã", "melão", "melancia"));

// ==> Exemplo 02
class Produtos {
    public exibir_produtos(...produtos: Array<string>): void {
        for(let produto of produtos) {
            console.log(produto);
        };
    }
}

const departamento_informatica: Produtos = new Produtos();
departamento_informatica.exibir_produtos("Computador", "Mouse", "Teclado", "Monitor");
