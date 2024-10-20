const arr1 = [1, 2, 3]
const arr2 = [4, 5, 6]
const arr3 = [...arr1, ...arr2]

console.log(arr3)

const arr4 = [0, ...arr1, 200]
console.log(arr4)

const carName = {name: "Palio"}
const carBrand = {brand: "Fiat"}
const carDetalis = {price: 10000, age: 1997}
const car = {...carName, ...carBrand, ...carDetalis, color: "Azul"}
console.log(car)

