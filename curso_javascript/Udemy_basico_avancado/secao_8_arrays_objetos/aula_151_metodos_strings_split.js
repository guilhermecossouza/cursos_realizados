let frase = "O rato roeu a roupa do rei de Roma"
let arrFrase = frase.split(" ") 

console.log(frase)
console.log(arrFrase)

arrFrase.forEach((element) => {
    console.log(`Cada palavra da frase ${element}`)
})
