const promise = Promise.resolve(5);
console.log("outros códigos");
console.log(promise);
console.log("mais códigos");
promise.then((value) => console.log(`O valor da promise é ${value}`));

promise.then((value) => {return value + 15})
       .then((value) => console.log(`O valor da promise é ${value}`));


