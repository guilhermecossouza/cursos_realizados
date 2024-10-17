//Funcao sem retorno informa void é opcional
function mesagem():void{
    console.log("Hello World");
}
mesagem();

function pessoa():Object{
    return {nome: "Guilherme"};
}
console.log(pessoa());

function logar(username:string, passwoqrd:string):string{
    return `Username: ${username} Password: ${passwoqrd}`;
}
console.log(logar("guilherme", "123456"));


function somaArray(arr:Array<number>):number{
    let total = 0;
    for(let i = 0; i < arr.length; i++){
        total += arr[i];
    }
    return total;
}

let arrNumeros:Array<number>; 
arrNumeros = [1,2,3,4,5,6,7,8,9,10];

let total:number = somaArray(arrNumeros);
console.log(total);


