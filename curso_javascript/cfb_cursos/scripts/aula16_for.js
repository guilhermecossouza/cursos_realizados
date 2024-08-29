for(let count = 0; count < 10; count++) {
    if(count%2 === 0) {
        console.log("contador par " + count);
    }else {
        console.log("contador impar " + count);
    }
}

//montando um array com for

let arrNumeros = []

for(let i = 0; i < 10; i++) {
    arrNumeros[i] = i + 1

}

console.log(arrNumeros);