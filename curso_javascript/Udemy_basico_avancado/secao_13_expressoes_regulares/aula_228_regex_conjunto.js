const regex = new RegExp("[123]")
const regex1 = new RegExp("[0-9]")

console.log(regex.test("existe 123?"));
console.log(regex1.test("tem o número 8?"))