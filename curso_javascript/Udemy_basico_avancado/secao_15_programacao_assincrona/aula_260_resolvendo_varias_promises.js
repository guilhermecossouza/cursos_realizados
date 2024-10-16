const promise = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve(5);
    }, 5000);
});

const promise1 = Promise.resolve(10);

const promise2 = new Promise((resolve, reject) => {
    resolve(1000);
})

Promise.all([promise, promise1, promise2]).then((values) => console.log(values));