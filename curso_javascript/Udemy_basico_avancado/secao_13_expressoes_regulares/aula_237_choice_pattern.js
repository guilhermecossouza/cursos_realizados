const frutas = /\d+ (banana|maça|laranja)/
console.log(frutas.test("1 banana"));
console.log(frutas.test("2 batata"));
console.log(frutas.test("3 maça"));