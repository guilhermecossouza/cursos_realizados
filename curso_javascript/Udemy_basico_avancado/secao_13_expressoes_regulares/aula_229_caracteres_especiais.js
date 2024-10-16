console.log(/./.test("aSDasd"));
console.log(/./.test(" "));
console.log(/./.test("123"))
console.log(/./.test("123asd"))
console.log("===============================")

console.log(/\d/.test("asd"));
console.log(/\d/.test(" "));
console.log(/\d/.test("123"));
console.log(/\d/.test("asd1234"));
console.log("===============================")

console.log(/\D/.test("asd"));
console.log(/\D/.test(" "));
console.log(/\D/.test("123"));
console.log(/\D/.test("asd1234"));
console.log("===============================")

console.log(/\s/.test("asd"));
console.log(/\s/.test(" "));
console.log(/\s/.test("123"));
console.log(/\s/.test("asd1234"));

console.log("===============================")

console.log(/\w/.test("asd"));
console.log(/\w/.test(" "));
console.log(/\w/.test("123"));
console.log(/\w/.test("asd1234"));
