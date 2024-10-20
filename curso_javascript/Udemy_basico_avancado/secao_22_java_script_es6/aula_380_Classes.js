class Product {
    constructor(name, price) {
        this.name = name;
        this.price = price;
    }
    discount(descont) {
        this.price = this.price * ((100 - descont) / 100)
    }
}

const shirt = new Product("Camisa Polo", 50.00)
shirt.discount(10);
console.log(shirt.price)
