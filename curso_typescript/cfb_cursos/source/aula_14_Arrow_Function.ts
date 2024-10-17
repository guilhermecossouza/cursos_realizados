const mostraMensagem = (): void => {
    console.log("Hello World");
}
mostraMensagem();

const mostraCurso = (curso:string, professor?:string):void => {
    console.log(`curso: ${curso}, professor: ${professor}`);
}

mostraCurso("Javascript");
mostraCurso("Typescript");
mostraCurso("Python");

const somar = (n1:number=0, n2:number=0):number => {
    return n1 + n2;
}
console.log(somar(10,20));


const somaArrayNumeros = (arr:number[]): number => {
    let total:number = 0;
    arr.forEach((element:number) => {
        total += element;    
    });
    return total;
}

const numerosArr: number[] = [1,2,3];
console.log(somaArrayNumeros(numerosArr))