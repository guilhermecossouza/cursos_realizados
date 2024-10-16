const regex = /Abacax?i/
//o caracte a esquerda passa a ser opcional

console.log(regex.test("Ab"))
console.log(regex.test("Abacaxi"))
console.log(regex.test("Abacai"))