"use strict"
// const regex = new RegExp("bola");
// console.log(regex.test("Tem bola?"));
// console.log(regex.test("Não tem bola?"));
// const regex1 = /bola/;
// console.log(regex.test("Tem bola?"));
// console.log(regex.test("Não tem bola?"));
// console.log(/bola/.test("Tem bola?"))

const regex = new RegExp("^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$");


console.log(regex.test("guilhermecossouza@gmail.com"));