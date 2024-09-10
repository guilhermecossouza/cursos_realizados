function lembrarSoma(x=0) {
    return (y) => {
        return x + y
    }
}

let soma = lembrarSoma(3);
console.log(soma(5))

let soma2 = lembrarSoma(8);
console.log(soma(2))

console.log("=========================");

function contador(i) {
    let count = i;
    let somarContador = function() {
        console.log(count);
        count++;
    }
    return somarContador
}

let meuContador = contador(5);
meuContador();
meuContador();
meuContador();
