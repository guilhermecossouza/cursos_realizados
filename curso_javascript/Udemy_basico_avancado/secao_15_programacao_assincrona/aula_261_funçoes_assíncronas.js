async function somar(num1, num2) {
    return num1 + num2;
}

console.log(somar(2,2));

somar(2, 2).then((value) => console.log(`A soma é ${value}`));