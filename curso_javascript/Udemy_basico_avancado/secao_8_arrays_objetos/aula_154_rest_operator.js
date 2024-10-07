let num = 1;
let num1 = 2;
let num2 = 3;
let num3 = 4;


function imprime_numeros(...args) {
    for(let i = 0; i < args.length; i++) {
        console.log(`valores : ${args[i]}`)
    }
}

imprime_numeros(num, num1, num2, num3)
console.log("---------------------------")
imprime_numeros(num1, num2)
console.log("---------------------------")
imprime_numeros(1,2,3,5,8)
