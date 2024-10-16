"use strict"
function somaComDalay(a,b) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(a + b)
        }, 5000);
    });
}

async function soma(a, b, c, d) {
    let x = somaComDalay(a, b);
    let y = c
    return await x + y
}

soma(1, 2, 3).then((value) => console.log(value));

