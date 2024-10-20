const arr = [1,2,3,4,5]

const maiorTres = arr.filter((element) => {return element >= 3})
console.log(maiorTres)

const user = [
    {id: 1, username: "Guilherme", status: true},
    {id: 2, username: "João", status: false},
    {id: 3, username: "Maria", status: false},
    {id: 4, username: "thiago", status: true},
]

const usersActivate = user.filter((user) => user.status)
console.log(usersActivate)

const usersNotActivate = user.filter((user) => !user.status)
console.log(usersNotActivate)