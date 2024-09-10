function retornarNumeroPar(n) {
    if (n % 2 === 0) {
        console.log(`O número ${n} é par`);
    }else {
        console.log(n);        
        retornarNumeroPar(n - 1)
    }
}

retornarNumeroPar(11);