
function soma1(a=0, b=0) {
    if (a === undefined || b === undefined) {
        console.log("Esta função precisa dos dois parametros");
    }else {
        return a + b
    }
}

console.log(soma1());
console.log(soma1(2, 3));
