function fSoma(...numeros:number[]): number {
    let resultado: number = 0
    numeros.forEach((element): void => {
        resultado += element
    });
    return resultado;
}

console.log(fSoma(1, 2, 3,7,9));