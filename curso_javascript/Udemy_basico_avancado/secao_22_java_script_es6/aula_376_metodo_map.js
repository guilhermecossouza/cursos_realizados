const products = [
    {name: "Camisa", price: 10.00, category: "roupas"},
    {name: "Calça", price: 20.00, category: "roupas"},
    {name: "Tênis", price: 30.00, category: "calçados"},
    {name: "Bolsa", price: 40.00, category: "acessórios"},
]

products.map((product) => {
    return product.category === "roupas" ? product.onSile = true : product.onSile = false;
});

console.log(products);