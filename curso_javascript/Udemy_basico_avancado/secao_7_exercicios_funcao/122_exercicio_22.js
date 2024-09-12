const numeroNegatico = (n) => {
    if (typeof(n) == "number"  && n < 0) {
        console.log("zaca")
        return Math.abs(n); 
    }
}
console.log(numeroNegatico(-1));