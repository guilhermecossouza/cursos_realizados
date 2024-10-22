/**
 * doc referência: <number> https://www.typescriptlang.org/docs/handbook/basic-types.html#number
 * doc referência: <bigint> https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-2.html#bigint
 */

// ==> Exemplos: number

const number1:number = 23.5;
const number2:number = 23;
const number3:number = 0b101011;
const number4:number = 0o743;
const number5:number = 0x7b;

console.log(`flutuante: ${number1}`);        
console.log(`inteiro: ${number2}`);
console.log(`binário: ${number3}`);
console.log(`octal: ${number4}`);
console.log('hexadecimal: ' + number5);


// ==> Exemplos: bigint

let big1: bigint = 9007199254740991n;
let big2: bigint = 0b100000000000000000000000000000000000000000000000000011n;;
let big3: bigint = 0x20000000000003n;
let big4: bigint = 0o400000000000000003n;

console.log('Bigint...: ', big1);
console.log('Bigint - Binário...: ', big2);
console.log('Bigint - Hexadecimal...: ', big3);
console.log('Bigint - Octal...: ', big4);