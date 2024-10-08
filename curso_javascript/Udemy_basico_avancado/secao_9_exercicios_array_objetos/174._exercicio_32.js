const nomes = ["Guilherme", "Kenia", "Hiago", "Gabriel", "Maria Vitória"];


for (let i = 0; i < nomes.length; i++) {
    console.log(`Nome: ${nomes[i]}`);
}
console.log("======================================");

nomes.map((elementos) => {
    console.log(`Nome: ${elementos}`);
})
console.log("======================================");

nomes.forEach((elementos) => {
    console.log(`Nome: ${elementos}`);
})


