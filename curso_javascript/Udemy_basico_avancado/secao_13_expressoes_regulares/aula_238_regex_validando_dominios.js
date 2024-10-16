const regex = /[?www.]\w+\.com.br|.com/

console.log(regex.test("www.google.com"))
console.log(regex.test("www.google.com.br"));
console.log(regex.test("w.google.com"));
console.log(regex.test("www.google"));