"use strict"

const regex = /\d\d\d\d/;
console.log(regex.test("05"));
console.log(regex.test("2024"));
console.log(regex.test("opa"));
console.log("==============================");
const regex1 = /\w\w\w/;
console.log(regex1.test("dia"));
console.log(regex1.test("ano"));
console.log(regex1.test("oi"));
console.log(regex1.test("teste")); 