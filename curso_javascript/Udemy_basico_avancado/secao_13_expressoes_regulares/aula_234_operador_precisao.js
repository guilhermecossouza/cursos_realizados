const regex = /\d{4,5}-\d{4}/

console.log(regex.test("3446-071"));
console.log(regex.test("3446-0719"));
console.log("-------------------------------")

const regexTelefone = /\(\d{2,3}\)\d{4,5}-\d{4}/
console.log(regexTelefone.test("(031)3446-0719"))
console.log(regexTelefone.test("(31)3446-0719"))
console.log(regexTelefone.test("(1)3446-0719"))