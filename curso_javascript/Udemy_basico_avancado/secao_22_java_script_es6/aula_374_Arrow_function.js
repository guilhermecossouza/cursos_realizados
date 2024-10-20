// const soma = (a, b) => {
//     return a + b
// }
//const soma = (a, b) => { return a + b }
const soma = (a, b) => a + b
console.log(soma(2, 2))

const greeting = (name) => {
    if(name !== undefined) {
        return `hello ${name}`
    }else {
        return "hello!"
    }
}

console.log(greeting("Guilherme"))
console.log(greeting(""))


const user = {
    name: "Guilherme",
    userName() {
        setTimeout(() => {
            console.log(this)
            console.log(`User Name ${this.name}`)
        }, 300);
    }
}

user.userName()
