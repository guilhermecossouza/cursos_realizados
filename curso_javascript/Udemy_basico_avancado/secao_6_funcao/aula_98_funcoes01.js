function multiplicarTresNumeros(a, b, c) {
    return a * b * c
}

console.log(multiplicarTresNumeros(1, 2, 3));
resultado = multiplicarTresNumeros(4, 5, 6);

console.log(`O resultado é ${resultado}`)

function podeDirigir(idade, cnh) {
    if (idade >= 18 && cnh) {
        console.log("Pode dirigir");
    } else {
        console.log("Não pode dirigir");
    }
}

podeDirigir(18, true);
podeDirigir(18, false);
podeDirigir(17, false);