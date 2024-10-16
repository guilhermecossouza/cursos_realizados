function* criadorIds() {
    let id = 0
    while(true) {
        yield id ++;
    }
}

let criaId = criadorIds();

console.log(criaId.next().value);
console.log(criaId.next().value);
console.log(criaId.next().value);
console.log(criaId.next())