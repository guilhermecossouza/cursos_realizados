/**
 * doc referência: https://www.typescriptlang.org/docs/handbook/basic-types.html#void
 */

const mensagem = (): void => {
    console.log("Não vai retornar nada");
}

mensagem();

function mensagemErro(erroMessage: string): void {
    console.log(erroMessage);
}

mensagemErro("Mensagem de erro");

