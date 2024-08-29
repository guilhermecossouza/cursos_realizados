"use script"
let num = 10
//                    true  :  fase  
let resposta1 = (num % 2 ? "par" : "impar"); // ele vai validar o resultado como true ou false [ O resto da divisão é 0 então ele retorna false ]
console.log(resposta1);
let resposta2 = num % 2 === 0 ? "par" : "impar"; // não precisa usar parenteses
console.log(resposta2);


