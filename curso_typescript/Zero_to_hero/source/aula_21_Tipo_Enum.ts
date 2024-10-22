/**
  * doc referência: https://www.typescriptlang.org/docs/handbook/basic-types.html#enum
 */

// ==> Exemplo 01: Numeric Enums (Enums Numérico)
enum Idioma {
    portugues,
    ingles,
    espanhol,
} 
console.log(Idioma);
console.log(Idioma.ingles)
console.log(Idioma[2])
// ==> Exemplo 02: String Enums
enum Dia {
    Segunda = "Segunda",    
    Terca = "Terça",
    Quarta = "Quarta",
    Quinta = "Quinta",
    Sexta = "Sexta",
    Sabado = "Sabado",
    Domingo = "Domingo",
}

console.log(Dia);
console.log(Dia.Segunda)
console.log(Dia["Domingo"])
  
// ==> Exemplo 03: Como podemos acessar um valor de um Enum com uma chave: (usando o const)
const enum Comida {
    Hambuguer,
    Pizza,
    Batata,
    Frango  
}  

function comida(c: Comida) {
    return "Comida muio apetitosa!";
}

console.log(comida(Comida.Hambuguer));
console.log(comida(Comida.Batata));
//console.log(comida(Comida[2])); erro
   
// ==> Exemplo 04: Quando usar enum?!
