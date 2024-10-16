const regex = /[^0-9]/

console.log(regex.test("11112"))
console.log(regex.test("123"))
console.log(regex.test("1"))
console.log(regex.test("12345"))
console.log(regex.test("456"))