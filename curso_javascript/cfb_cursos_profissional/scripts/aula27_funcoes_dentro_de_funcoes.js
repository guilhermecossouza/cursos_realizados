const soma = (...valores) => {
    const somar = valor => {
        let res = 0
        for(num of valor) {
            res += num
        }
        return res
    }
    return somar(valores)
}

let numeros = [1, 2, 3]

console.log(soma(...numeros));