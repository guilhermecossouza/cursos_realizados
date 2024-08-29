/**
 * A diferença entre os dois e que o:
 * While () verifica a condiçõa lógica antes de executar o bloco
 * D Whilw() executa primeiro o bloco e depois o teste lógico
 */

let num = 0

while(num < 10){
    console.log(num);
    num++
}

num = 100

do {
    console.log("==> " + num); // saida 100
    num++
} while (num < 10); //para aqui


